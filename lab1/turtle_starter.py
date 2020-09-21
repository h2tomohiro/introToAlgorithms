import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

def draw_square(length):
    for i in range(4):
        t.forward(length)
        t.right(90)

draw_square(400)
draw_square(100)
screen.exitonclick()
