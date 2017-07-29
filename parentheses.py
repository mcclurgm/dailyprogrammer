s = "()"
pairs = []
for i, char in enumerate(s):
    print i, char
    if i == '(':
        pairs.append([i])
for i in s:
    if i == '(':
        pass