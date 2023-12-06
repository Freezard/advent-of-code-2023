"Advent of Code 2023 Day 4-2"

def main():
    "Main function"

    lines = open('day4-input.txt', 'r', encoding='utf-8').readlines()
    lines = [line.strip() for line in lines]

    all_card_copies = {}
    total_cards = 0

    for line_index, line in enumerate(lines):
        numbers = line.split(': ')[1].split(' | ')
        winning_numbers = numbers[0].split()
        player_numbers = numbers[1].split()
        card_number = line_index + 1
        card_matches = 0
        card_copies = all_card_copies[card_number] if card_number in all_card_copies else 0

        for number in player_numbers:
            if number in winning_numbers:
                card_matches += 1
                # Add new card copies based on copies of current card
                card_copy_number = card_number + card_matches
                if card_copy_number not in all_card_copies:
                    all_card_copies[card_copy_number] = 1 + card_copies
                else:
                    all_card_copies[card_copy_number] += 1 + card_copies

        total_cards += 1 + card_copies

    print(total_cards)

main()
