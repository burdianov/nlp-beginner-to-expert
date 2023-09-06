import re

sample_sent = ["abc", "ab", "ac", "a", "Abbc", "Abcc", "Abb", "Acc", "bc"]

pattern = "ab?c?"

for sent in sample_sent:
    result = re.search(pattern, sent)
    if result != None:
        print(f"string found at position: {result.start()}")
    else:
        print("string not found")
