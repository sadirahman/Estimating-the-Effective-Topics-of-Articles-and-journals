from nltk.corpus import gutenberg
from gensim.models import word2vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from string import punctuation

id_f = gutenberg.fileids()
print(id_f)
austen_emma_words = gutenberg.words('austen-emma.txt')
print(len(austen_emma_words))
austen_emma_sents = gutenberg.sents('austen-emma.txt')
print(len(austen_emma_sents))
print(austen_emma_sents[0])
print(austen_emma_sents[5000])

bible_kjv_words = gutenberg.words('bible-kjv.txt')
print(len(bible_kjv_words))
bible_kjv_sents = gutenberg.sents('bible-kjv.txt')
print(len(bible_kjv_sents))
print(punctuation)
discard_punctuation_and_lowercased_sents = [[word.lower() for word in sent if word not in punctuation] for sent in bible_kjv_sents]

print(discard_punctuation_and_lowercased_sents[0])

bible_kjv_word2vec_model = word2vec.Word2Vec(discard_punctuation_and_lowercased_sents, min_count=5, size=200)
bible_kjv_word2vec_model.save("bible_word2vec_gensim")
bible_kjv_word2vec_model.wv.save_word2vec_format("bible_word2vec_org", "bible_word2vec_vocabulary")
result = bible_kjv_word2vec_model.most_similar(["process"], topn=10)
print(result)
