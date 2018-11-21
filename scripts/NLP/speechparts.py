import nltk
import io
from nltk.tokenize import sent_tokenize, word_tokenize

with io.open('<filename.txt>', 'r', encoding="UTF8") as myfile:
    data=myfile.read().replace('\n', '')

text = word_tokenize(data)
finished = nltk.pos_tag(text)

print(finished)

# print(word_tokenize(data))
