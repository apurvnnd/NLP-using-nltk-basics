from nltk.tokenize import word_tokenize, sent_tokenize

def read_file(filename):
    with open(filename,'r') as file:
        text = file.read()
    return text

text = read_file('shakespeare-taming-2.txt')

# word_tokenize - inputs --> string containing the text
#               - output --> list of words
words = word_tokenize(text)
print(print(words)) #use set to prevent duplicates print(set(word))


# sent_tokenize - inputs --> string containing the text
#               - output --> list of sentences
sentences = sent_tokenize(text)
for sentence in sentences:
    print(sentence)