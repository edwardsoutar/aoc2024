import os
from collections import Counter

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

def calculate_similarity_score(list_1, list_2):
    list_1_unique_values = set(list_1)
    list_2_frequencies = Counter(list_2)

    similarity_score = 0

    for value in list_1_unique_values:
        similarity_score += value * list_2_frequencies[value]

    return similarity_score

list_1, list_2 = parse_input()
print(calculate_similarity_score(list_1, list_2))



