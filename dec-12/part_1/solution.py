import os
from collections import deque

def parse_input():
    dir = os.path.dirname(__file__)

    file = open(os.path.join(dir,'input.txt'), "r")

    arrangement = []

    for line in file:
        arrangement.append([char for char in line.rstrip()])

    file.close()

    return arrangement

def calculate_price(arrangement):
    seen = set()

    rows, columns = len(arrangement), len(arrangement[0])

    def calculate_price_of_plot(row, column):
        queue = deque()
        queue.append((row, column))

        area = 0
        perimeter = 0

        while queue:
            (r, c) = queue.popleft()

            if (r, c) in seen:
                continue

            plant = arrangement[r][c]

            seen.add((r, c))
            area += 1

            if r == 0 or (r > 0 and arrangement[r - 1][c] != plant):
                perimeter += 1
            else:
                queue.append((r - 1, c))

            if r == rows - 1 or (r < rows - 1 and arrangement[r + 1][c] != plant):
                perimeter += 1
            else:
                queue.append((r + 1, c))

            if c == 0 or (c > 0 and arrangement[r][c - 1] != plant):
                perimeter += 1
            else:
                queue.append((r, c - 1))

            if c == columns - 1 or (c < columns - 1 and arrangement[r][c + 1] != plant):
                perimeter += 1
            else:
                queue.append((r, c + 1))

        return area * perimeter
    
    total_price = 0

    for row in range(rows):
        for column in range(columns):
            total_price += calculate_price_of_plot(row, column)

    return total_price

arrangement = parse_input()
print(calculate_price(arrangement))