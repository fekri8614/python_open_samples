import turtle
import random

def draw_galaxy():
    for _ in range(500):
        turtle.penup()
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        turtle.speed(1000 * 1000)
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(random.choice(["blue", "cyan", "white", "light blue", "red", "pink"]))
        turtle.circle(1)

def create_screen():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Milky Way Galaxy")
    return screen

def main():
    screen = create_screen()
    draw_galaxy()
    turtle.done()

if __name__ == "__main__":
    main()