
import turtle

# Pengaturan layar
s = turtle.Screen()
t = turtle.Turtle()
t.speed(0) # Kecepatan maksimal
t.left(90) # Pohon tumbuh ke atas

def fibonacci_tree(n, length):
    """
    n: jumlah iterasi (kedalaman pohon)
    length: panjang cabang
    """
    if n > 0:
        # Gambar batang utama
        t.forward(length)
        
        # Cabang Kanan
        t.right(30)
        fibonacci_tree(n - 1, length * 0.7) # n-1 mengikuti pola rekursi
        
        # Cabang Kiri
        t.left(60)
        fibonacci_tree(n - 2, length * 0.7) # n-2 untuk logika Fibonacci
        
        # Kembali ke posisi semula
        t.right(30)
        t.backward(length)

# Pindah ke posisi bawah layar
t.penup()
t.goto(0, -200)
t.pendown()
t.color("darkgreen")

# Memanggil fungsi: n=10 untuk pohon yang rimbun
fibonacci_tree(10, 100)

turtle.done()
