import re

re.findall("ab*c", "ac")
# ['ac']
re.findall("ab*c", "abcd")
# ['abc']
re.findall("ab*c", "acc")
# ['ac']
re.findall("ab*c", "abcac")
# ['abc', 'ac']
re.findall("ab*c", "abdc")
# []

re.findall("ab*c", "ABC")
# []
re.findall("ab*c", "ABC", re.IGNORECASE)
# ['ABC']

re.findall("a.c", "abc")
# ['abc']
re.findall("a.c", "abbc")
# []
re.findall("a.c", "ac")
# []
re.findall("a.c", "acc")
# ['acc']
re.findall("a.*c", "abc")
# ['abc']
re.findall("a.*c", "abbc")
# ['abbc']
re.findall("a.*c", "ac")
# ['ac']
re.findall("a.*c", "acc")
# ['acc']
