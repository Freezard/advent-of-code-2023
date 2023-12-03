"""Advent of Code 2023 Day 1-2
   total_sum is off by 20 due to misunderstood instructions"""

import re

def main():
    "Main function"

    lines = open('day1-input.txt', 'r', encoding='utf-8').readlines()

    text_to_numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    def find_first_word(line, line_index):
        lowest_position = -1
        lowest_word = ""
        for word in text_to_numbers:
            pos = line.find(word)
            if pos != -1:
                if lowest_position == -1 or pos < lowest_position:
                    lowest_position = pos
                    lowest_word = word
        if lowest_position != -1:
            lines[line_index] = line.replace(lowest_word, str(text_to_numbers[lowest_word]), 1)
            find_first_word(lines[line_index], line_index)

    for line_index, line in enumerate(lines):
        find_first_word(line, line_index)

    stripped_lines = [re.sub(r'\D', '', line) for line in lines]

    calibration_values = []
    for line in stripped_lines:
        calibration_values.append([line[0], line[len(line)-1]])

    total_sum = 0
    for values in calibration_values:
        total_sum += int(values[0] + values[1])

    print(total_sum)

main()
