import nltk
from nltk.corpus import gutenberg as gt

#input - list of words
#output - returns a list of unusual words

# My name is ABC

def unusual_words(text):
    text_vocab = set([w.lower() for w in text if w.isalpha()])
    english_vocab = set([w.lower() for w in nltk.corpus.words.words()])
    unusual_list = text_vocab.difference(english_vocab)
    return sorted(unusual_list)

list_of_unusual_words = unusual_words(gt.words('austen-emma.txt'))

print(list_of_unusual_words)

from nltk.corpus import stopwords

print(stopwords.words('english'))