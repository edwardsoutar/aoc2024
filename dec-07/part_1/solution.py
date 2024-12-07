import os
from collections import deque

def parse_input():
    dir = os.path.dirname(__file__)

    file = open(os.path.join(dir,'input.txt'), "r")

    equations = []

    for line in file:
        numbers = line.split(" ")

        equations.append([int(numbers[0][:-1]), [int(number) for number in numbers[1:]]])
            
    file.close()

    return equations

def check_equation_is_valid(equation):
    target = equation[0]
    components = equation[1]

    values = deque()
    values.append(components[0])
    
    for value in components[1:]:
        for _ in range(len(values)):
            base = values.popleft()

            values.append(base * value)
            values.append(base + value)
            values.append(int(str(base) + str(value)))
    
    return target in values

def get_valid_equations(equations):
    total = 0
    for equation in equations:
        if check_equation_is_valid(equation):
            total += equation[0]

    return total

equations = parse_input()

print(get_valid_equations(equations))