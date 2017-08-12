from nltk.corpus import gutenberg as gt

print(gt.fileids())

#words
bible_kjv = gt.words("bible-kjv.txt")
print(bible_kjv)

#raw
bible_kjv = gt.raw("bible-kjv.txt")
print(bible_kjv)

for fileid in gt.fileids():
    raw_data = gt.raw(fileid)
    num_words = gt.words(fileid)
    num_sents = gt.sents(fileid)
    num_words = len(num_words)
    num_sents = len(num_sents)
    print("Data for file :", fileid)
    print("Number of words :", num_sents)
    print("Number of sentences :", num_sents)
    print("Words :", gt.words(fileid), end = '\n\n\n')