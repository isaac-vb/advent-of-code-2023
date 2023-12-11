from itertools import cycle
import re
import math
with open('day8input.txt', 'r') as file:
    puzzle_input = [line for line in file.read().split('\n') if line != '']

# The L/R instructions
instructions = puzzle_input[0]


# Convert info from puzzle input with this structure
# {'AAA' :['BBB', 'BBB'], 'BBB' : ['AAA', 'ZZZ'] , ....}
node_dict = {}
for node in puzzle_input[1:]:
    node_info = re.findall(r'[A-Z]+', node)
    node_dict[node_info[0]] = [node_info[1], node_info[2]]

# Use cycle so the instructions are repeated ("LR" becomes "LRLRLRLR....")
instructions_cycle = cycle(instructions)


# Set up the starting node
current_node = "AAA"

count = 0
while current_node != "ZZZ":
    current_instruction = next(instructions_cycle)

    if current_instruction == "L":
        current_node = node_dict[current_node][0]

    elif current_instruction == "R":
        current_node = node_dict[current_node][1]

    count += 1


print(f"Part 1 Answer: {count}")


# Part 2

# Starting nodes
a_nodes = list(k for k in node_dict.keys() if k.endswith("A"))
# Target/end nodes
z_nodes = list(k for k in node_dict.keys() if k.endswith("Z"))


path_length_list = []

for n in a_nodes:
    current_node = n

    count = 0
    while current_node not in z_nodes:
        current_instruction = next(instructions_cycle)

        if current_instruction == "L":
            current_node = node_dict[current_node][0]

        elif current_instruction == "R":
            current_node = node_dict[current_node][1]

        count += 1

    path_length_list.append(count)

# Find LCM of the paths to see where they overlap
print(f"Part 2 Answer: {math.lcm(*path_length_list)}")
