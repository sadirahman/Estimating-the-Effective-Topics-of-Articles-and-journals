from nltk.corpus import wordnet
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize ,word_tokenize
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from gensim import corpora, models
import nltk
from nltk.corpus import wordnet
import tokenize
import gensim

tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')
p_stemmer = PorterStemmer()
l_lemma = WordNetLemmatizer()
syns = wordnet.synsets("noun")

des = []

n_doc_a = ""
n_doc_b = ""
n_doc_c = ""
n_doc_d = ""
n_doc_e = ""

for i in range(2):
    if i == 0:
        n_doc_a = syns[i].definition()
        print(n_doc_a)
    elif i == 1:
        n_doc_b = syns[i].definition()
    elif i == 2:
        n_doc_c = syns[i].definition()
    elif i == 3:
        n_doc_d = syns[i].definition()
    elif i == 4:
        n_doc_e = syns[i].definition()

#     des.append(syns[i].definition())
#     des.append(".")
# print(des)

n_doc_set = [n_doc_a, n_doc_b, n_doc_c, n_doc_d, n_doc_e]
n_texts = []
for i in n_doc_set:
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]

    # stem tokens
    stemmed_tokens = [l_lemma.lemmatize(i) for i in stopped_tokens]

    n_texts.append(stemmed_tokens)

print(n_texts)

n_l = []
n_m = []

# for i in texts:
n_a = nltk.pos_tag(n_texts[0])
n_nn_tagged = [(word, tag) for word, tag in n_a if tag.startswith('NN') or tag.startswith('NNP')]

for i in n_nn_tagged:
    n_m.append(i[0])
n_l.append(n_m)

n_n = []
n_a = nltk.pos_tag(n_texts[1])
n_nn_tagged = [(word, tag) for word, tag in n_a if tag.startswith('NN') or tag.startswith('NNP')]

for i in n_nn_tagged:
    n_n.append(i[0])
n_l.append(n_n)

n_o = []
n_a = nltk.pos_tag(n_texts[2])
n_nn_tagged = [(word, tag) for word, tag in n_a if tag.startswith('NN') or tag.startswith('NNP')]

for i in n_nn_tagged:
    n_o.append(i[0])
n_l.append(n_o)

n_p = []
n_a = nltk.pos_tag(n_texts[3])
n_nn_tagged = [(word, tag) for word, tag in n_a if tag.startswith('NN') or tag.startswith('NNP')]

for i in n_nn_tagged:
    n_p.append(i[0])
n_l.append(n_p)

n_q = []
n_a = nltk.pos_tag(n_texts[4])
n_nn_tagged = [(word, tag) for word, tag in n_a if tag.startswith('NN') or tag.startswith('NNP')]

for i in n_nn_tagged:
    n_q.append(i[0])
n_l.append(n_q)
print(n_l)
