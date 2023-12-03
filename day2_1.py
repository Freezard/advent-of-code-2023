"Advent of Code 2023 Day 2-1"

def main():
    "Main function"

    total_cubes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    sum_valid_ids = 0

    lines = open('day2-input.txt', 'r', encoding='utf-8').readlines()
    lines = [line.strip() for line in lines]

    for line_index, line in enumerate(lines):
        game_id = line_index + 1
        cubes = line.split(': ')[1]
        cube_grabs = cubes.split('; ')
        valid_cube_grabs = True
        for cube in cube_grabs:
            cube_grab = cube.split(', ')
            for cube in cube_grab:
                cube_info = cube.split()
                amount = int(cube_info[0])
                color = cube_info[1]

                if amount > total_cubes[color]:
                    valid_cube_grabs = False
                    break
            if not valid_cube_grabs:
                break
        if valid_cube_grabs:
            sum_valid_ids += game_id

    print(sum_valid_ids)

main()
