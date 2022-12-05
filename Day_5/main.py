def stack(input):
    stacks = [[], [], [], [], [], [], [], [], []]

    for line in range(8):
        for j in range(1, len(input[line]), 4):  # There is a potential 'crate' every 4 spaces
            # Check if there is a letter, if there is add it to one of the 9 lists
            if input[line][j].isalpha():
                stacks[int((j - 1) / 4)].insert(0, (input[line][j]))
    return stacks


def p1(input):
    stacks = stack(input)
    for line in input[10:]:
        moves = line.split(' ')
        moves = [int(x) for x in moves if x.isnumeric()]

        for x in range(moves[0]):
            stacks[moves[2] - 1].append((stacks[moves[1]-1]).pop())

    return [i[-1] for i in stacks]


def p2(input):
    stacks = stack(input)
    for line in input[10:]:
        # Create a list of each int in the instructions
        line = line.split(' ')
        line = [int(x) for x in line if x.isnumeric()]

        stacks[line[2] - 1].extend((stacks[line[1] - 1])[-line[0]:])
        del (stacks[line[1] - 1])[-line[0]:]


    return [i[-1] for i in stacks]


with open('input.txt', 'r') as f:
    items = [line.replace("\n", "") for line in f]
    print(p1(items))
    print(p2(items))
