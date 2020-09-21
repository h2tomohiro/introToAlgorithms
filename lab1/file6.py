import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

def draw_star(length):
    for i in range(5):
        t.forward(length)
        t.right(144)

draw_star(200)
screen.exitonclick()