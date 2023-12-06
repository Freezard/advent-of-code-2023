"Advent of Code 2023 Day 3-2"

def main():
    "Main function"

    lines = open('day3-input.txt', 'r', encoding='utf-8').readlines()
    lines = [line.strip() for line in lines]
    map_2d = [list(line) for line in lines]

    number = 0
    number_id = 0

    all_gears = {}
    valid_gears = {}
    total_sum = 0

    def find_number():
        "Numbers can be 1-3 digits long"
        nonlocal number_id

        number = char
        for i in range(1, 3):
            if x + i <= len(row) - 1 and row[x + i].isdigit():
                number += row[x + i]
            else:
                break
        number_id += 1
        return int(number)

    def find_gears():
        gears = []
        if x + 1 <= len(row) - 1 and row[x + 1] == '*':
            gears.append((x + 1, y))
        if x - 1 >= 0 and row[x - 1] == '*':
            gears.append((x - 1, y))
        if map_2d[y - 1][x] == '*':
            gears.append((x, y - 1))
        if y + 1 <= len(map_2d) - 1 and map_2d[y + 1][x] == '*':
            gears.append((x, y + 1))
        if map_2d[y - 1][x - 1] == '*':
            gears.append((x - 1, y - 1))
        if x + 1 <= len(row) - 1 and map_2d[y - 1][x + 1] == '*':
            gears.append((x + 1, y - 1))
        if y + 1 <= len(map_2d) - 1 and map_2d[y + 1][x - 1] == '*':
            gears.append((x - 1, y + 1))
        if y + 1 <= len(map_2d) - 1 and x + 1 <= len(row) - 1 and map_2d[y + 1][x + 1] == '*':
            gears.append((x + 1, y + 1))

        if gears:
            for gear in gears:
                if gear not in all_gears:
                    all_gears[gear] = [[number_id, number]]
                for gear_id, gear_number in all_gears[gear]:
                    if gear_id == number_id:
                        break
                else:
                    all_gears[gear].append([number_id, number])

    for y, row in enumerate(map_2d):
        for x, char in enumerate(row):
            if char.isdigit():
                # Find the whole number of first digit
                if x - 1 < 0 or not row[x - 1].isdigit():
                    number = find_number()
                # Check for gears surrounding the digit
                find_gears()

    # Create a new dict with valid gears only (exactly two nearby numbers)
    for gear, numbers in all_gears.items():
        if len(numbers) == 2:
            valid_gears[gear] = numbers

    # Multiply the numbers and add the product to the total sum
    for numbers in valid_gears.values():
        total_sum += numbers[0][1] * numbers[1][1]

    print(total_sum)

main()
