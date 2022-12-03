def p1(input):
    sum = 0
    for x in input:
        # Creates set of both halves, finds the intersection of the halves and pops
        dupe = set(x[0:(int(len(x)/2))]).intersection(x[int((len(x)/2)):(int(len(x)))]).pop()
        sum += (ord(dupe)) - 96 if dupe.islower() else ord(dupe) - 38
    return sum


def p2(input):
    i = 0
    sum = 0
    while i < len(input):
        dupe = set(input[i]).intersection(input[i+1], input[i+2]).pop()
        sum += (ord(dupe)) - 96 if dupe.islower() else ord(dupe) - 38
        i += 3
    return sum


with open('input.txt', 'r') as f:
    items = [line.strip() for line in f]
    print(p1(items))
    print(p2(items))
