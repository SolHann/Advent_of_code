def p1(input):
    for c in range(4, len(input)):
        if len(set(input[c-4:c])) == 4:
            return c


def p2(input):
    for c in range(14, len(input)):
        if len(set(input[c-14:c])) == 14:
            return c


with open('../Day_7/input.txt', 'r') as f:
    items = f.read()
    print(p1(items))
    print(p2(items))
