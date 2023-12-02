from typing import List

num_strings = {
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

with open("inputs/day1.txt", 'r') as file:
    input = file.read().splitlines()

def part_one(input: List[str]) -> int:
    line_sum = 0
    for line in input:
        first_num = None
        last_num = None
        for char in line:
            if char.isnumeric():
                if first_num == None:
                    first_num = char
                last_num = char
        num = int(first_num + last_num)
        line_sum += num
    return line_sum

def part_two(input: List[str]) -> int:
    line_sum = 0
    for line in input:
        last_num = None
        first_num = get_first_num(line)
        last_num = get_last_num(line)
        num = int(first_num + last_num)
        line_sum += num
    return line_sum

def get_first_num(line: str):
    possible_num_string = ""
    for char in line:
        if char.isnumeric():
            return char
        else:
            possible_num_string += char
            possible_num = string_contains_num(possible_num_string)
            if possible_num:
                return possible_num
            
def get_last_num(line: str):
    possible_num_string = ""
    for char in line[::-1]:
        if char.isnumeric():
            return char
        else:
            possible_num_string = char + possible_num_string
            possible_num = string_contains_num(possible_num_string)
            if possible_num:
                return possible_num

def string_contains_num(s: str) -> str:
    for num_string, num in num_strings.items():
        if num_string in s:
            return str(num)
    return ''

print(part_two(input))