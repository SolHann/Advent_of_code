def p1(input):
    sum=0
    for l in input:
        a, c = l.split(",")
        a, b = a.split("-")
        c, d = c.split("-")
        if int(a) >= int(c) and int(b) <= int(d) or int(a) <= int(c) and int(b) >= int(d):
            sum += 1
    return sum


def p2(input):
    sum = 0
    for l in input:
        a, c = l.split(",")
        a, b = a.split("-")
        c, d = c.split("-")
        if not (int(b) < int(c) or int(d) < int(a)):
            sum += 1
    return sum


with open('input.txt', 'r') as f:
    items = [line.strip() for line in f]
    print(p1(items))
    print(p2(items))
