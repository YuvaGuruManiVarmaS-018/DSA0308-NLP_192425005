
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Machine learning is used in AI",
    "Python is a programming language",
    "AI uses machine learning techniques"
]

query = ["machine learning"]

vectorizer = TfidfVectorizer()

tfidf = vectorizer.fit_transform(documents)
query_vector = vectorizer.transform(query)

scores = cosine_similarity(query_vector, tfidf)

for i, score in enumerate(scores[0]):
    print("Document", i + 1, ":", round(score, 3))

print("Most relevant document:",
      scores.argmax() + 1)
