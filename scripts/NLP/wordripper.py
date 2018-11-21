import io
from nltk.tokenize import sent_tokenize, word_tokenize

with io.open('<filename.txt>', 'r', encoding="UTF8") as myfile:
    data=myfile.read()

print(word_tokenize(data))
