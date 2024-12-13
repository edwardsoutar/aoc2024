import os
from collections import deque, defaultdict

def parse_input():
    dir = os.path.dirname(__file__)

    file = open(os.path.join(dir,'input.txt'), "r")

    arrangement = []

    for line in file:
        arrangement.append([char for char in line.rstrip()])

    file.close()

    return arrangement

def count_sides(edges):
    sides = 0

    for edge in edges.values():
        sides += 1

        edge.sort()

        for i in range(1, len(edge)):
            if abs(edge[i] - edge[i - 1]) != 1:
                sides += 1

    return sides

def calculate_price(arrangement):
    seen = set()

    rows, columns = len(arrangement), len(arrangement[0])

    def calculate_price_of_plot(row, column):
        queue = deque()
        queue.append((row, column))

        area = 0
        edges = defaultdict(list)

        while queue:
            (r, c) = queue.popleft()

            if (r, c) in seen:
                continue

            plant = arrangement[r][c]

            seen.add((r, c))
            area += 1

            if r == 0 or (r > 0 and arrangement[r - 1][c] != plant):
                edges[r, (0, -1)].append(c)
            else:
                queue.append((r - 1, c))

            if r == rows - 1 or (r < rows - 1 and arrangement[r + 1][c] != plant):
                edges[r, (0, 1)].append(c)
            else:
                queue.append((r + 1, c))

            if c == 0 or (c > 0 and arrangement[r][c - 1] != plant):
                edges[c, (-1, 0)].append(r)
            else:
                queue.append((r, c - 1))

            if c == columns - 1 or (c < columns - 1 and arrangement[r][c + 1] != plant):
                edges[c, (1, 0)].append(r)
            else:
                queue.append((r, c + 1))

        return area * count_sides(edges)
    
    total_price = 0

    for row in range(rows):
        for column in range(columns):
            total_price += calculate_price_of_plot(row, column)

    return total_price

arrangement = parse_input()
print(calculate_price(arrangement))