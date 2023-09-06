import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

pd.set_option("max_colwidth", 100)

documents = [
    "Machine learning uses historical data to predict output values.",
    "It is seen as a part of artificial intelligence.",
    "Machine learning programs can perform tasks without being explicitly programmed to do so.",
]

print(documents)
