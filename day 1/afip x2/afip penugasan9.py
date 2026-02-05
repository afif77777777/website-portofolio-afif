# Segitiga Bintang (Piramida)

n = int(input("Masukkan jumlah baris: "))

for i in range(1, n + 1):
    # spasi
    for j in range(n - i):
        print(" ", end="")
    # bintang
    for k in range(2 * i - 1):
        print("*", end="")
    print()