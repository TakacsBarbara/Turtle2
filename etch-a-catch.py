# Etch-a-catch
# You can draw the screen with the following keys: A , W, S, D
import turtle as turtle_module

tim = turtle_module.Turtle()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen = turtle_module.Screen()
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()
