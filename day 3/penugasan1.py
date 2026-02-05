import turtle

t = turtle.Turtle()
t.speed(5)

def gambar_bangun(sisi, warna, x, y, jenis):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(warna)
    t.begin_fill()
    
    if jenis == "persegi_panjang":
        for _ in range(2):
            t.forward(100); t.left(90)
            t.forward(50); t.left(90)
    elif jenis == "segitiga":
        for _ in range(3):
            t.forward(80); t.left(120)
    elif jenis == "trapesium":
        t.forward(100); t.left(120); t.forward(50)
        t.left(60); t.forward(50); t.left(60); t.forward(50)
    elif jenis == "jajar_genjang":
        for _ in range(2):
            t.forward(100); t.left(60); t.forward(50); t.left(120)
    elif jenis == "segilima":
        for _ in range(5):
            t.forward(60); t.left(72)
            
    t.end_fill()

# Memanggil fungsi
gambar_bangun(0, "red", -200, 100, "persegi_panjang")
gambar_bangun(0, "yellow", -50, 100, "segitiga")
gambar_bangun(0, "green", 100, 100, "trapesium")
gambar_bangun(0, "blue", -150, -50, "jajar_genjang")
gambar_bangun(0, "purple", 50, -50, "segilima")
