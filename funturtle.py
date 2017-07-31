import turtle
##turtle.shape('turtle')
##square = turtle.clone()
##square.shape('square')
##square.goto(100,100)
##square.goto(300,300)
##square.stamp()
##square.goto(100,100)

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
direction = UP
UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
SPACEBAR = "space"

def up():
    global direction
    direction=UP
    print("you pressed up")
def left():
    global direction
    direction=LEFT
    print("you pressed left")
def right():
    global direction
    direction=RIGHT
    print("you pressed right")
def down():
    global direction
    direction = DOWN
    print("you pressed down")

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, "Right")
turtle.listen()
turtle.mainloop()













