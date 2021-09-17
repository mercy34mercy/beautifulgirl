import spacy



def ginza(text_data):
    nlp = spacy.load('ja_ginza')
    doc = nlp(text_data)

    for sent in doc.sents:
        for token in sent:
            if token.pos_ == 'NOUN':
                #url = get_image(top_key + token.orth_)
                print(token.orth_)
                return token.orth_
            #ここ直す

# text_data = "私の名前は小林"
# ginza(text_data)