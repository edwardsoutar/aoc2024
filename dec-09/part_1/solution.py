import os

def parse_input():
    dir = os.path.dirname(__file__)

    file = open(os.path.join(dir,'input.txt'), "r")

    disk = []

    for line in file:
        id = 0
        is_even = True

        for char in line.rstrip():
            if is_even:
                disk += [id] * int(char)
                is_even = False
                id += 1
            else:
                disk += ["."] * int(char)
                is_even = True
            
    file.close()

    return disk

def move_file_blocks(disk):
    left, right = 0, len(disk) - 1

    while left < right:
        if disk[left] != '.':
            left += 1
        elif disk[right] == '.':
            right -= 1
        else:
            disk[left] = disk[right]
            disk[right] = '.'
            left += 1
            right -= 1

    return disk

def get_checksum(disk):
    checksum = 0
    for i in range(len(disk)):
        if disk[i] == '.':
            break

        checksum += i * disk[i]

    return checksum

disk = parse_input()
disk = move_file_blocks(disk)

print(get_checksum(disk))