import spacy

# Load the English language model
nlp: spacy.language.Language = spacy.load("en_core_web_sm")

# Sample text
text: str = "Apple Inc. is headquartered in Cupertino, California."

# Process the text
doc: spacy.tokens.doc.Doc = nlp(text)

# Tokenization
print("Tokens:", [token.text for token in doc])

# Part-of-speech tagging
print("POS Tags:", [(token.text, token.pos_) for token in doc])

# Named Entity Recognition
print("Named Entities:", [(ent.text, ent.label_) for ent in doc.ents])

# Sentence Segmentation
for sent in doc.sents:
    print("Sentence:", sent.text)

# Lemmatization
print("Lemmas:", [(token.text, token.lemma_) for token in doc])
