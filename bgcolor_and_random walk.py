import turtle as Turtle
import random

Turtle.speed(10000)
Turtle.bgcolor('Black')
turns = 1000000000000000
distance = 20

for x in range(turns):
    right = Turtle.right(random.randint(0, 360))
    left = Turtle.left(random.randint(0, 360))
    Turtle.color(random.choice(['Blue','Red','Green','Cyan','Magenta','Pink','Violet']))
    random.choice([right, left])
    Turtle.forward(distance)
