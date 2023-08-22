import turtle
import random

BRANCH_HEIGHT = 100
BRANCH_WEIGHT = (0.8, 0.9)
BRANCH_RANGE = BRANCH_HEIGHT * 0.45
DRAW_STEPS = 0
DRAW_BACKGROUND = "black"
PENCIL_COLOR = "#406c35"
PENCIL_POSITION = (0, -250)


def drawTree(size, pencil) -> None:
    pencil.pensize(size/10)
    if size < (BRANCH_RANGE):
        return None
    pencil.forward(size)
    pencil.left(30)
    drawTree(size*random.uniform(*BRANCH_WEIGHT), pencil)
    pencil.right(60)
    drawTree(size*random.uniform(*BRANCH_WEIGHT), pencil)
    pencil.left(30)
    pencil.backward(size)


if __name__ == "__main__":
    window = turtle.Screen()
    window.bgcolor(DRAW_BACKGROUND)

    pencil = turtle.Turtle()
    pencil.speed(DRAW_STEPS)
    pencil.left(90)
    pencil.penup()
    pencil.setpos(PENCIL_POSITION)
    pencil.pendown()
    pencil.hideturtle()
    pencil.color(PENCIL_COLOR)

    drawTree(BRANCH_HEIGHT, pencil)

    window.exitonclick()
