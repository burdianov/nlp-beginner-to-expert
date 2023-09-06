import re

string = "A regular expression is a sequence of characters that specifies a search pattern in the text."

pattern = "sequence"

result = re.search(pattern, string)

start_pos = result.start()
end_pos = result.end()
