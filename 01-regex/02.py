import re

sample_sent = [
    "She pulled out her coin purse.",
    "She flipped both the coins and looked down.",
    "It's very humid outside",
    "you must not ask for more rupees",
]

pattern = "coins?"

for sent in sample_sent:
    result = re.search(pattern, sent)
    if result != None:
        start_pos = result.start()
        print(start_pos)
        end_pos = result.end()
        print(end_pos)
    else:
        print("Not found")
