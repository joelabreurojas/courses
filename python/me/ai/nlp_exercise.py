from collections import defaultdict

import spacy
from spacy.language import Language
from spacy.tokens.doc import Doc
from spacy.tokens.token import Token


def main() -> None:
    nlp: Language = spacy.load(name="en_core_web_sm")

    text: str = "Elon Musk founded SpaceX in Hawthorne, California."

    doc: Doc = nlp(text)

    formatted_doc: Doc = preprocess_doc(doc, nlp)

    parts_of_speech: dict = extract_pos(formatted_doc)

    name_entities: dict = extract_ner(doc)

    relationships: list = extract_svo(doc)

    display_results(text, formatted_doc, parts_of_speech, name_entities, relationships)


def preprocess_doc(doc: Doc, nlp: Language) -> Doc:
    tokens: list[str] = [
        token.lemma_
        for token in doc
        if not token.is_stop and not token.is_punct and not token.is_space
    ]

    return nlp(" ".join(tokens))


def extract_pos(doc: Doc) -> dict:
    parts_of_speech: dict = defaultdict(list)

    for token in doc:
        parts_of_speech[token.pos_].append(token.text)

    return parts_of_speech


def extract_ner(doc: Doc) -> dict:
    named_entities: dict = defaultdict(list)

    for ent in doc.ents:
        named_entities[ent.label_].append(ent.text)

    return named_entities


def extract_svo(doc: Doc) -> list:
    svo_list: list = []

    for token in doc:
        # if the token is a subject
        if token.dep_ == "nsubj":
            subject: str = " ".join([t.text for t in token.subtree])
            subject += f" ({token.dep_})"

            potential_verb: Token = token.head

            # if the head of the token is a verb
            if potential_verb.pos_ == "VERB":
                verb: str = f"{potential_verb.lemma_} ({potential_verb.dep_})"

                if object_ := _find_object(potential_verb):
                    svo_list.append(f"{subject} - {verb} - {object_}")

    return svo_list


def display_results(
    text: str,
    formmatted_doc: Doc,
    parts_of_speech: dict,
    name_entities: dict,
    relationships: list,
):
    print("Original Text:", text)
    print("Preprocessed Text:", formmatted_doc)

    print("Parts of Speech:")
    for pos, tokens in parts_of_speech.items():
        print(f"  {pos}: {', '.join(tokens)}")

    print("Named Entities:")
    for ent, tokens in name_entities.items():
        print(f"  {ent}: {', '.join(tokens)}")

    print("Relationships:")
    for relationship in relationships:
        print(f"  {relationship}")


def _find_object(verb: Token) -> str | None:
    for child in verb.children:
        # if the child is a direct, indirect or prepositional object
        if child.dep_ in ["dobj", "iobj", "pobj"]:
            object_: str = " ".join([t.text for t in child.subtree])

            return f"{object_} ({child.dep_})"

    return None


if __name__ == "__main__":
    main()
