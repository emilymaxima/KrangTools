import io
import os
from nltk.tokenize import sent_tokenize, word_tokenize

for filename in os.listdir("."):
    if filename.endswith(".txt"):
        with io.open(filename, 'r', encoding="UTF8") as f:
            data=f.read()
            print(word_tokenize(data))
    else:
        continue
