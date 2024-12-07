import os

def parse_input():
    dir = os.path.dirname(__file__)

    file = open(os.path.join(dir,'input.txt'), "r")

    grid = []

    for line in file:
        grid.append(line.rstrip())
            
    file.close()

    return grid

def calculate_distinct_positions_visited(grid):
    rows, columns = len(grid), len(grid[0])


    def follow_guard_path(row, column):
        seen = set()
        seen.add((row, column))

        r, c = row, column

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        direction_index = 0

        while (r > 0 and r < rows - 1) and (c > 0 and c < columns - 1):
            direction = directions[direction_index]

            if grid[r + direction[0]][c + direction[1]] == '#':
                direction_index = (direction_index + 1) % len(directions)
                direction = directions[direction_index]

            r += direction[0]
            c += direction[1]

            seen.add((r, c))

        return len(seen)

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == "^":
                return follow_guard_path(row, column)
            
    return 0

grid = parse_input()

print(calculate_distinct_positions_visited(grid))