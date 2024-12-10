import os
from collections import deque

def parse_input():
    dir = os.path.dirname(__file__)

    file = open(os.path.join(dir,'input.txt'), "r")

    map = []

    for line in file:
        map.append([int(char) if char.isnumeric() else char for char in line.rstrip()])

    file.close()

    return map

def get_trailhead_score(i, j, map):
    queue = deque()
    queue.append((i, j))

    results = set()

    while queue:
        (value_i, value_j) = queue.popleft()

        if map[value_i][value_j] == 9:
            results.add((value_i, value_j))
            continue

        if value_i > 0 and map[value_i - 1][value_j] == map[value_i][value_j] + 1:
            queue.append((value_i - 1, value_j))
        if value_i < len(map) - 1 and map[value_i + 1][value_j] == map[value_i][value_j] + 1:
            queue.append((value_i + 1, value_j))
        if value_j > 0 and map[value_i][value_j - 1] == map[value_i][value_j] + 1:
            queue.append((value_i, value_j - 1))
        if value_j < len(map[value_i]) - 1 and map[value_i][value_j + 1] == map[value_i][value_j] + 1:
            queue.append((value_i, value_j + 1))

    return len(results)

def get_total_trailhead_scores(map):
    total = 0

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                total += get_trailhead_score(i, j, map)

    return total

map = parse_input()
print(get_total_trailhead_scores(map))