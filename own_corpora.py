from nltk.corpus import PlaintextCorpusReader
import os

#plaintextcorpusreader expects two inputs -- corpus root and fileids
#corpus root is path from where files are to be read

corpus_root = os.getcwd() + '/'
print(corpus_root)
file_ids = ".*.txt"
corpus = PlaintextCorpusReader(corpus_root, file_ids)
print(corpus)

print(corpus.fileids())
print(corpus.words('shakespeare-taming-2.txt'))
print(len(corpus.words('shakespeare-taming-2.txt')))

print(corpus.words('Machine Learning.txt'))


print(len(corpus.words('Machine Learning.txt')))