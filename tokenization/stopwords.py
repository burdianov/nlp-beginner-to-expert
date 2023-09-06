from nltk.corpus import stopwords

print(stopwords.words("english"))

sample_text = """Natural language processing refers to the branch of computer science and more specifically, the branch of artificial intelligence or AI concerned with giving computers the ability to understand text and spoken words in much the same way human beings can understand."""

# tokenize sample_text into words
sample_words = sample_text.split()

# identify all the stopwords in sample text
found_stopwords = [word for word in sample_words if word in stopwords.words("english")]

# removing stop words
no_stopwords = [word for word in sample_words if word not in stopwords.words("english")]

# joining back splitted words
sample_text = " ".join(no_stopwords)
