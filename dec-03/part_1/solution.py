import os
import re

def calculate_multiplication(values):
    return int(values[0]) * int(values[1])

def get_sum_of_multiplications():
    dir = os.path.dirname(__file__)
    file = open(os.path.join(dir,'input.txt'), "r")

    pattern = "mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, file.read())

    sum_value = 0

    for match in matches:
        sum_value += calculate_multiplication(match)

    return sum_value

print(get_sum_of_multiplications())