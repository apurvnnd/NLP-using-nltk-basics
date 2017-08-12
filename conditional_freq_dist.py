from nltk.corpus import brown

#Introduction to Brown Corpus
print(brown.categories())

#Accessing words to Brown Corpus

print(brown.words(categories='lore'))

#Introduction to Conditional Frequency Distribution
from nltk import ConditionalFreqDist #imports statement

# pair_list [ (condition, word) ]
pair_list = [(category,word) for category in brown.categories() for word in brown.words(categories=category)]

print(pair_list[:10])

freqdist = ConditionalFreqDist(pair_list)
print(freqdist['lore']['the'])


#Conditional Method


#tabulate functions

category = ['adventure','lore','news']
samples = ['the','and','man']
freqdist.tabulate(conditions=category,samples=samples)