import os

def parse_input():
    grid = []

    dir = os.path.dirname(__file__)

    file = open(os.path.join(dir,'input.txt'), "r")

    for line in file:
        grid.append(line.rstrip())

    file.close()

    return grid

def count_xmases(grid):
    rows, columns = len(grid), len(grid[0])

    def is_xmas(row, column):
        mappings = {
            'M': 'S',
            'S': 'M'
        }

        if grid[row - 1][column - 1] not in mappings:
            return 0
        elif grid[row - 1][column + 1] not in mappings:
            return 0
        elif grid[row + 1][column + 1] != mappings[grid[row - 1][column - 1]]:
            return 0
        elif grid[row + 1][column - 1] != mappings[grid[row - 1][column + 1]]:
            return 0
        
        return 1

    count = 0

    for row in range(1, rows - 1):
        for column in range(1, columns - 1):
            if grid[row][column] == 'A':
                count += is_xmas(row, column)

    return count

grid = parse_input()
print(count_xmases(grid))

