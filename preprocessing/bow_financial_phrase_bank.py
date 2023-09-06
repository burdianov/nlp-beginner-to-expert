import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


df = pd.read_csv("../datasets/finbank_data.csv")


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


# take a subset of data (first 50 rows only)
df = df.iloc[:50, :]

# extract the messages from the dataframe
texts = df["text"]

# convert messages into list
messages = [text for text in texts]

# preprocess messages using the preprocess function
messages = [preprocess(message) for message in messages]

# creating bag of words model
vectorizer = CountVectorizer()
bow_model = vectorizer.fit_transform(messages)

# creating dataframe from bag of words matrix representation
df_bow = pd.DataFrame(bow_model.toarray(), columns=vectorizer.get_feature_names_out())

print(vectorizer.get_feature_names_out())
