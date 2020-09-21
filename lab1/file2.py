import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

def draw_square(b):
    for i in range(4):
        t.forward(b)
        t.right(90)

def draw_small_square(s):
    t.penup()
    t.goto(120,45)
    t.right(45)
    t.pendown()
    for i in range(4):
        t.forward(s)
        t.right(90)

draw_square(250)
draw_small_square(250)
screen.exitonclick()