def calculate_points_v1(cards):
    """Calculates and returns the total points for version 1 algorithm.

    Args:
        cards (list): List of card strings in the format "player:numbers|winning_numbers".

    Returns:
        int: Total points calculated.
    """
    total_points = 0
    for card in cards:
        points = 0

        # Splitting the card string to extract player and winning numbers
        _, card_data = card.split(":")
        player_numbers, winning_numbers = card_data.split("|")
        player_numbers = player_numbers.split()
        winning_numbers = winning_numbers.split()

        # Calculate points based on matching numbers
        for number in player_numbers:
            if number in winning_numbers:
                points = 1 if points == 0 else points * 2
        total_points += points
    return total_points


def calculate_points_v2(cards):
    """Calculates and returns the total points for version 2 algorithm.

    Args:
        cards (list): List of card strings in the format "player:numbers|winning_numbers".

    Returns:
        int: Total points calculated.
    """
    total_points = 0
    win_multiplier = [1] * 10  # Initialize multiplier queue

    for card in cards:
        # Splitting the card string to extract player and winning numbers
        _, card_data = card.split(":")
        player_numbers, winning_numbers = card_data.split("|")
        player_numbers = player_numbers.split()
        winning_numbers = winning_numbers.split()

        # Count number of wins and update multipliers accordingly
        wins_count = sum(number in winning_numbers for number in player_numbers)
        multiplier = win_multiplier.pop(0)
        win_multiplier.append(1)

        for i in range(wins_count):
            win_multiplier[i] += multiplier

        total_points += multiplier
    return total_points


def read_cards_from_file(file_path):
    """Reads card data from a file.

    Args:
        file_path (str): Path to the file containing card data.

    Returns:
        list: List of card strings read from the file.
    """
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
