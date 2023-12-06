"Advent of Code 2023 Day 3-1"

def main():
    "Main function"

    lines = open('day3-input.txt', 'r', encoding='utf-8').readlines()
    lines = [line.strip() for line in lines]
    map_2d = [list(line) for line in lines]

    valid_numbers = []

    def find_number():
        "Numbers can be 1-3 digits long"

        number = char
        for i in range(1, 3):
            if x + i <= len(row) - 1 and row[x + i].isdigit():
                number += row[x + i]
            else:
                break
        return int(number)

    def validate_number():
        if ((x + 1 <= len(row) - 1 and not row[x + 1].isdigit() and row[x + 1] != '.')
            or (x - 1 >= 0 and not row[x - 1].isdigit() and row[x - 1] != '.')
            or (not map_2d[y - 1][x].isdigit() and map_2d[y - 1][x] != '.')
            or (y + 1 <= len(map_2d) - 1 and
                not map_2d[y + 1][x].isdigit() and map_2d[y + 1][x] != '.')
            or (not map_2d[y - 1][x - 1].isdigit() and map_2d[y - 1][x - 1] != '.')
            or (x + 1 <= len(row) - 1 and
                not map_2d[y - 1][x + 1].isdigit() and map_2d[y - 1][x + 1] != '.')
            or (y + 1 <= len(map_2d) - 1 and
                not map_2d[y + 1][x - 1].isdigit() and map_2d[y + 1][x - 1] != '.')
            or (y + 1 <= len(map_2d) - 1 and x + 1 <= len(row) - 1 and
                not map_2d[y + 1][x + 1].isdigit() and map_2d[y + 1][x + 1] != '.')
        ):
            valid_numbers.append(number)
            return True
        return False

    number = 0
    validated = False
    for y, row in enumerate(map_2d):
        for x, char in enumerate(row):
            if char.isdigit():
                # Find the whole number of first digit
                if x - 1 < 0 or not row[x - 1].isdigit():
                    number = find_number()
                # Check if valid number
                if not validated:
                    validated = validate_number()
            else:
                validated = False

    print(sum(valid_numbers))

main()
