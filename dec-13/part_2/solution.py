import os
import re

class Button:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

class Machine:
    def __init__(self):
        self.a = None
        self.b = None
        self.prize = None

    def set_a_button(self, a_x, a_y):
        self.a = Button(a_x, a_y)

    def set_b_button(self, b_x, b_y):
        self.b = Button(b_x, b_y)
        
    def set_prize(self, prize_x, prize_y):
        self.prize = [int(prize_x) + 10000000000000, int(prize_y) + 10000000000000]

    def get_minimum_tokens(self):
        x = ((self.prize[0] * self.b.y) - (self.prize[1] * self.b.x)) / ((self.a.x * self.b.y) - (self.a.y * self.b.x))
        y = ((self.prize[0] * self.a.y) - (self.prize[1] * self.a.x)) / ((self.a.x * self.b.y) - (self.a.y * self.b.x))
        
        if not x.is_integer() or not y.is_integer():
            return 0

        return abs(int(x)) * 3 + abs(int(y))
def parse_input():
    dir = os.path.dirname(__file__)

    file = open(os.path.join(dir,'input.txt'), "r")

    machines = []
    machine = Machine()

    for line in file:
        match_a = re.match("^Button A: X\+(\d+), Y\+(\d+)", line)
        match_b = re.match("^Button B: X\+(\d+), Y\+(\d+)", line)
        match_prize = re.match("^Prize: X=(\d+), Y=(\d+)", line)

        if match_a:
            machine.set_a_button(match_a.group(1), match_a.group(2))
        elif match_b:
            machine.set_b_button(match_b.group(1), match_b.group(2))
        elif match_prize:
            machine.set_prize(match_prize.group(1), match_prize.group(2))
        else:
            machines.append(machine)
            machine = Machine()

    machines.append(machine)
    machine = Machine()

    file.close()

    return machines
    
def get_minimum_tokens_for_all_machines(machines):
    minimum_tokens = 0

    for machine in machines:
        tokens = machine.get_minimum_tokens()

        minimum_tokens += tokens

    return minimum_tokens

machines = parse_input()
print(get_minimum_tokens_for_all_machines(machines))
