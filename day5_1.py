"Advent of Code 2023 Day 5-1"

def main():
    "Main function"

    lines = open('day5-input.txt', 'r', encoding='utf-8').readlines()
    lines = [line.strip() for line in lines]

    seeds = []
    # Lists containing elements [destination range start, source range start, range length]
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []

    # Order of lists for the seed to location process
    maps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light,
            light_to_temperature, temperature_to_humidity, humidity_to_location]
    locations = []

    def create_lists():
        "Creates lists from the input text"

        current_array = []
        for line in lines:
            if 'seeds' in line.lower():
                nonlocal seeds
                seeds = line.split(': ')[1].split()
            elif 'seed-to-soil map' in line.lower():
                current_array = seed_to_soil
            elif 'soil-to-fertilizer map' in line.lower():
                current_array = soil_to_fertilizer
            elif 'fertilizer-to-water map' in line.lower():
                current_array = fertilizer_to_water
            elif 'water-to-light' in line.lower():
                current_array = water_to_light
            elif 'light-to-temperature' in line.lower():
                current_array = light_to_temperature
            elif 'temperature-to-humidity' in line.lower():
                current_array = temperature_to_humidity
            elif 'humidity-to-location' in line.lower():
                current_array = humidity_to_location
            elif line != '':
                values = line.split()
                current_array.append(values)

    def find_locations():
        "Finds seed locations and inserts them into locations list"

        for seed in seeds:
            location = find_destination(int(seed), seed_to_soil)
            locations.append(location)

    def find_destination(source, process_map):
        "Finds destination of source based on processing map"

        destination = source
        map_index = maps.index(process_map)
        for values in process_map:
            destination_start = int(values[0])
            source_start = int(values[1])
            length = int(values[2])

            if source in range(source_start, source_start + length):
                destination = source + (destination_start - source_start)
                break

        if map_index < len(maps) - 1:
            return find_destination(destination, maps[map_index + 1])

        return destination

    create_lists()
    find_locations()

    print(min(locations))

main()
