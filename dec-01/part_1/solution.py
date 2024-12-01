import os

def parse_input():
    list_1 = []
    list_2 = []

    dir = os.path.dirname(__file__)

    file = open(os.path.join(dir,'input.txt'), "r")

    for line in file:
        items = line.split()

        list_1.append(int(items[0]))
        list_2.append(int(items[1]))

    return list_1, list_2

def sum_differences(list_1, list_2):
    sum_val = 0

    for i in range(len(list_1)):
        sum_val += abs(list_1[i] - list_2[i])

    return sum_val

list_1, list_2 = parse_input()

list_1.sort()
list_2.sort()

print(sum_differences(list_1, list_2))