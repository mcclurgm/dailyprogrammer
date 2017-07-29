num = input("num")
denom = input("denom")

if num < denom:
    min = num
else:
    min = denom

for i in range(1,min + 1):
    if num % i == 0 and denom % i == 0:
        num = num / i
        denom = denom / i
    if i > num or i > denom:
        break

if denom == 1:
    out = num
else:
    out = "%i/%i" % (num, denom)
print out
