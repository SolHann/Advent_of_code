# Returns a list of the sums of ints split by an empty line(/n/n)
def sum_groups(input):
    ints = input.read().split("\n")

    sum = 0
    sum_l = []
    for x in ints:
        if x == '':  # Since we have already split by /n x = '' indicates an empty line
            sum_l.append(sum)
            sum = 0
            continue
        sum += int(x)
    return sum_l


# Return the three largest ints in a list
def three_largest(list):
    big_three = []
    for i in range(3):
        x = max(list)
        big_three.append(x)
        list.remove(x)

    return big_three


if __name__ == '__main__':
    input = open('input.txt')
    sum_l = sum_groups(input)
    print(max(sum_l))

    big_three = three_largest(sum_l)
    print(sum(big_three))
