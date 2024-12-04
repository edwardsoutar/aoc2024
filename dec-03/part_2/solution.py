import os
import re

def calculate_multiplication(string):
    pattern = "mul\((\d{1,3}),(\d{1,3})\)"
    match = re.match(pattern, string).groups()

    return int(match[0]) * int(match[1])

def get_sum_of_multiplications():
    dir = os.path.dirname(__file__)
    file = open(os.path.join(dir,'input.txt'), "r")

    pattern = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, file.read())

    file.close()

    sum_value = 0

    enabled = True

    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            sum_value += calculate_multiplication(match)

    return sum_value

print(get_sum_of_multiplications())