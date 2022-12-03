def p1(input):
    return input


def p2(input):
    return input


with open('input.txt', 'r') as f:
    items = [line.strip() for line in f]
    print(p1(items))
    print(p2(items))
