import tkinter as tk
from tkinter import ttk

class KasirApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Kasir")

        # List data barang (nama dan harga)
        self.data_barang = [
            ("Kopi Arabika", 25.000),
            ("Kopi Robusta", 20.000),
            ("Cappuccino", 15.000),
            ("Espresso", 25.000),
            ("Latte", 35.000)
        ]

        # Inisialisasi list untuk menyimpan barang
        self.daftar_barang = []

        # Membuat label dan combobox untuk memilih nama barang
        tk.Label(root, text="Nama Barang:").grid(row=0, column=0)
        self.nama_combobox = ttk.Combobox(root, values=[item[0] for item in self.data_barang])
        self.nama_combobox.grid(row=0, column=1)

        tk.Label(root, text="Jumlah Barang:").grid(row=1, column=0)
        self.jumlah_entry = tk.Entry(root)
        self.jumlah_entry.grid(row=1, column=1)

        # Membuat tombol + dan - untuk menambah/mengurangi jumlah barang
        self.plus_button = tk.Button(root, text="+", command=self.tambah_jumlah)
        self.plus_button.grid(row=1, column=2)
        self.minus_button = tk.Button(root, text="-", command=self.kurangi_jumlah)
        self.minus_button.grid(row=1, column=3)

        # Membuat tombol untuk menambahkan barang ke dalam list
        self.tambah_button = tk.Button(root, text="Tambah Barang", command=self.tambah_barang)
        self.tambah_button.grid(row=2, columnspan=4)

        # Membuat listbox untuk menampilkan daftar barang
        self.listbox = tk.Listbox(root)
        self.listbox.grid(row=3, columnspan=4)

        # Membuat label untuk menampilkan total harga
        self.total_label = tk.Label(root, text="")
        self.total_label.grid(row=4, columnspan=4)

    def tambah_jumlah(self):
        current_value = int(self.jumlah_entry.get())
        self.jumlah_entry.delete(0, tk.END)
        self.jumlah_entry.insert(0, str(current_value + 1))

    def kurangi_jumlah(self):
        current_value = int(self.jumlah_entry.get())
        if current_value > 0:
            self.jumlah_entry.delete(0, tk.END)
            self.jumlah_entry.insert(0, str(current_value - 1))

    def tambah_barang(self):
        # Mendapatkan nilai dari combobox nama dan entry jumlah barang
        nama_barang = self.nama_combobox.get()
        jumlah = int(self.jumlah_entry.get())

        # Mencari harga barang berdasarkan nama barang dari list data_barang
        harga = None
        for item in self.data_barang:
            if item[0] == nama_barang:
                harga = item[1]
                break

        # Menambahkan barang ke dalam list
        if harga is not None:
            self.daftar_barang.append((nama_barang, harga, jumlah))

            # Menampilkan barang yang ditambahkan ke dalam listbox
            self.listbox.insert(tk.END, f"{nama_barang} - Rp {harga:.2f} - {jumlah} pcs")

            # Update total harga
            total_harga = sum(harga * jumlah for _, harga, jumlah in self.daftar_barang)
            self.total_label.config(text=f"Total Harga: Rp {total_harga:.2f}")
        else:
            tk.messagebox.showerror("Error", "Barang tidak ditemukan dalam daftar")

if __name__ == "__main__":
    root = tk.Tk()
    app = KasirApp(root)
    root.mainloop()
import tkinter as tk
from tkinter import ttk
