import tkinter as tk
from tkinter import messagebox

class CoffeeShopApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Coffee Shop Kasir")

        self.total_price = 00
        self.cart_items = []

        self.item_prices = {
            "Espresso": 15,
            "Latte": 20,
            "Cappuccino": 25,
            "Americano": 20,
            "Mocha": 30
        }

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Pilih Menu:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.menu_var = tk.StringVar(self.master)
        self.menu_var.set("Espresso")  # Default menu

        self.menu_dropdown = tk.OptionMenu(self.master, self.menu_var, *self.item_prices.keys())
        self.menu_dropdown.grid(row=0, column=1, padx=10, pady=10)

        self.add_button = tk.Button(self.master, text="Tambah", command=self.add_to_cart)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        self.cart_label = tk.Label(self.master, text="Keranjang Belanja:")
        self.cart_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.cart_listbox = tk.Listbox(self.master, width=40, height=10)
        self.cart_listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.total_label = tk.Label(self.master, text="Total Belanja: $0.00")
        self.total_label.grid(row=3, columnspan=3, padx=10, pady=10)

        self.money_label = tk.Label(self.master, text="Uang Pembeli:")
        self.money_label.grid(row=4, column=0, padx=10, pady=10)

        self.money_entry = tk.Entry(self.master)
        self.money_entry.grid(row=4, column=1, padx=10, pady=10)

        self.pay_button = tk.Button(self.master, text="Bayar", command=self.pay)
        self.pay_button.grid(row=4, column=2, padx=10, pady=10)

    def add_to_cart(self):
        item = self.menu_var.get()
        price = self.item_prices[item]
        self.cart_items.append((item, 1, price))  # default quantity is 1
        self.update_cart_listbox()
        self.calculate_total()

    def update_cart_listbox(self):
        self.cart_listbox.delete(0, tk.END)
        for item, quantity, price in self.cart_items:
            self.cart_listbox.insert(tk.END, f"{item} - {quantity}x: ${price:.2f}")

    def calculate_total(self):
        self.total_price = sum(quantity * price for _, quantity, price in self.cart_items)
        self.total_label.config(text=f"Total Belanja: ${self.total_price:.2f}")

    def pay(self):
        amount_paid = float(self.money_entry.get())
        if amount_paid < self.total_price:
            messagebox.showerror("Kesalahan", "Jumlah pembayaran kurang!")
        else:
            change = amount_paid - self.total_price
            messagebox.showinfo("Kembalian", f"Kembalian Anda: ${change:.2f}")
            self.reset()

    def reset(self):
        self.cart_items.clear()
        self.update_cart_listbox()
        self.calculate_total()
        self.money_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = CoffeeShopApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
