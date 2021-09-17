import spacy



def ginza(text_data):
    nlp = spacy.load('ja_ginza')
    doc = nlp(text_data)

    for sent in doc.sents:
        for token in sent:
            if token.pos_ == 'NOUN':
                print(token.orth_)
                return token.orth_
            