import turtle

# Setup layar dan turtle
s = turtle.Screen()
t = turtle.Turtle()
t.speed(3)

def pindah(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# 1. Persegi Panjang - Warna Merah
pindah(-250, 100)
t.fillcolor("black")
t.begin_fill()
for _ in range(2):
    t.forward(120)
    t.left(90)
    t.forward(60)
    t.left(90)
t.end_fill()

# 2. Segitiga - Warna Kuning
pindah(-50, 100)
t.fillcolor("black")
t.begin_fill()
for _ in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

# 3. Trapesium - Warna Hijau
pindah(100, 100)
t.fillcolor("black")
t.begin_fill()
t.forward(120)  # Sisi bawah
t.left(120)
t.forward(60)   # Sisi miring
t.left(60)
t.forward(60)   # Sisi atas
t.left(60)
t.forward(60)   # Sisi miring
t.end_fill()

# 4. Jajar Genjang - Warna Biru
pindah(-150, -100)
t.setheading(0) # Reset arah ke kanan
t.fillcolor("black")
t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.left(60)
    t.forward(50)
    t.left(120)
t.end_fill()

# 5. Segilima (Pentagon) - Warna Ungu
pindah(50, -100)
t.setheading(0)
t.fillcolor("black")
t.begin_fill()
for _ in range(5):
    t.forward(70)
    t.left(72)
t.end_fill()

t.hideturtle()
turtle.done()
