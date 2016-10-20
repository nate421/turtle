import turtle
import time

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    time.sleep(5)

    brad = turtle.Turtle()
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    
    

    window.exitonclick()

draw_square()