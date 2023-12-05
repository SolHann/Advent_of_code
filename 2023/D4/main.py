def calculate_points_v1(cards):
    total_points = 0
    for card in cards:
        points = 0

        _, card_data = card.split(":")
        player_numbers, winning_numbers = card_data.split("|")
        player_numbers = player_numbers.split()
        winning_numbers = winning_numbers.split()

        for number in player_numbers:
            if number in winning_numbers:
                points = 1 if points == 0 else points * 2
        total_points += points
    return total_points


def calculate_points_v2(cards):
    total_points = 0
    win_multiplier = [1] * 10

    for card in cards:
        _, card_data = card.split(":")
        player_numbers, winning_numbers = card_data.split("|")
        player_numbers = player_numbers.split()
        winning_numbers = winning_numbers.split()

        wins_count = sum(number in winning_numbers for number in player_numbers)
        multiplier = win_multiplier.pop(0)
        win_multiplier.append(1)

        for i in range(wins_count):
            win_multiplier[i] += multiplier

        total_points += multiplier
    return total_points


def read_cards_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]
    except IOError as e:
        print(f"Error reading file: {e}")
        return []


# Main execution
cards = read_cards_from_file('input.txt')
print(calculate_points_v1(cards), '\n')
print(calculate_points_v2(cards))