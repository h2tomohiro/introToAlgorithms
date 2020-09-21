import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

def draw_square(a):
    t.fillcolor("green")
    t.begin_fill()
    t.penup()
    t.goto(-150, 150)
    t.pendown()
    for i in range(4):
        t.color("green")
        t.forward(a)
        t.right(90)
    t.end_fill()
    t.home()
    t.fillcolor("blue")
    t.begin_fill()
    t.color('blue', 'blue')
    t.end_fill()

def draw_turtle():
    s = 0
    for i in range(12):
        t.penup()
        t.forward(90)
        t.pendown()
        t.forward(20)
        t.penup()
        t.home()
        s += 1
        t.left(30*s)

draw_square(300)
draw_turtle()
screen.exitonclick()