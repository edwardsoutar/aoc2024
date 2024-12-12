import os
from collections import Counter
from functools import cache

def parse_input():
    dir = os.path.dirname(__file__)

    file = open(os.path.join(dir,'input.txt'), "r")

    stones = Counter()

    for line in file:
        for value in line.rstrip().split(" "):
            stones[int(value)] += 1

    file.close()

    return stones

def get_length(stone_weight):
    length = 0
    
    while stone_weight > 0:
        length += 1
        stone_weight = stone_weight // 10

    return length

def split(stone_weight):
    length = get_length(stone_weight)
    split_value = 0

    for i in range(length // 2):
        split_value += (stone_weight % 10) * (10 ** i)
        stone_weight = stone_weight // 10

    return [stone_weight, split_value]

@cache
def blink_once(stone_weight):
    if stone_weight == 0:
        return [1]
    
    elif get_length(stone_weight) % 2 == 0:
        return split(stone_weight)
    
    else:
        return [stone_weight * 2024]


def blink_x_times(x, stones):
    for _ in range(x):
        new_stones = Counter()

        for stone_weight in stones:
            for stone in blink_once(stone_weight):
                new_stones[stone] += stones[stone_weight]

        stones = new_stones

    return stones

def count_stones(stones):
    total = 0

    for count in stones.values():
        total += count

    return total

stones = parse_input()
stones = blink_x_times(75, stones)
print(count_stones(stones))