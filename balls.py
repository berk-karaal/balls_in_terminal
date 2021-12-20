import os
import time
import random


# x_size -> (Canvas' width)
# y_size -> (Canvas' height)
x_size, y_size = os.get_terminal_size()
y_size -= 6  # left a margin (bottom side)
x_size -= 6  # left a margin (right side)


class Ball:
    def __init__(self, x_speed, y_speed, x_pos, y_pos):
        # Speeds won't change except their signs (+ or -)
        self.x_speed = x_speed
        self.y_speed = y_speed

        # Starting positions
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self):
        # if ball hit left or right side of canvas, reverse its x speed
        if self.x_pos < 2 or self.x_pos > x_size - 1:
            self.x_speed *= -1
        # if ball hit top or bottom side of canvas, reverse its y speed
        if self.y_pos < 1 or self.y_pos > y_size - 1:
            self.y_speed *= -1

        # add its speed to related position variable
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed

    # This method returns ball's x and y positions
    def give_pos(self):
        return [self.x_pos, self.y_pos]


os.system("clear")  # clear screen

ball_shape = "●"  # you can also try ◉ ○ ◌ ◐

# Asking user for balls count to display
while True:
    try:
        n = int(input("How many balls? : "))
        if n > 0:
            break
        else:
            print("Please enter an integer greater than 0")
    except:
        print("Please enter an integer greater than 0")

# Adding balls to list as much as user wants
# and giving them random values for needed arguments
balls = []
for i in range(n):
    balls.append(
        Ball(
            random.randint(100, 400) / 100,
            random.randint(100, 400) / 100,
            random.randint(2, x_size),
            random.randint(2, y_size),
        )
    )

os.system("clear")

border_char = ["┃", "┏", "━", "┓", "┛", "┗"]
"""indexes represent these positions:
123
0 0
524
"""

while True:
    # in every frame, code makes calculations for balls new position
    for a in balls:
        a.move()

    # Checking every coordinate (position)
    # Is there Ball or is it canvas' edge or empty
    for y in range(y_size + 1):
        line = ""
        for x in range(x_size + 1):

            for ball in balls:
                if int(ball.x_pos) == x and int(ball.y_pos) == y:
                    line += ball_shape
                    break
            else:
                if x == 0:
                    if y == 0:
                        line += border_char[1]
                    elif y == y_size:
                        line += border_char[5]
                    else:
                        line += border_char[0]

                elif x == x_size:
                    if y == 0:
                        line += border_char[3]
                    elif y == y_size:
                        line += border_char[4]
                    else:
                        line += border_char[0]

                elif y == 0 or y == y_size:
                    line += border_char[2]

                else:
                    line += " "

        print(line)

    print("\nCtrl+c to exit")
    time.sleep(0.1)  # Delay between frames
    os.system("clear")
