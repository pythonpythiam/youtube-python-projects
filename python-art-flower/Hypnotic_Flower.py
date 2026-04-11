import turtle

screen = turtle.Screen()

screen.setup(width=600, height=1000)

screen.setworldcoordinates(-300, -500, 300, 500)

screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.width(2)

colors = ["cyan", "magenta", "yellow", "lime", "orange"]

for i in range(150):
    t.pencolor(colors[i % len(colors)])
    t.circle(120)
    t.left(3)

turtle.done()
