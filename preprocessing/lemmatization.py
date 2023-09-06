import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

text = "Very orderly and methodical he looked, with a hand on each knee, and a loud watch ticking a sonorous sermon under his flapped newly bought waist-coat, as though it pitted its gravity and longevity against the levity and evanescence of the brisk fire."

# tokenize text
tokens = word_tokenize(text)

wordnet_lemmatizer = WordNetLemmatizer()
lemmatized = [wordnet_lemmatizer.lemmatize(token) for token in tokens]
print(lemmatized)

from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

stemmed = [stemmer.stem(token) for token in tokens]

# create dataframe for comparing the stemmer with the lemmatizer
df = pd.DataFrame(
    data={
        "token": tokens,
        "stemmed": stemmed,
        "lemmatized": lemmatized,
    }
)

df = df[["token", "stemmed", "lemmatized"]]

# print only mismatching tokens
df[(df.token != df.stemmed) | (df.token != df.lemmatized)]
