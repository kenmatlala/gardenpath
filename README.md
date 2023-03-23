# Garden Path

This Python script demonstrates the use of the `spacy` library to tokenize and perform entity recognition on a list of garden path sentences. 

## Requirements

- `spacy` library
- Python 3.10
- en_core_web_sm 3.2.0

To install the required libraries, run the following command:
- pip install -r requirements.txt

## Usage

1. Clone this repository to your local machine.
2. Install the required libraries (see Requirements section).
3. Run the following command to execute the script:

  - python garden_path.py
  

## Output

The script will tokenize each sentence in the `gardenpathSentences` list and perform entity recognition using the `en_core_web_sm` model from the `spacy` library. For each token in each sentence, the script will print the token text, the POS tag, and the entity type. 

## Example

1. Sentence: The horse raced past the barn fell.
- Token: The POS tag: DET Entity: (None)
- Token: horse POS tag: NOUN Entity: (None)
- Token: raced POS tag: VERB Entity: (None)
- Token: past POS tag: ADP Entity: (None)
- Token: the POS tag: DET Entity: (None)
- Token: barn POS tag: NOUN Entity: (None)
- Token: fell POS tag: VERB Entity: (None)

2. Sentence: The old man the boat.
- Token: The POS tag: DET Entity: (None)
- Token: old POS tag: ADJ Entity: (None)
- Token: man POS tag: NOUN Entity: PERSON (People, including fictional)
- Token: the POS tag: DET Entity: (None)
- Token: boat POS tag: NOUN Entity: (None)

3. Sentence: The complex houses married and single soldiers and their families.
- Token: The POS tag: DET Entity: (None)
- Token: complex POS tag: ADJ Entity: (None)
- Token: houses POS tag: NOUN Entity: (None)
- Token: married POS tag: ADJ Entity: (None)
- Token: and POS tag: CCONJ Entity: (None)
- Token: single POS tag: ADJ Entity: (None)
- Token: soldiers POS tag: NOUN Entity: PERSON (People, including fictional)
- Token: and POS tag: CCONJ Entity: (None)
- Token: their POS tag: ADJ Entity: (None)
- Token: families POS tag: NOUN Entity: (None)

4. Sentence: The chicken is ready to eat.
- Token: The POS tag: DET Entity: (None)
- Token: chicken POS tag: NOUN Entity: ANIMAL (Animals, including humans)
- Token: is POS tag: AUX Entity: (None)
- Token: ready POS tag: ADJ Entity: (None)
- Token: to POS tag: PART Entity: (None)
- Token: eat POS tag: VERB Entity: (None)

5. Sentence: I convinced her children are noisy.
- Token: I POS tag: PRON Entity: (None)
- Token: convinced POS tag: VERB Entity: (None)
- Token: her POS tag: DET Entity: (None)
- Token: children POS tag: NOUN Entity: PERSON (People, including fictional)
- Token: are POS tag: AUX Entity: (None)
- Token: noisy POS

## License

This code is licensed under the MIT License.

