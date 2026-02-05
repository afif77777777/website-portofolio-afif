import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

BIAYA_PER_JAM = 2000

data_parkir = []
data_keluar = []

def hitung_biaya():
    try:
        masuk = datetime.strptime(entry_masuk.get(), "%H:%M")
        keluar = datetime.strptime(entry_keluar.get(), "%H:%M")

        durasi = (keluar - masuk).seconds / 3600
        durasi = max(1, int(durasi))

        biaya = durasi * BIAYA_PER_JAM
        entry_biaya.delete(0, tk.END)
        entry_biaya.insert(0, str(biaya))
        return biaya
    except:
        messagebox.showerror("Error", "Format waktu salah (HH:MM)")
        return 0

def tambah_data():
    plat = entry_plat.get()
    masuk = entry_masuk.get()
    keluar = entry_keluar.get()

    if not plat or not masuk or not keluar:
        messagebox.showwarning("Warning", "Data belum lengkap")
        return

    biaya = hitung_biaya()

    data = (plat, masuk, keluar, biaya)
    data_parkir.append(data)
    data_keluar.append(data)

    tabel_keluar.insert("", tk.END, values=data)
    update_bayar_terbanyak()

    entry_plat.delete(0, tk.END)
    entry_masuk.delete(0, tk.END)
    entry_keluar.delete(0, tk.END)
    entry_biaya.delete(0, tk.END)

def update_bayar_terbanyak():
    for i in tabel_bayar.get_children():
        tabel_bayar.delete(i)

    urut = sorted(data_keluar, key=lambda x: x[3], reverse=True)
    for d in urut:
        tabel_bayar.insert("", tk.END, values=d)

# ===== GUI =====
root = tk.Tk()
root.title("Aplikasi Parkir Kelompok 6")
root.geometry("900x500")

# ===== Input =====
frame_input = tk.Frame(root)
frame_input.pack(side=tk.LEFT, padx=20)

tk.Label(frame_input, text="Cari NoPol").grid(row=0, column=0, sticky="w")
entry_cari = tk.Entry(frame_input)
entry_cari.grid(row=0, column=1)

tk.Label(frame_input, text="No Plat Polisi").grid(row=1, column=0, sticky="w")
entry_plat = tk.Entry(frame_input)
entry_plat.grid(row=1, column=1)

tk.Label(frame_input, text="Waktu Masuk (HH:MM)").grid(row=2, column=0, sticky="w")
entry_masuk = tk.Entry(frame_input)
entry_masuk.grid(row=2, column=1)

tk.Label(frame_input, text="Waktu Keluar (HH:MM)").grid(row=3, column=0, sticky="w")
entry_keluar = tk.Entry(frame_input)
entry_keluar.grid(row=3, column=1)

tk.Label(frame_input, text="Biaya").grid(row=4, column=0, sticky="w")
entry_biaya = tk.Entry(frame_input)
entry_biaya.grid(row=4, column=1)

tk.Button(frame_input, text="Button", command=tambah_data).grid(row=5, column=1, pady=10)

# ===== Biaya =====
frame_biaya = tk.Frame(root)
frame_biaya.pack(side=tk.TOP, pady=20)

tk.Label(frame_biaya, text="Biaya Per Jam", fg="red", font=("Arial", 14)).pack()
tk.Label(frame_biaya, text="Rp. 2.000", fg="red", font=("Arial", 24, "bold")).pack()

# ===== Tabel =====
frame_tabel = tk.Frame(root)
frame_tabel.pack(side=tk.BOTTOM, pady=10)

tk.Label(frame_tabel, text="List Pelanggan Urut Terakhir Keluar").grid(row=0, column=0)
tk.Label(frame_tabel, text="List Pelanggan Banyak Bayar").grid(row=0, column=1)

kolom = ("No Plat Polisi", "Masuk", "Keluar", "Biaya")

tabel_keluar = ttk.Treeview(frame_tabel, columns=kolom, show="headings", height=8)
for k in kolom:
    tabel_keluar.heading(k, text=k)
tabel_keluar.grid(row=1, column=0, padx=10)

tabel_bayar = ttk.Treeview(frame_tabel, columns=kolom, show="headings", height=8)
for k in kolom:
    tabel_bayar.heading(k, text=k)
tabel_bayar.grid(row=1, column=1, padx=10)

root.mainloop()
