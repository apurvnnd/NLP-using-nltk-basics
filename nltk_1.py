from nltk.book import *


#texts function
print(texts())

#sents function
print(sents())
print(sent1)

print(text1)
print(type(text1))
print(type(1.0))



#finds all the word of the name 'man'
print(text1.concordance('man'))


#finds all the similar words related to woman
print(text1.similar('woman'))

#dispersion plot - tells about how the words are distributed throughout
print(text4.dispersion_plot(['democracy','freedom','law','apurv']))

#len
print(len(text5))

#count
print(text4.count('freedom'))
