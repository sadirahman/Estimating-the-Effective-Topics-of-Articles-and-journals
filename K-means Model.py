from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

#S2
# documents = ["An increasing number of people are changing their way of thinking by reading news headlines. The interactivity and sincerity present in online news headlines are becoming influential to society. ",
#               "Apart from that, news websites build efficient policies to catch people’s awareness and attract their clicks. In that case, it is a must to identify the sentiment polarity of the news headlines for avoiding misconceptions.",
#               " In this paper, we analyze 3383 news headlines generated by five major global newspapers during a minimum of four consecutive months. In order to identify the sentiment polarity (or sentiment orientation) of news headlines, we use 7 machine learning algorithms and compare those results to find the better ones.",
#               " Among those Bernoulli Naïve Bayes technique achieves higher accuracy than others. ",
#               "This study will help the public to make any decision based on news headlines by avoiding misconceptions against any leader or governance and will help to identify the most neutral newspaper or news blogs."]


#S1
# documents = ["Analyzing short text or documents using topic modeling becomes a popular solution for the increasing number of documents produced in everyday life.",
#              " For handling a large amount of documents, many topic modeling algorithms are used e.g. LDA, LSI, pLSI, NMF. ",
#              "In this study, we have used LDA, LSI, NMF and also lexical database WordNet synset for candidate labels in our topics labeling.",
#              " And ﬁnally compare the eﬀectiveness of topic modeling algorithms for short documents. Among those LDA gives a better result in terms of WUP similarity.",
#              " This study will help to select the proper algorithm for labeling topics and can easily identify the meaning of topics."

#]

documents = ["Topics generated by topic models are typically reproduced as a list of words.",
             " To decrease the cognitional overhead of understanding these topics for end-users,",
             " We have proposed labeling topics with a noun phrase that summarizes its theme or idea",
             " Using the WordNet lexical database as candidate labels, we estimate natural labeling for documents with words to select the most relevant labels for topics.",
             "Compared to WUP similarity topic labeling system, our methodology is simpler, more effective, and obtains better topic labels."

]


vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

true_k = 3
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :3]:
        print(' %s' % terms[ind]),
    print

print("\n")
print("Prediction")

Y = vectorizer.transform(["google chrome browser to open."])
prediction = model.predict(Y)
print(prediction)

Y = vectorizer.transform(["My cat ninja is hungry."])
prediction = model.predict(Y)
print(prediction)