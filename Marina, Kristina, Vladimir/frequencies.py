#creating frequencies.json

from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation
import time as t
import json

mystem = Mystem()
russian_stopwords = stopwords.words("russian") + ["ко"]

with open("ugrams from ruscorpora.txt", encoding = "utf8") as doc:
    corpora = doc.readlines()

#following may take some time
#for quicker performance run on kaggle or somewhere
d = {}
for i in corpora:
    if i.split()[1] not in russian_stopwords:
        token = mystem.lemmatize(i.split()[1])
        if token[0] not in d and token[0] not in russian_stopwords and token[0].isalpha() and len(token[0]) > 1:
            d[token[0]] = int(i.split()[0])
        if token[0] in d:
             d[token[0]] = int(i.split()[0]) + int(d[token[0]])

with open("frequencies.json", "w", encoding = "utf8") as doc:
    json.dump(d, doc)