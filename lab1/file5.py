import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

def draw_five_square():
    for i in range(5):
        t.left(74)
        t.forward(50)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(50)

draw_five_square()
screen.exitonclick()
