thing = [0,1]
counter = 2

end = input()

ops = 0

print 0, 1

while counter <= end:
    ops += 4
    thing.append(thing[0] + thing[1])
    del thing[0]
    counter += 1

    print thing[-1]

print thing[-1]
print ops