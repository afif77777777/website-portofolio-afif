import tkinter as tk
from tkinter import messagebox

def simpan():
    data = f"""
Nama Lengkap : {e_nama.get()}
Tanggal Lahir: {e_ttl.get()}
Asal Sekolah : {e_sekolah.get()}
NISN         : {e_nisn.get()}
Nama Ayah    : {e_ayah.get()}
Nama Ibu     : {e_ibu.get()}
No Telp/HP   : {e_telp.get()}
Alamat       : {txt_alamat.get("1.0", tk.END)}
"""
    messagebox.showinfo("Data Tersimpan", data)

def hapus():
    e_nama.delete(0, tk.END)
    e_ttl.delete(0, tk.END)
    e_sekolah.delete(0, tk.END)
    e_nisn.delete(0, tk.END)
    e_ayah.delete(0, tk.END)
    e_ibu.delete(0, tk.END)
    e_telp.delete(0, tk.END)
    txt_alamat.delete("1.0", tk.END)

# ===== WINDOW =====
root = tk.Tk()
root.title("MainWindow")
root.geometry("500x650")
root.configure(bg="#eaeaea")

# ===== HEADER =====
header = tk.Label(
    root,
    text="DATA SISWA BARU",
    bg="#b2f0f7",
    fg="black",
    font=("Arial", 16, "bold"),
    pady=15
)
header.pack(fill="x")

# ===== FRAME FORM =====
form = tk.Frame(root, bg="#eaeaea")
form.pack(padx=20, pady=15, fill="x")

def label_entry(text):
    tk.Label(form, text=text, bg="#eaeaea", anchor="w").pack(fill="x")
    entry = tk.Entry(form)
    entry.pack(fill="x", pady=5)
    return entry

e_nama = label_entry("Nama Lengkap")
e_ttl = label_entry("Tanggal Lahir")
e_sekolah = label_entry("Asal Sekolah")
e_nisn = label_entry("NISN")
e_ayah = label_entry("Nama Ayah")
e_ibu = label_entry("Nama Ibu")
e_telp = label_entry("Nomor Telepon / HP")

tk.Label(form, text="Alamat", bg="#eaeaea", anchor="w").pack(fill="x")
txt_alamat = tk.Text(form, height=5)
txt_alamat.pack(fill="x", pady=5)

# ===== BUTTON =====
btn_frame = tk.Frame(root, bg="#eaeaea")
btn_frame.pack(pady=20)

tk.Button(
    btn_frame,
    text="Hapus",
    bg="#e67e22",
    fg="white",
    width=12,
    command=hapus
).pack(side="left", padx=10)

tk.Button(
    btn_frame,
    text="Simpan",
    bg="#e67e22",
    fg="white",
    width=12,
    command=simpan
).pack(side="left", padx=10)

root.mainloop()
