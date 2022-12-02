
def method(input):
    sum = 0
    for l in input:
        round = l.strip().split(" ")
        player = round[1]
        opponent = round [0]
        if player == 'X':
            sum += 1
        elif player == 'Y':
            sum += 2
        elif player == 'Z':
            sum += 3

        if opponent == "A" and player == "Y" or opponent == "B" and player == "Z" or opponent == "C" and player == "X":
            sum += 6
        elif opponent == "A" and player == "X" or opponent == "B" and player == "Y" or opponent == "C" and player == "Z":
            sum += 3
        elif opponent == "A" and player == "Z" or opponent == "B" and player == "X" or opponent == "C" and player == "Y":
            sum += 0

    return sum


if __name__ == '__main__':
    with open('input.txt') as f:
        print(method(f))
