from nltk.tokenize import word_tokenize, sent_tokenize, TweetTokenizer, regexp_tokenize

document = """To keep your marriage brimming. With love in the loving cup. Whenever you're wrong, admit it. Whenever you're right, shut up."""

document.split()

words = word_tokenize(document)

sentences = sent_tokenize(document)

msg = "WIN with PRIMI to celebrate #NationalPizzaDay! RT this tweet, tell us what your fav PRIMI PIZZA is & stand to WIN a R250 voucher. This is gr8 <3  🥳🍕"

print(msg)

tokenizer = TweetTokenizer()

tokenizer.tokenize(msg)

message = "WIN with PRIMI to celebrate #NationalPizzaDay! RT this tweet, tell us what your fav PRIMI PIZZA is & stand to WIN a R250 voucher. This is gr8 <3  🥳🍕"

pattern = "#[\w]+"

regexp_tokenize(message, pattern)
