import re

sample_sent = ["0101", "01011", "010111", "010", "01", "011", "0"]


def process(pattern: str, sample: list):
    for s in sample:
        result = re.search(pattern, s)
        if result != None:
            print(True)
        else:
            print(False)


pattern = "0101*"

process(pattern, sample_sent)

sample_sent = ["10", "100", "1000", "0", "1", "15"]

pattern = "10+"

process(pattern, sample_sent)
