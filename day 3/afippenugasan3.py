import turtle

t = turtle.Turtle()
t.speed(3)

def gambar_bendera(x, y):
    # Pindah ke posisi awal
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # --- Bagian MERAH ---
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(2):
        t.forward(300) # Panjang bendera
        t.left(90)
        t.forward(100) # Lebar satu warna
        t.left(90)
    t.end_fill()
    
    # --- Bagian PUTIH (dengan garis tepi) ---
    t.penup()
    t.goto(x, y - 100) # Pindah ke bawah bagian merah
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    for _ in range(2):
        t.forward(300)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()
    
    # --- Opsional: Tiang Bendera ---
    t.penup()
    t.goto(x, y + 100)
    t.pendown()
    t.setheading(270) # Menghadap ke bawah
    t.pensize(5)
    t.forward(350)

# Jalankan fungsi
gambar_bendera(-150, 50)

t.hideturtle()
turtle.done()
