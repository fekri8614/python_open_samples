import turtle

try:
    for i in range(20):
        turtle.bgcolor('black')
        turtle.pencolor('white')
        turtle.fd(i - 20)
        turtle.left(48)
        turtle.speed(0)
        #turtle.done()
    for k in range(100):
        turtle.pencolor('pink')
        turtle.fd(k + 2)
        turtle.right(k / 2)
except Exception as e:
    assert e
