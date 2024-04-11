import turtle

def draw_name(name):
    screen = turtle.Screen()
    screen.bgcolor("white")

    jacob_turtle = turtle.Turtle()
    jacob_turtle.speed(0)
    jacob_turtle.penup()
    jacob_turtle.goto(-200, 0)
    jacob_turtle.pendown()

    colors = ["Blue", "Red", "Green"]

    for i, letter in enumerate(name):
        jacob_turtle.color(colors[i % len(colors)])
        jacob_turtle.write(letter, font=("Arial", 24, "bold"))
        jacob_turtle.penup()
        jacob_turtle.forward(40)

    jacob_turtle.hideturtle()
    screen.mainloop()

name = input("Enter your name: ")
draw_name(name)
