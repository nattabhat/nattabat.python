import time
import turtle
import random

WIDTH, HEIGHT = 500, 500 #constant value
COLORS = ["red", "green", "blue", "gray", "yellow", "black", "orange", "brown", "violet", "purple"]


def get_number_of_racers():
    racers = 0
    while True: #ask user continuously
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid Value... Please enter a number")
            continue # here we need 'continue' because here is not the end of the while loop

        if 2 <= racers <= 10:
            return racers #match1
        else:
            print("Number is not in range of 2 - 10. Try Again!")
            #right here we don't need 'continue' since it is the end of the while loop


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
#   [ 0 ,   1 ,   2  ] = i
#   [red, blue, green] = color
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.speed(2)
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing Game")


racers = get_number_of_racers() #match1
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
#this work by
# [1, 2, 3, 4][:2]
# we will get [1, 2]
winner = race(colors)
print("The winner is the turtle with color:", winner)
# all turtles are not moving at same time, first turtle go first then second
time.sleep(3)


