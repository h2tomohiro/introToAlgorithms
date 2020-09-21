import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

def draw_two_square():
    for i in range(1):
        t.pensize(3)
        draw_square(200)
        t.penup()
        t.goto(-75, -100)
        t.pendown()
        draw_square(200)

draw_two_square()
screen.exitonclick()