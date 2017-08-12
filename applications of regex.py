from nltk.corpus import gutenberg, nps_chat
import nltk

moby = nltk.Text(gutenberg.words("melville-moby_dick.txt"))

#findall - text class - regular expression

print(moby.findall(r'<a><.*><man>'))
chat_obj = nltk.Text(nps_chat.words())
print(chat_obj.findall(r'<.*><.*><bro>'))
print(chat_obj.findall(r'<a><.*><man>'))

text = "Hello, I am a computer programmer who is currently learning and studying NLP"

our_own_text_obj = nltk.Text(nltk.word_tokenize(text))
print(our_own_text_obj.findall(r'<.*ing>+'))