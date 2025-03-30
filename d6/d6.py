'''AOC 2022 Day 7 - No Space left on Device'''

from pathlib import Path
from collections import defaultdict 

script_dir = Path(__file__).parent
file_path = script_dir / 'd6_test.txt'
directory = {'/': {}}
current_path = []

with open(file_path, 'r') as f: 
    for line in f:
        params = line.strip().split()
        if params[0] == '$': #command case
            if params[1] == 'cd':
                if params[1] == '/': #Go to Root
                    current_path = ['/']
                elif params[1] == '..':
                    if len(current_path) > 1:
                        current_path.pop()
                else:
                    current_path.append(params[2])
                # if params[2] not in directory:
                #     directory[params[2]] = {}
                # current_directory = params[2]
        else: #case where files are being enumerated
            
            current_dir = directory
            for dir_name in current_path:
                current_dir = current_dir[dir_name]
            
            if params[0] == 'dir':
                if params[1] not in current_dir: 
                    current_dir[params[1]] = {}
            else:
                size, file_name = int(params[0]), params[1]
                current_dir[file_name] = size
                
