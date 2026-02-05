import turtle

def draw_square(ttl, x, y, length):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for _ in range(4):
        ttl.forward(length)
        ttl.right(90)
    ttl.penup()

bob = turtle.Turtle()
bob.speed(10)
bob.pensize(3)
bob.color("blue")

draw_square(bob, 0, 0, 100)

turtle.done()
