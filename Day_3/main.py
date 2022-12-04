def p1(input):
    sum = 0
    for l in input:
        # Creates set of both halves, finds the intersection of the halves and pops
        dupe = set(l[0:(int(len(l)/2))]).intersection(l[int((len(l)/2)):(int(len(l)))]).pop()
        sum += (ord(dupe)) - 96 if dupe.islower() else ord(dupe) - 38
    return sum


def p2(input):
    sum = 0
    for l in range(0, len(input), 3):
        dupe = set(input[l]).intersection(input[l+1], input[l+2]).pop()
        sum += (ord(dupe)) - 96 if dupe.islower() else ord(dupe) - 38
    return sum


with open('input.txt', 'r') as f:
    items = [line.strip() for line in f]
    print(p1(items))
    print(p2(items))
