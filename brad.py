import turtle
import time

def draw_square(some_turtle):
    for i  in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")

    time.sleep(5)

    brad = turtle.Turtle()
    brad.shape("triangle")
    brad.color("purple")
    brad.speed(1)
    
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)

    peter = turtle.Turtle()
    peter.speed(1)
    peter.shape("circle")
    peter.color("green")
    peter.circle(150)
    

    window.exitonclick()

draw_square()