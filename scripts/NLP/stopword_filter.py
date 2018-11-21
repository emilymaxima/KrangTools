from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize




filename = "<filename.txt>"
file = open(filename, "r")
for line in file:
  stop_words = set(stopwords.words("english"))
  print(stop_words)
# print line,
#  close()
