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

    def dfs(row, column, direction):
        word = "XMAS"
        index = 1

        while index < len(word):
            row = row + direction[0]
            column = column + direction[1]

            if row < 0 or row >= rows:
                return 0
            
            if column < 0 or column >= columns:
                return 0

            if grid[row][column] != word[index]:
                return 0
            
            index += 1

        return 1

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    count = 0

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 'X':
                for direction in directions:
                    count += dfs(row, column, direction)

    return count

grid = parse_input()
print(count_xmases(grid))

