def p1(input):
    sum = 0
    for card in input:
        point = 0

        player_nums, winning_no = card.split(":")[1].split("|")
        player_nums = player_nums.split()
        winning_no = winning_no.split()

        for i in player_nums:
            if i in winning_no:
                point = 1 if point == 0 else point * 2
        sum += point
    return sum


def p2(input):
    counter = 0
    multiplier = [1]*10

    for card in input:
        point = 0

        player_nums, winning_no = card.split(":")[1].split("|")
        player_nums = player_nums.split()
        winning_no = winning_no.split()

        for i in player_nums:
            if i in winning_no:
                point += 1

        multi = multiplier.pop(0)
        multiplier.append(1)

        for i in range(point):
            multiplier[i] += multi

        counter += multi
    return counter


with open('input.txt', 'r') as f:
    items = [line.strip() for line in f]
    print(p1(items), '\n')
    print(p2(items))
