import os
from collections import defaultdict
import re

def parse_input():
    postrequisites = defaultdict(list)
    updates = []

    dir = os.path.dirname(__file__)

    file = open(os.path.join(dir,'input.txt'), "r")

    for line in file:
        line = line.rstrip()

        if line == "":
            continue

        match = re.fullmatch("^(\d+)\|(\d+)$", line)

        if match:
            postrequisites[int(match.group(1))].append(int(match.group(2)))
        else:
            update = line.split(",")

            updates.append([int(page) for page in update])

    file.close()

    return postrequisites, updates

def sum_middle_page_of_valid_updates(postrequisites, updates):
    def is_valid_update(update):
        seen = set()
        
        for page in update:
            for postrequisite in postrequisites[page]:
                if postrequisite in seen:
                    return False
  
            seen.add(page)

        return True
    
    def get_middle_page_number(update):
        middle = len(update) // 2

        return update[middle]

    sum_value = 0

    for update in updates:
        if is_valid_update(update):
            sum_value += get_middle_page_number(update)

    return sum_value

postrequisites, updates = parse_input()

print(sum_middle_page_of_valid_updates(postrequisites, updates))