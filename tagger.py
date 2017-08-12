import nltk
text = 'We are learning Natural Language Processing'
tokens = nltk.word_tokenize(text)
print(nltk.pos_tag(tokens))

#what is pos tag returning
# guide to each tag
print(nltk.help.upenn_tagset('PRP'))

#SIMILAR TEXTS
tokens = [word.lower() for word in nltk.corpus.brown.words()]
text = nltk.Text(tokens)
print(nltk.pos_tag(['woman']))
print(text.similar('woman'))