'''Advent of Code 2022 - Day 10 Cathode-Ray Tube'''

from pathlib import Path
from collections import Counter

script_dir = Path(__file__).parent
file_path = script_dir / 'd10.txt'

class Clock:
    def __init__(self, file_path):
        with open(file_path, 'r') as f: 
            self.instructions = f.readlines()
        
        self.x = 1
        self.cycle = 0
        self.cycles = []
        self.add_vals = []
        self.target_signals = []
    
    def process_instruction(self):
        if self.cycle in (20, 600, 100, 140, 180, 220):
            self.target_signals.append(self.x * self.cycle)
        
        instruction = self.instructions.pop(0).strip().split()
        if instruction[0] == 'addx':
            self.add_vals.append(int(instruction[1]))
            self.cycles.append(2)
        
        if self.cycles:
            for cycle in self.cycles:
                if cycle == 0:
                    self.x += self.add_vals.pop(0)
            
        self.cycle += 1 
            
        
    
    
        
