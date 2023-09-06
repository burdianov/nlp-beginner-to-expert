from nltk.stem import PorterStemmer

words = ["generous", "fairly", "sings", "generation"]

porter = PorterStemmer()
for word in words:
    print(word, "--->", porter.stem(word))


from nltk.stem import SnowballStemmer

snowball = SnowballStemmer(language="english")
for word in words:
    print(word, "--->", snowball.stem(word))

from nltk.stem import LancasterStemmer

lancaster = LancasterStemmer()
for word in words:
    print(word, "--->", lancaster.stem(word))
