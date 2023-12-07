
import re
with open('day5input.txt', 'r') as file:
    puzzle_input = file.readlines()


result = []
temp_list = []

for item in puzzle_input:
    if item == '\n':
        result.append(temp_list)
        temp_list = []
    else:
        temp_list.append(item.strip())

result.append(temp_list)


seed_map_dict = {}

seed_map_dict['seeds'] = [int(n) for n in re.findall(r'\d+', result[0][0])]
seed_map_dict['seed_to_soil_map'] = [list(map(int, re.findall(r'\d+', m)))
                                     for m in result[1][1:]]
seed_map_dict['soil_to_fertilizer_map'] = [list(map(int, re.findall(r'\d+', m)))
                                           for m in result[2][1:]]
seed_map_dict['fertilizer_to_water_map'] = [list(map(int, re.findall(r'\d+', m)))
                                            for m in result[3][1:]]
seed_map_dict['water_to_light_map'] = [list(map(int, re.findall(r'\d+', m)))
                                       for m in result[4][1:]]
seed_map_dict['light_to_temperature_map'] = [list(map(int, re.findall(r'\d+', m)))
                                             for m in result[5][1:]]
seed_map_dict['temperature_to_humidity_map'] = [list(map(int, re.findall(r'\d+', m)))
                                                for m in result[6][1:]]
seed_map_dict['humidity_to_location'] = [list(map(int, re.findall(r'\d+', m)))
                                         for m in result[7][1:]]


def get_mappings(seeds: list, dest_range_start,  source_range_start, range_length):
    source_range = list(
        range(source_range_start, source_range_start + range_length))
    dest_range = list(range(dest_range_start, dest_range_start + range_length))

    mapped_seeds = list(zip(source_range, dest_range))

    print("seeds: ", seeds)

    for seed in seeds:
        if seed not in [s[0] for s in mapped_seeds]:
            mapped_seeds.append((seed, seed))

    return [s for s in mapped_seeds if s[0] in seeds]


print(seed_map_dict)

print(get_mappings(seed_map_dict['seeds'], 52, 50, 48))

seed_2_soil_maps = [[50, 98, 2], [52, 50, 48]]

for m in seed_2_soil_maps:
    all_maps = []
    all_maps.extend(get_mappings(seed_map_dict['seeds'], m[0], m[1], m[2]))

print(all_maps)
