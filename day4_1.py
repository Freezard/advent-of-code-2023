"Advent of Code 2023 Day 4-1"

def main():
    "Main function"

    lines = open('day4-input.txt', 'r', encoding='utf-8').readlines()
    lines = [line.strip() for line in lines]

    total_points = 0

    for line in lines:
        numbers = line.split(': ')[1].split(' | ')
        winning_numbers = numbers[0].split()
        player_numbers = numbers[1].split()
        card_points = 0

        for number in player_numbers:
            if number in winning_numbers:
                if card_points == 0:
                    card_points += 1
                else:
                    card_points *= 2

        total_points += card_points


    print(total_points)

main()
