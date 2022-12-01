input1 = open('input.txt')


def max_of_sum():
    ints = input1.read().split("\n")

    sum = 0
    sum_l = []
    for x in ints:
        if x == '':
            sum_l.append(sum)
            sum = 0
            continue
        sum += int(x)
    return max(sum_l)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(max_of_sum())
