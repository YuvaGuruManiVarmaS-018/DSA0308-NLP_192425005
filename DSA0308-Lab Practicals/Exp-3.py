import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('wordnet', quiet=True)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = input("Enter words: ").split()
print("Mani Varma-192425005")
for word in words:
    word = word.lower()
    print("Word:", word)
    print("Stem:", stemmer.stem(word))
    print("Lemma:", lemmatizer.lemmatize(word))
