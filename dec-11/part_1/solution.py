import os

class ListNode:
    def __init__(self, value = None, next = None):
        self.value = value
        self.set_length()
        self.next = next 

    def evolve(self):
        next = self.next

        if self.value == 0:
            self.value = 1
            self.length = 1

        elif self.length % 2 == 0:
            split_value = self.split()
            self.next = ListNode(split_value, next)
            
        else:
            self.value = self.value * 2024
            self.set_length()

        return next 

    def split(self): 
        split_value = 0

        for i in range(self.length // 2):
            split_value += (self.value % 10) * 10 ** i
            self.value = self.value // 10

        self.set_length()

        return split_value
    

    def set_length(self):
        self.length = 0
        value = self.value

        while value and value > 0:
            self.length += 1
            value = value // 10

def parse_input():
    dir = os.path.dirname(__file__)

    file = open(os.path.join(dir,'input.txt'), "r")

    arrangement_head = cur_node = ListNode()

    for line in file:
        for value in line.rstrip().split(" "):
            cur_node.next = ListNode(value = int(value))
            cur_node = cur_node.next

    file.close()

    return arrangement_head

def blink_x_times(x, head):
    for i in range(x):
        cur_node = head.next

        while cur_node:
            cur_node = cur_node.evolve()

    return head

def count_stones(head):
    if not head:
        return 0

    cur_node = head.next
    total = 0

    while cur_node:
        total += 1
        cur_node = cur_node.next

    return total

head = parse_input()
cur_node = blink_x_times(25, head)
print(count_stones(head))