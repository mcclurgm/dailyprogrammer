num = raw_input("num")
denom = raw_input("denom")

if num < denom:
    min = num
else:
    min = denom

i = 0
while i < len(num):
    c = num[i]
    while True:
        dc = denom.find(c)
        if dc < 0:
            i += 1
            break
        else:
            num = num[:i] + num[i + 1:]
            denom = denom[:dc] + denom[dc + 1:]


if denom == "":
    out = num
else:
    out = "%s/%s" % (num, denom)
print out
