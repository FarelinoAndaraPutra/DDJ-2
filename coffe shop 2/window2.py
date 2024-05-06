import tkinter as tk
from tkinter import messagebox

class Menu:
    def __init__(self):
        self.menu_items = {'01': {'name': 'Kopi Hitam', 'price': 10000},
                           '02': {'name': 'Kopi Susu', 'price': 12000},
                           '03': {'name': 'Espresso', 'price': 15000},
                           '04': {'name': 'Cappuccino', 'price': 15000},
                           '05': {'name': 'Latte', 'price': 15000}}

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
