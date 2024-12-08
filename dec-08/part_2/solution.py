import os
from collections import defaultdict

def parse_input():
    dir = os.path.dirname(__file__)

    file = open(os.path.join(dir,'input.txt'), "r")

    grid = []

    for line in file:
        grid.append([char for char in line.rstrip()])
            
    file.close()

    return grid

def get_antennae(grid):
    rows, columns = len(grid), len(grid[0])

    antennae = defaultdict(list)

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == '.':
                continue

            antenna = grid[row][column]

            antennae[antenna].append((row, column))

    return antennae

def is_in_bounds(antinode, rows, columns):
    return 0 <= antinode[0] < rows and 0 <= antinode[1] < columns

def get_antinodes_coordinates(antenna_1, antenna_2, rows, columns):
    row_displacement = antenna_1[0] - antenna_2[0]
    column_displacement = antenna_1[1] - antenna_2[1]

    antinodes = set()
    antinodes.add(antenna_1)
    antinodes.add(antenna_2)

    i = 1

    while True:
        antinode = (antenna_1[0] + (row_displacement * i), antenna_1[1] + (column_displacement * i))

        if not is_in_bounds(antinode, rows, columns):
            break

        antinodes.add(antinode)
        i += 1

    i = 1

    while True:
        antinode = (antenna_2[0] - (row_displacement * i), antenna_2[1] - (column_displacement * i))

        if not is_in_bounds(antinode, rows, columns):
            break

        antinodes.add(antinode)
        i += 1

    return antinodes

def get_antinodes(grid, antennae):
    rows, columns = len(grid), len(grid[0])

    antinodes = set()

    for antenna_locations in antennae.values():
        for i in range(len(antenna_locations)):
            for j in range(i + 1, len(antenna_locations)):
                antinodes = antinodes.union(get_antinodes_coordinates(antenna_locations[i], antenna_locations[j], rows, columns))

    return antinodes

grid = parse_input()
antennae = get_antennae(grid)

print(len(get_antinodes(grid, antennae)))