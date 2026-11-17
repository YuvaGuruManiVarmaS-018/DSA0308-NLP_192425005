
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = [
    "Machine learning is a part of artificial intelligence",
    "Machine learning uses data to train models",
    "Football is a popular outdoor sport"
]

vectorizer = CountVectorizer()
matrix = vectorizer.fit_transform(text)

similarity = cosine_similarity(matrix)

score = (
    similarity[0, 1] + similarity[1, 2]
) / 2

print("Coherence Score:", round(score, 2))

if score > 0.1:
    print("Text has some coherence")
else:
    print("Text has low coherence")
