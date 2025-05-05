from collections import defaultdict

import spacy
from spacy.language import Language
from spacy.tokens.doc import Doc


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


def extract_relationships(doc: Doc) -> str:
    """
    Extracts the relationships between tokens in the given spaCy document.
    """

    relationships: list = [token.text for token in doc]

    for index, token in enumerate(doc):
        if token.dep_ != "compound":
            relationships[index] += f" ({token.dep_}) -"

    sentence: str = " ".join(relationships)

    # Remove suffix if the last token isn't compound
    return sentence.removesuffix(" -")


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

    print("Relationships:", relationships)


if __name__ == "__main__":
    main()
