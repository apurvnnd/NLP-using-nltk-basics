from nltk import FreqDist

text = 'Hello ! This is a course designed for people who are interested in learning the core concepts of NLP and ' \
        'utilising those concepts to make applications to perform sentiment analysis analysis'

# Freq Dist - input list

text_list = text.split(' ')
print(text_list)

freqDist = FreqDist(text_list)
words = list(freqDist.keys())
print(words)

print(freqDist['analysis'])