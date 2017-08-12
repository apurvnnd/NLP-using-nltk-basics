import re

text = 'The tagger was originally written by Kristina Toutanova.' \
        'Since that time, Dan Klein, Christopher Manning, William Morgan,' \
        'Anna Rafferty, Michel Galley, and John Bauer have improved its speed,' \
        'performance, usability, and support for other languages. higher-level'
print(re.split(' ',text))
print(re.split('\s',text))
print(re.split('\W',text))
print(re.findall('\w+|\S|\w*',text))
print(re.findall("\w+[-']+\w+|\w+",text))