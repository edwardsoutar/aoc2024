import os

def out_of_boundary(row, column, grid):
    return row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0])

def hit_obstacle(grid, row, column, direction):
    if out_of_boundary(row + direction[0], column + direction[1], grid):
        return False

    return grid[row + direction[0]][column + direction[1]] == '#'

def parse_input():
    dir = os.path.dirname(__file__)

    file = open(os.path.join(dir,'input.txt'), "r")

    grid = []

    for line in file:
        grid.append([char for char in line.rstrip()])
            
    file.close()

    return grid


def get_guard_path(grid):
    rows, columns = len(grid), len(grid[0])

    def follow_guard_path(row, column):
        path = []

        r, c = row, column

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        direction_index = 0

        while not out_of_boundary(r, c, grid):
            path.append((r, c, direction_index))

            direction = directions[direction_index]

            if hit_obstacle(grid, r, c, direction):
                direction_index = turn(direction_index)
            else:
                r += direction[0]
                c += direction[1]
            
        return path

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == "^":
                return follow_guard_path(row, column)
            
    return 0

def turn(i):
    return (i + 1) % 4

def get_total_obstacles(grid, path):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def is_loop(row, column, index):
        seen = set()
        stack = [(row, column, index)]

        while stack:
            (r, c, i) = stack.pop()

            if (r, c, i) in seen:
                return True

            seen.add((r, c, i))

            direction = directions[i]

            if out_of_boundary(r, c, grid):
                return False

            if hit_obstacle(grid, r, c, direction):
                i = turn(i)
            else:
                r += direction[0]
                c += direction[1]
            
            stack.append((r, c, i))

        return False

    obstacles = set()
    start = path[0]

    for (row, column, direction_index) in path[:-1]:
        direction = directions[direction_index]

        if hit_obstacle(grid, row, column, direction):
            continue

        temp = grid[row + direction[0]][column + direction[1]]
        grid[row + direction[0]][column + direction[1]] = '#'

        if is_loop(start[0], start[1], 0):
            obstacles.add((row + direction[0], column + direction[1]))
        
        grid[row + direction[0]][column + direction[1]] = temp

    return len(obstacles)

grid = parse_input()
path = get_guard_path(grid)

print(get_total_obstacles(grid, path))