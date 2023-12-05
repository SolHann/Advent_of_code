import re

def p1(input):
    sum = 0
    for y_pos, line in enumerate(input):
        digit_found = False
        digit_start = 0

        for x_pos, char in enumerate(line):
            # Flags if we find a digit and records the first position
            if char.isdigit() and not digit_found:
                digit_found = True
                digit_start = x_pos

            # If the digit has been found search surround indexes
            elif digit_found and not (char.isdigit()):
                digit_found = False

                above = (input[y_pos-1][digit_start-1: x_pos+1])
                below = (input[y_pos+1][digit_start-1: x_pos+1])
                if (re.search(r'[^\.123456789]', above) is not None
                 or re.search(r'[^\.123456789]', below) is not None
                 or re.search(r'[^\.123456789]', input[y_pos][digit_start-1]) is not None
                 or re.search(r'[^\.123456789]', input[y_pos][x_pos]) is not None):
                    sum += int((input[y_pos][digit_start:x_pos]))
    return sum


def p2(input):
    sum = 0
    for y_pos, line in enumerate(input):
        for x_pos, char in enumerate(line):
            if char == '*':
                first_num = []
                second_num = []
                furthest_position = -1

                for i, c in enumerate(input[y_pos-1][x_pos-1:x_pos+2]):
                    if c.isdigit() and i > furthest_position:
                        first_num.append(c)
                        furthest_position = (x_pos - 1 + i)
                        counter = 0
                        while True:
                            counter += 1
                            if not (input[y_pos-1][(x_pos - 1 + i + counter)]).isdigit():
                                break
                            first_num.append(input[y_pos-1][(x_pos - 1 + i + counter)])
                            furthest_position = (x_pos - 1 + i + counter)

                        counter = 0
                        while True:
                            counter -= 1
                            if not (input[y_pos - 1][(x_pos - 1 + i + counter)]).isdigit():
                                break
                            first_num.insert(0, input[y_pos - 1][(x_pos - 1 + i + counter)])

                        first_num.append(" ")
                        print(first_num)
                furthest_position = -1
                for i, c in enumerate(input[y_pos+1][x_pos-1:x_pos+2]):
                    if c.isdigit() and i > furthest_position:
                        first_num.append(c)
                        furthest_position = (x_pos - 1 + i)
                        counter = 0
                        while True:
                            counter += 1
                            if not (input[y_pos+1][(x_pos - 1 + i + counter)]).isdigit():
                                break
                            first_num.append(input[y_pos+1][(x_pos - 1 + i + counter)])
                            furthest_position = (x_pos - 1 + i + counter)

                        counter = 0
                        while True:
                            counter -= 1
                            if not (input[y_pos + 1][(x_pos - 1 + i + counter)]).isdigit():
                                break
                            first_num.insert(0, input[y_pos + 1][(x_pos - 1 + i + counter)])
                        first_num.append(" ")
                        print(first_num)
                if input[y_pos][x_pos-1].isdigit():
                    first_num.append(input[y_pos][x_pos-1])
                    counter = 0
                    while True:
                        counter -= 1
                        if not (input[y_pos][(x_pos - 1 + counter)]).isdigit():
                            break
                        first_num.insert(0, input[y_pos][(x_pos - 1 + counter)])

                    first_num.append(" ")
                    print(first_num)

                if input[y_pos][x_pos+1].isdigit():
                    first_num.append(input[y_pos][x_pos+1])
                    counter = 0
                    while True:
                        counter += 1
                        if not (input[y_pos][(x_pos + 1 + counter)]).isdigit():
                            break
                        first_num.append(input[y_pos][(x_pos + 1 + counter)])

                    first_num.append(" ")
                    print(first_num)

                product = ''.join(first_num)
                if product.count(' ') == 2:
                    product = product.split(' ')
                    print(int(product[0]) * int(product[1]))
                    sum += (int(product[0]) * int(product[1]))
    return sum


with open('input.txt', 'r') as f:
    items = ['.' + line.strip() + '.' for line in f]
    items.insert(0, '...................................................')
    items.append('.................................................')
    print(p1(items))
    print(p2(items))
