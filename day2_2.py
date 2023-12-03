"Advent of Code 2023 Day 2-2"

import math

def main():
    "Main function"

    sum_set_powers = 0

    lines = open('day2-input.txt', 'r', encoding='utf-8').readlines()
    lines = [line.strip() for line in lines]

    for line in lines:
        minimum_cubes = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        cubes = line.split(': ')[1]
        cube_grabs = cubes.split('; ')
        for cube in cube_grabs:
            cube_grab = cube.split(', ')
            for cube in cube_grab:
                cube_info = cube.split()
                amount = int(cube_info[0])
                color = cube_info[1]

                if amount > minimum_cubes[color]:
                    minimum_cubes[color] = amount
        sum_set_powers += math.prod(minimum_cubes.values())

    print(sum_set_powers)

main()
