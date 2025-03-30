'''Advent of Code Year 2022 Day 5: Supply Stacks'''
from pathlib import Path


script_dir = Path(__file__).parent
file_path = script_dir / 'd5.txt'

stacks = [
   ['W', 'D', 'G', 'B', 'H', 'R', 'V'],
   ['J', 'N', 'G', 'C', 'R', 'F'],
   ['L', 'S', 'F', 'H', 'D', 'N', 'J'],
   ['J', 'D', 'S', 'V'],
   ['S', 'H', 'D', 'R', 'Q', 'W', 'N', 'V'],
   ['P', 'G', 'H', 'C', 'M'],
   ['F', 'J', 'B', 'G', 'L', 'Z', 'H', 'C'],
   ['S', 'J', 'R'],
   ['L', 'G', 'S', 'R', 'B', 'N', 'V', 'M']
]

def parse_line(line):
    args = line.strip().split()
    if len(args) >= 6 and args[0] == 'move':
        num_stacks = int(args[1])
        source = int(args[3]) - 1
        dest = int(args[-1]) - 1
        return num_stacks, source, dest
    return None


def move_stacks(stacks, num_stacks, source, dest, part_two= False):
    
    if part_two:
        if stacks[source]:
            # moving_boxes = stacks[source][: num_stacks]
            moving_boxes = stacks[source][-num_stacks: ]
            del stacks[source][-num_stacks: ] 
            # stacks[dest] = moving_boxes + stacks[dest]
            stacks[dest].extend(moving_boxes)
    else: 
        for _ in range(num_stacks):
            if stacks[source]:
                box = stacks[source].pop()
                stacks[dest].append(box)
    
    return

with open(file_path, 'r') as f: 
    for line in f: 
        parsed = parse_line(line)
        if parsed: 
            num_stacks, source, dest = parse_line(line)
            move_stacks(stacks, num_stacks, source, dest, part_two= True)

def return_answer(stacks):
    ans = []
    for stack in stacks:
        if stack: 
            ans.append(stack[-1])
        else:
            ans.append(' ')
    
    return ''.join(ans)

print(return_answer(stacks))