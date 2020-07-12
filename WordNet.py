from nltk.corpus import wordnet


syns = wordnet.synsets("program")

#synset
#print(syns[0])


#print(syns[0].lemmas())

#Just the word
print(syns[0].lemmas()[0].name())

#definition
#print(syns[0].definition())

#example
print(syns[0].examples())

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))


print("wup similar result")
w1 = wordnet.synset("noun.n.01")
w2 = wordnet.synset("person.n.01")
print(w1.wup_similarity(w2))
print("result one")

w1 = wordnet.synset("noun.n.01")
w2 = wordnet.synset("content.n.01")
print(w1.wup_similarity(w2))
print("result Two")

w1 = wordnet.synset("noun.n.01")
w2 = wordnet.synset("word.n.01")
print(w1.wup_similarity(w2))
print("result Three")


w1 = wordnet.synset("noun.n.01")
w2 = wordnet.synset("object.n.01")
print(w1.wup_similarity(w2))
print("result Four")

w1 = wordnet.synset("noun.n.01")
w2 = wordnet.synset("preposition.n.01")
print(w1.wup_similarity(w2))
print("result Five")

# w1 = wordnet.synset("Patient.n.01")
# w2 = wordnet.synset("person.n.01")
# print(w1.wup_similarity(w2))
#
#
# w1 = wordnet.synset("feel.n.01")
# w2 = wordnet.synset("awareness.n.01")
# print(w1.wup_similarity(w2))
# #
# w1 = wordnet.synset("say.n.01")
# w2 = wordnet.synset("chance.n.01")
# print(w1.wup_similarity(w2))
#
#
# w1 = wordnet.synset("Stress.n.01")
# w2 = wordnet.synset("awareness.n.01")
# print(w1.wup_similarity(w2))
#
# w1 = wordnet.synset("Drug.n.01")
# w2 = wordnet.synset("Substance.n.01")
# print(w1.wup_similarity(w2))
#
# w1 = wordnet.synset("feeling.n.01")
# w2 = wordnet.synset("Confidence.n.01")
# print(w1.wup_similarity(w2))
#
# w1 = wordnet.synset("like.n.01")
# w2 = wordnet.synset("case.n.01")
# print(w1.wup_similarity(w2))








