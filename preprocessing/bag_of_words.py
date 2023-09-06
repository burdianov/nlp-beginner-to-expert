import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

pd.set_option("max_colwidth", 100)

docs = [
    "Machine learning uses historical data to predict output values.",
    "It is seen as a part of artificial intelligence.",
    "Machine learning programs can perform tasks without being explicitly programmed to do so.",
]

print(docs)


def preprocess(document: str):
    # change sentence to lower case
    document = document.lower()

    # tokenize into words
    words = word_tokenize(document)

    # remove stop words
    words = [word for word in words if word not in stopwords.words("english")]

    # join back the words
    document = " ".join(words)

    return document


docs = [preprocess(document) for document in docs]

vectorizer = CountVectorizer()

bow_model = vectorizer.fit_transform(docs)
bow_model_array = bow_model.toarray()
