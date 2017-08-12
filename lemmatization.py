from nltk import WordNetLemmatizer
from nltk.corpus import brown

#Difference between Stemming and lemmatization

tokens = brown.words(categories=['religion'])

wnl = WordNetLemmatizer()

print(set([wnl.lemmatize(t) for t in tokens]))

text = 'the women are lying'

tokens1 = nltk.word_tokenize(text)
print([wnl.lemmatize(t) for t in tokens1])
