import os
from collections import defaultdict

def parse_input():
    dir = os.path.dirname(__file__)

    file = open(os.path.join(dir,'input.txt'), "r")

    disk = []
    spaces = []
    files = {}

    for line in file:
        id = 0
        index = 0
        is_even = True

        for char in line.rstrip():
            if is_even:
                file_size = int(char)
                disk += [id] * file_size
                files[id] = file_size
                is_even = False
                id += 1
                index += file_size
            else:
                space_size = int(char)
                spaces.append([index, space_size])
                disk += ["."] * space_size
                is_even = True
                index += space_size
            
    file.close()

    return disk, spaces, files

def move_file_block(disk, file_index, space_index, file_size):
    id = disk[file_index]

    for i in range(file_size):
        disk[file_index - i] = '.'
        disk[space_index + i] = id

    return disk

def move_file_blocks(disk, spaces, files):
    right = len(disk) - 1

    while right >= 0:
        # Right moves to left until hits an index containing id 
        if disk[right] == '.':
            right -= 1
        else:
            file_size = files[disk[right]]
            
            for i in range(len(spaces)):
                if spaces[i][0] >= right:
                    continue

                if spaces[i][1] > file_size:
                    disk = move_file_block(disk, right, spaces[i][0], file_size)
                    spaces[i][0] += file_size
                    spaces[i][1] -= file_size
                    break
                elif spaces[i][1] == file_size:
                    disk = move_file_block(disk, right, spaces[i][0], file_size)
                    spaces.pop(i)
                    break
            else:
                right -= file_size
            
    return disk

def get_checksum(disk):
    checksum = 0
    for i in range(len(disk)):
        if disk[i] == '.':
            continue
        
        checksum += i * disk[i]

    return checksum

disk, spaces, files = parse_input()
disk = move_file_blocks(disk, spaces, files)

print(get_checksum(disk))