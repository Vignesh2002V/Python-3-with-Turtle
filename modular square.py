import turtle as Turtle
import time

def square(length):
    for i in range(4):
        print(i)
        Turtle.forward(length)
        Turtle.left(90)

if __name__== "__main__":
    square(150)
    square(50)
    time.sleep(10)
    Turtle.bye()
