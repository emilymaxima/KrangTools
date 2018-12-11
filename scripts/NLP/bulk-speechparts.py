import nltk
import io
import os

from nltk.tokenize import sent_tokenize, word_tokenize

for filename in os.listdir("."):
    if filename.endswith(".txt"):
        with io.open(filename, 'r', encoding="UTF8") as f:
          data=f.read().replace('\n', '')
          text = word_tokenize(data)
          finished = nltk.pos_tag(text)
          print(finished)
