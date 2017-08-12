from nltk.book import *

freqDist = FreqDist(text1)

print(freqDist)

words = freqDist.keys()

print(type(words))

print(words)

print(freqDist['short'])
freqDist.plot(21)