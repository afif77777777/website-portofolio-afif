import turtle


def save_as_jpg(canvas, filename):
    ps_file = filename + ".eps"
    canvas.postscript(file=ps_file)
    img = Image.open(ps_file)
    img.save(filename + ".jpg", "JPEG")

def drawRectangle(ttl, x, y, width, height):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for _ in range(2):
        ttl.forward(width)
        ttl.right(90)
        ttl.forward(height)
        ttl.right(90)
    ttl.penup()

def filltriangle(ttl, x1, y1, x2, y2, x3, y3, color):
    ttl.fillcolor(color)
    ttl.penup()
    ttl.goto(x1, y1)
    ttl.pendown()
    ttl.begin_fill()
    ttl.goto(x2, y2)
    ttl.goto(x3, y3)
    ttl.goto(x1, y1)
    ttl.end_fill()
    ttl.penup()

# Colors (RGB)
myBlue   = (0, 63, 135)
myYellow = (255, 205, 0)
myRed    = (217, 0, 18)
myWhite  = (255, 255, 255)
myGreen  = (0, 122, 61)

Joe = turtle.Turtle()
Joe.speed(0)
Joe.hideturtle()

Joe.screen.colormode(255)

# Background rectangle
drawRectangle(Joe, 0, 300, 600, 300)

# Triangles (Seychelles flag)
filltriangle(Joe, 0, 0, 300, 200, 300, 0, myBlue)
filltriangle(Joe, 0, 0, 200, 300, 400, 300, myYellow)
filltriangle(Joe, 0, 0, 400, 300, 600, 300, myRed)
filltriangle(Joe, 0, 0, 600, 300, 600, 150, myWhite)
filltriangle(Joe, 0, 0, 600, 150, 600, 0, myGreen)

# Save image
ts = turtle.getscreen()
tc = ts.getcanvas()


turtle.done()
