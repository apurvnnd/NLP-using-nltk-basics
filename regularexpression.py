from nltk.tokenize import word_tokenize, sent_tokenize
import re

def read_file(filename):
    with open(filename,'r') as file:
        text = file.read()
    return text

text = read_file('shakespeare-taming-2.txt')
words = word_tokenize(text)

#search function
# takes 2 parameters - regex pattern and word/string on which we wanna apply the pattern
print(re.search('^ab','abc'))

if re.search('^ab','Abc'):
    print('Found it!')
    

#words ending with ed
words_ending_with_ed = [w for w in words if re.search('ed$',w)]
print(words_ending_with_ed)

print(set([w for w in words if re.search('^a+',str(w).lower())]))