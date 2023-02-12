import re

match_results = re.search("ab*c", "ABC", re.IGNORECASE)
match_results.group()
# 'ABC'

# Greedy matching:
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)
print(string)
# 'Everything is ELEPHANTS.'
# re.sub is greedy by default, so the above execution replaces everything up to the closing >.

# Non-greedy matching with ?:
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string)
print(string)
# 'Everything is ELEPHANTS if it's in ELEPHANTS.'

