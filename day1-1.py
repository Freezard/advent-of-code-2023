"""Advent of Code 2023 Day 1-1"""

import re

def main():
    lines = open('day1-input.txt', 'r').readlines()
    stripped_lines = [re.sub(r'\D', '', line) for line in lines]

    calibration_values = []
    for line in stripped_lines:
        calibration_values.append([line[0], line[len(line)-1]])

    total_sum = 0
    for values in calibration_values:
        total_sum += int(values[0] + values[1])

    print(total_sum)

main()
