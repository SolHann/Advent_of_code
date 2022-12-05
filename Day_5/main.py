def stack(input):
    stacks = [[],[],[],[],[],[],[],[],[]]
    for i in range(8):
        for j in range(1, len(input[i]),4):
            if input[i][j].isalpha():
                stacks[int((j-1)/4)].insert(0,(input[i][j]))
    return stacks

def p1(input):
    stacks = stack(input)
    for line in input[10:]:
        l = line.split(' ')
        l = [int(x) for x in l if x.isnumeric()]
        print(stacks)
        temp = (stacks[l[1]-1])[-l[0]:]
        del (stacks[l[1]-1])[-l[0]:]
        stacks[l[2]-1].extend(temp)
    return [i[-1] for i in stacks]


def p2(input):
    stacks = stack(input)
    for line in input[10:]:
        l = line.split(' ')
        l = [int(x) for x in l if x.isnumeric()]

        for x in range(l[0]):
            temp = stacks[(l[1]-1)]
            stacks[l[2]-1].append(temp)

    return [i[-1] for i in stacks]


with open('input.txt', 'r') as f:
    items = [line.replace("\n", "") for line in f]
    print(p1(items))
    print(p2(items))
