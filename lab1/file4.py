import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

def draw_hexagon():
    for i in range(6):
        t.forward(100)
        t.left(120)
        t.forward(100)
        t.left(120)
        t.forward(100)
        t.left(180)

draw_hexagon()
screen.exitonclick()