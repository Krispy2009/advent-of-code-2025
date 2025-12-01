
START = 50

class Dial:
    def __init__(self, start):
        self.position = start
        self.max = 99
        self.min = 0
        self.points_at_zero = 0

    def turn(self, direction, clicks):
        if direction == "L":
            for i in range(clicks):
                self.position -= 1
                if self.position == 0:
                    self.points_at_zero += 1
                if self.position < self.min:
                    self.position = self.max
        elif direction == "R":
            for i in range(clicks):
                self.position += 1
                if self.position > self.max:
                    self.position = self.min
                    self.points_at_zero += 1
   
    def get_position(self):
        return self.position


def parse_line(line):
    directon, clicks = line.strip()[0], int(line.strip()[1:])
    return directon, clicks

if __name__ == "__main__":

    dial_points_at_zero = 0

    with open("input.txt", "r") as file:
        lines = file.readlines()
        dial = Dial(START)
        for line in lines:
            direction, clicks = parse_line(line)
            dial.turn(direction, clicks)

    print(f"Password is: {dial.points_at_zero}")
