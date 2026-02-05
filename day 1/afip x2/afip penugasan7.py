while True:
    nilai = int(input("Masukkan nilai siswa: "))

    if nilai >= 75:
        print("Tuntas")
        break
    else:
        ulang = input("Nilai belum tuntas. Mengulang? (Ya/Tidak): ")
        if ulang.lower() != "ya":
            print("Tidak Tuntas")
            break