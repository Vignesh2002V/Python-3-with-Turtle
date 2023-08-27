import turtle as Turtle
Turtle.speed(100)
Turtle.bgcolor('Black')

colors = ['Red','Yellow','Cyan']
for x in range(1000):
    Turtle.circle(x)
    Turtle.color(colors[x%3])
    Turtle.left(80)
