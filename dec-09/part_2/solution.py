import os
from collections import defaultdict

def parse_input():
    dir = os.path.dirname(__file__)

    file = open(os.path.join(dir,'input.txt'), "r")

    disk = []
    spaces = {}
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
                spaces[index] = space_size
                disk += ["."] * space_size
                is_even = True
                index += space_size
            
    file.close()

    return disk, spaces, files

def move_file_blocks(disk, spaces, files):
    right = len(disk) - 1

    while right >= 0:
        # Right moves to left until hits an index containing id 
        if disk[right] == '.':
            right -= 1
        else:
            file_size = files[disk[right]]
            id = disk[right]

            # Left moves forward until finds a space large enough to contain right
            left, left_end = 0, 0

            while left_end < right and left_end - left < file_size:
                if disk[left] != '.':
                    left += 1
                    left_end = left
                elif disk[left_end] != '.':
                    left = left_end
                else:
                    left_end += 1
                    
            if left_end - left == file_size:
                for i in range(file_size):
                    disk[left + i] = id
                    disk[right - i] = '.'
            else:
                right -= files[id]
            
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