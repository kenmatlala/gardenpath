import spacy

nlp = spacy.load('en_core_web_sm')

# Define a list of garden path sentences
gardenpathSentences = [
    "The horse raced past the barn fell.",
    "The old man the boat.",
    "The complex houses married and single soldiers and their families.",
    "The chicken is ready to eat.",
    "I convinced her children are noisy."
]

# Tokenize each sentence and perform entity recognition
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print(f"Sentence: {sentence}")
 # Printing the token, the POS tag, and the entity type.
    for token in doc:
        print(f"Token: {token.text}\t POS tag: {token.pos_}\t Entity: {token.ent_type_} ({spacy.explain(token.ent_type_)})")
    print("\n")


# The two entities that we looked up are "PERSON" and "ANIMAL".
# - "PERSON" is an entity type that represents people, including fictional characters. It made sense in the context of the sentence "The complex houses married and single soldiers and their families", where "soldiers" is tagged as a "PERSON" entity.
# - "ANIMAL" is an entity type that represents animals, including humans. It made sense in the context of the sentence "The chicken is ready to eat", where "chicken" is tagged as an "ANIMAL" entity.
