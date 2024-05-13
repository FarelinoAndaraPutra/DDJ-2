import tkinter as tk
from tkinter import messagebox

class Menu:
    def __init__(self):
        self.menu_items = {'1': {'name': 'Kopi Hitam', 'price': 10000},
                           '2': {'name': 'Kopi Susu', 'price': 12000},
                           '3': {'name': 'Espresso', 'price': 15000},
                           '4': {'name': 'Cappuccino', 'price': 15000},
                           '5': {'name': 'Latte', 'price': 15000}}

    def display_menu(self):
        print("Menu:")
        for key, value in self.menu_items.items():
            print(f"{key}. {value['name']}: Rp {value['price']}")

class Order:
    def __init__(self):
        self.order_items = {}

    def add_item(self, item, quantity):
        if item in self.order_items:
            self.order_items[item] += quantity
        else:
            self.order_items[item] = quantity

    def calculate_total(self, menu):
        total = 0
        for item, quantity in self.order_items.items():
            total += menu.menu_items[item]['price'] * quantity
        return total

def place_order():
    try:
        choice = int(entry_menu.get())
        quantity = int(entry_quantity.get())
        if choice in range(1, 6):
            order.add_item(str(choice), quantity)
            messagebox.showinfo("Info", "Item berhasil ditambahkan ke pesanan!")
        else:
            messagebox.showerror("Error", "Pilihan tidak valid. Silakan pilih nomor menu yang benar.")
    except ValueError:
        messagebox.showerror("Error", "Input harus berupa nomor.")

def display_total():
    total = order.calculate_total(menu)
    messagebox.showinfo("Total", f"Total harga pesanan: Rp {total}")

menu = Menu()
order = Order()

# Set up GUI
root = tk.Tk()
root.title("Menu Kopi")

label_menu = tk.Label(root, text="Masukkan nomor menu:")
label_menu.grid(row=0, column=0, padx=10, pady=10)

entry_menu = tk.Entry(root)
entry_menu.grid(row=0, column=1, padx=10, pady=10)

label_quantity = tk.Label(root, text="Masukkan jumlah pesanan:")
label_quantity.grid(row=1, column=0, padx=10, pady=10)

entry_quantity = tk.Entry(root)
entry_quantity.grid(row=1, column=1, padx=10, pady=10)

button_order = tk.Button(root, text="Tambahkan ke Pesanan", command=place_order)
button_order.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

button_total = tk.Button(root, text="Tampilkan Total", command=display_total)
button_total.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

import tkinter as tk

import tkinter as tk
from tkinter import ttk

class KasirApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Kasir")

        # List data barang (nama dan harga)
        self.data_barang = [
            ("Kopi Arabika", 25000),
            ("Kopi Robusta", 20000),
            ("Cappuccino", 30000),
            ("Espresso", 28000),
            ("Latte", 32000)
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

        # Label dan inputan untuk uang yang diberikan pelanggan
        tk.Label(root, text="Uang Pelanggan:").grid(row=5, column=0)
        self.uang_entry = tk.Entry(root)
        self.uang_entry.grid(row=5, column=1)

        # Tombol untuk pembayaran
        self.bayar_button = tk.Button(root, text="Bayar", command=self.bayar)
        self.bayar_button.grid(row=5, column=2, columnspan=2)

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

    def bayar(self):
        # Mendapatkan total harga dan uang yang diberikan pelanggan
        total_harga = sum(harga * jumlah for _, harga, jumlah in self.daftar_barang)
        uang_pelanggan = float(self.uang_entry.get())

        # Menghitung kembalian
        kembalian = uang_pelanggan - total_harga

        # Menampilkan struk pembayaran
        struk = "===== Struk Pembayaran =====\n"
        for nama_barang, harga, jumlah in self.daftar_barang:
            struk += f"{nama_barang} - Rp {harga:.2f} - {jumlah} pcs\n"
        struk += f"\nTotal Harga: Rp {total_harga:.2f}\n"
        struk += f"Uang Pelanggan: Rp {uang_pelanggan:.2f}\n"
        struk += f"Kembalian: Rp {kembalian:.2f}\n"
        struk += "============================="
        tk.messagebox.showinfo("Struk Pembayaran", struk)

if __name__ == "__main__":
    root = tk.Tk()
    app = KasirApp(root)
    root.mainloop()
