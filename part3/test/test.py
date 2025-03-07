# # from turtle import Turtle, Screen
# # import turtle
import turtle as t
from random import randint

screen = t.Screen()
print(screen.canvheight)

turtle = t.Turtle()
turtle.shape("turtle")
turtle.color("grey")
t.colormode(255)
turtle.speed("fastest")

# turtle2 = t.Turtle()
# turtle2.shape("turtle")
# turtle2.color("green")


# def dottedline():
#     for number in range(10):
#         turtle.pendown()
#         turtle.forward(10)
#         turtle.penup()
#         turtle.forward(10)

# turtle.forward(100)
# for number in range(72):
#     turtle.left(125)
#     turtle.forward(100)

# turtle2.right(180)
# turtle2.forward(100)
# for number in range(72):
#     turtle2.right(125)
#     turtle2.forward(100)

def move_forwards():
    turtle.forward(10)

def move_backwards():
    turtle.backward(10)

def turn_left():
    turtle.left(5)

def turn_right():
    turtle.right(5)

def clear():
    turtle.clear()
    turtle.teleport(0, 0)


screen.listen()
screen.onkeypress(move_forwards, "Up")
screen.onkeypress(move_backwards, "Down")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")
screen.onkeypress(clear, "")


screen.exitonclick()