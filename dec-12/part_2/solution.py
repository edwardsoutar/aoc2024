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

def calculate_price(arrangement):
    seen = set()

    rows, columns = len(arrangement), len(arrangement[0])

    def calculate_price_of_plot(row, column):
        queue = deque()
        queue.append((row, column))

        area = 0
        horizontal_sides = defaultdict(list)
        vertical_sides = defaultdict(list)

        while queue:
            (r, c) = queue.popleft()

            if (r, c) in seen:
                continue

            plant = arrangement[r][c]

            seen.add((r, c))
            area += 1

            if r == 0 or (r > 0 and arrangement[r - 1][c] != plant):
                if r - 1 in horizontal_sides:
                    for side in horizontal_sides[r - 1]:
                        if side[0] - 1 == c:
                            side[0] -= 1
                            break
                        elif side[1] + 1 == c:
                            side[1] += 1
                            break
                        elif side[0] <= c <= side[1]:
                            break
                    else:
                        horizontal_sides[r - 1].append([c, c])
                else:
                    horizontal_sides[r - 1].append([c, c])
                
            else:
                queue.append((r - 1, c))

            if r == rows - 1 or (r < rows - 1 and arrangement[r + 1][c] != plant):
                if r + 1 in horizontal_sides:
                    for side in horizontal_sides[r + 1]:
                        if side[0] - 1 == c:
                            side[0] -= 1
                            break
                        elif side[1] + 1 == c:
                            side[1] += 1
                            break
                        elif side[0] <= c <= side[1]:
                            break
                    else:
                        horizontal_sides[r + 1].append([c, c])
                else:
                    horizontal_sides[r + 1].append([c, c])

            else:
                queue.append((r + 1, c))

            if c == 0 or (c > 0 and arrangement[r][c - 1] != plant):
                if c - 1 in vertical_sides:
                    for side in vertical_sides[c - 1]:
                        if side[0] - 1 == r:
                            side[0] -= 1
                            break
                        elif side[1] + 1 == r:
                            side[1] += 1
                            break
                        elif side[0] <= r <= side[1]:
                            break
                    else:
                        vertical_sides[c - 1].append([r, r])
                else:
                    vertical_sides[c - 1].append([r, r])
            else:
                queue.append((r, c - 1))

            if c == columns - 1 or (c < columns - 1 and arrangement[r][c + 1] != plant):
                if c + 1 in vertical_sides:
                    for side in vertical_sides[c + 1]:
                        if side[0] - 1 == r:
                            side[0] -= 1
                            break
                        elif side[1] + 1 == r:
                            side[1] += 1
                            break
                        elif side[0] <= r <= side[1]:
                            break
                    else:
                        vertical_sides[c + 1].append([r, r])
                else:
                    vertical_sides[c + 1].append([r, r])
            else:
                queue.append((r, c + 1))

        print(arrangement[row][column], vertical_sides.values(), horizontal_sides.values())

        return area * (len(vertical_sides.values()) + len(horizontal_sides.values()))
    
    total_price = 0

    for row in range(rows):
        for column in range(columns):
            total_price += calculate_price_of_plot(row, column)

    return total_price

arrangement = parse_input()
print(calculate_price(arrangement))