import turtle

def draw_face(pen):
    pen.penup()
    pen.goto(-100, 200)
    pen.pendown()
    pen.circle(100)

def draw_left_eye(pen):
    pen.penup()
    pen.goto(-50, 150)
    pen.pendown()
    pen.circle(20)

def draw_right_eye(pen):
    pen.penup()
    pen.goto(50, 150)
    pen.pendown()
    pen.circle(20)

def draw_nose(pen):
    pen.penup()
    pen.goto(0, 100)
    pen.pendown()
    pen.circle(10)

def draw_mouth(pen):
    pen.penup()
    pen.goto(-30, 50)
    pen.pendown()
    pen.circle(40, 180)

def draw_hair(pen):
    pen.penup()
    pen.goto(-50, 150)
    pen.pendown()
    pen.circle(50)
    pen.penup()
    pen.goto(50, 150)
    pen.pendown()
    pen.circle(50)

def draw_flowers(pen):
    for i in range(5):
        pen.penup()
        pen.goto(0, 0)
        pen.pendown()
        pen.color("red")
        pen.circle(5)
        pen.penup()
        pen.goto(10, 10)
        pen.pendown()
        pen.color("yellow")
        pen.circle(5)

def create_screen():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Famous Person's Face")
    return screen

def main():
    screen = create_screen()
    pen = turtle.Turtle()
    pen.speed(0)
    pen.width(3)

    draw_face(pen)
    draw_left_eye(pen)
    draw_right_eye(pen)
    draw_nose(pen)
    draw_mouth(pen)
    draw_hair(pen)

    pen2 = turtle.Turtle()
    pen2.speed(0)
    pen2.width(3)
    draw_flowers(pen2)

    turtle.done()

if __name__ == "__main__":
    main()