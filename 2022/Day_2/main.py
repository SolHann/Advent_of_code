# Calculates a score based on who wins a game of rock paper scissor
def rock_paper_scissor(input):
    sum = 0

    for l in input:
        round = l.strip().split(" ")

        player = round[1]
        opponent = round[0]

        if player == "X":  # Lose
            if opponent == "A":
                sum += 3
            elif opponent == "B":
                sum += 1
            else:
                sum += 2
        if player == "Y":  # Draw
            if opponent == "A":
                sum += 4
            elif opponent == "B":
                sum += 5
            else:
                sum += 6
        if player == "Z":  # Win
            if opponent == "A":
                sum += 8
            elif opponent == "B":
                sum += 9
            else:
                sum += 7
    return sum


if __name__ == '__main__':
    with open('input.txt') as f:
        print(rock_paper_scissor(f))

