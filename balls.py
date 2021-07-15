import os
import time
import random


class Ball:

    # x_size -> (Canvas' width)
    # y_size -> (Canvas' height)
    x_size, y_size = os.get_terminal_size()
    x_size -= 6  # left a margin (right side)
    y_size -= 6  # left a margin (bottom side)

    def __init__(self, x_speed, y_speed, x_pos, y_pos):
        # Speeds won't change except their signs (+ or -)
        self.x_speed = x_speed
        self.y_speed = y_speed

        # Starting positions
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self):
        # if ball hit left or right side of canvas, reverse its x speed
        if self.x_pos < 2 or self.x_pos > Ball.x_size - 1:
            self.x_speed *= -1
        # if ball hit top or bottom side of canvas, reverse its y speed
        if self.y_pos < 1 or self.y_pos > Ball.y_size - 1:
            self.y_speed *= -1

        # add its speed to related position variable
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed

    # This method returns ball's x and y positions
    def give_pos(self):
        return [self.x_pos, self.y_pos]


os.system("clear")  # clear screen

ball_shape = "●"  # you can also try ◉ ○ ◌ ◐
wall_shape = "#"  # you can also try ■ ◆ ▦ ●

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
            random.randint(2, Ball.x_size),
            random.randint(2, Ball.y_size),
        )
    )

os.system("clear")

while True:

    # in every frame, code makes calculations for balls new position
    for a in balls:
        a.move()

    # Checking every coordinate (position)
    # Is there Ball or is it canvas' edge or empty
    for y in range(Ball.y_size + 1):
        for x in range(Ball.x_size + 1):

            for b in balls:
                if int(b.x_pos) == x and int(b.y_pos) == y:
                    print(ball_shape, end="\n" if x == Ball.x_size else "")
                    break
            else:
                if x == Ball.x_size:
                    print(wall_shape)  # its separate because need to go new line
                    continue
                if x == 0 or y == 0 or y == Ball.y_size:
                    print(wall_shape, end="")  # canvas borders (except right side)
                    continue
                print(" ", end="")  # if this coordinate empty make a space

    print("\nCtrl+c to exit")
    time.sleep(0.1)  # Delay between frames
    os.system("clear")
