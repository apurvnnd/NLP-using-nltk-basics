from nltk import PorterStemmer, LancasterStemmer
import nltk

tokens = nltk.corpus.brown.words(categories=['romance'])

porter = PorterStemmer()
tokens = ['lying']

print(porter.stem(tokens[0]))

lancast = LancasterStemmer()
print(lancast.stem(tokens[0]))