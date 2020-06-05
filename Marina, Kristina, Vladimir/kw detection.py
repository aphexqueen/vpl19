from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation
import json

mystem = Mystem()
russian_stopwords = stopwords.words("russian") + ["ко"]

with open("frequencies.json", encoding="utf8") as doc:
    corpora = json.load(doc)
    corp_total = 0
    for i in corpora:
        corp_total += corpora[i]

# instead of file.txt insert the doc you want to exctract key words from
with open("file.txt", encoding="utf8") as doc:
    tokens = mystem.lemmatize(doc.read().lower())
    tokens = [token for token in tokens if token not in russian_stopwords \
              and token != " " \
              and token.strip() not in punctuation]
    tokens = [token for token in tokens if token.isalpha() and len(token) > 1]


# calculating frequencies for each token in both your text and corpora
doc_frqn = {}
corp_frqn = {}
for token in tokens:
    doc_frqn[token] = tokens.count(token) / len(tokens)
    try:
        corp_frqn[token] = corpora[token]  / corp_total
    except KeyError:
        corp_frqn[token] = 0


# calculating expected frequency for each token in your text
expected = {}
for token in doc_frqn.keys():
    a = doc_frqn[token]
    b = corp_frqn[token]
    c = 1 - a
    d = 1 - b
    expected[token] = ((a + b) * (a + c)) / (a + b + c + d)

# calculating chi2 mean for each token in your text
chi = {}
for token in expected.keys():
    o = doc_frqn[token]
    e = expected[token]
    chi[token] = ((o - e) ** 2) / e

# soring tokens according to chi
l = list(chi.items())
l.sort(key=lambda i: i[1])
l = l[::-1]

# detecting significant tokens
Q = 0.003932
key_words = []
for i in l:
    if i[1] <= Q:
        key_words.append(i[0])

for i in key_words:
    print(i)