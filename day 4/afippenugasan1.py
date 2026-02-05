import tkinter as tk
from tkinter import messagebox

# Fungsi menghitung total
def hitung_total():
    try:
        harga = float(entry_harga.get())
        kuantitas = int(entry_kuantitas.get())
        total = harga * kuantitas
        label_total.config(text=f"Total: Rp.{total:,.2f}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

# Window utama
root = tk.Tk()
root.title("Program Kasir")
root.geometry("300x200")

# Label dan Entry Harga
label_harga = tk.Label(root, text="Harga:")
label_harga.pack(pady=(20, 0))

entry_harga = tk.Entry(root)
entry_harga.pack()

# Label dan Entry Kuantitas
label_kuantitas = tk.Label(root, text="Kuantitas:")
label_kuantitas.pack(pady=(10, 0))

entry_kuantitas = tk.Entry(root)
entry_kuantitas.pack()

# Tombol Hitung Total
button_hitung = tk.Button(root, text="Hitung Total", command=hitung_total)
button_hitung.pack(pady=10)

# Label Total
label_total = tk.Label(root, text="Total: Rp.0.00")
label_total.pack()

root.mainloop()
