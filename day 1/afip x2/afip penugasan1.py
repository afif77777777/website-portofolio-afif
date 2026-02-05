n = int(input("Masukkan jumlah baris: "))

for i in range(1, n + 1):
    # mencetak spasi
    for j in range(n - i):
        print(" ", end="")
    # mencetak bintang
    for k in range(1, 2 * i):
        print("*", end="")
    print()1