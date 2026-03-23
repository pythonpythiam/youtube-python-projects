import turtle

t = turtle.Turtle()
t.speed(8)

# Background
turtle.bgcolor("black")

# Heart color
t.color("red")
t.begin_fill()

# Draw heart
t.left(140)
t.forward(180)

t.circle(-90, 200)
t.left(120)
t.circle(-90, 200)

t.forward(180)
t.width(3)
t.end_fill()

turtle.done()
