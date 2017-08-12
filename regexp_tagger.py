import nltk

patterns = [(r'.*ing$','VBG'),(r'.*','NN')] #tagging pos using regular expression all at once
#here r'.*' is used at the end so as to tag the remaining ones at the end, if it is used
# in the begining, all the words will be tagged as "NN" which is not right.

text = 'i am playing football'

regex_tag = nltk.RegexpTagger(patterns)
print(regex_tag.tag(nltk.word_tokenize(text)))

patterns = [(r'.*ing$', 'VBG'), (r'.*ed$', 'VBD'), (r'.*es$', 'VBZ'), (r'.*ould$', 'MD'), (r'.*\'s$', 'NN$'),
             (r'.*s$', 'NNS'),  (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), (r'.*', 'NN')]
#these patterns tags all the words at once
#note what is used at last.

regexp_tagger = nltk.RegexpTagger(patterns)
print(regexp_tagger.tag(nltk.corpus.brown.words()))

