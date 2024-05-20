import tkinter as tk
from tkinter import messagebox

class CoffeeShopApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Coffee Shop Kasir")

        self.total_price = 00
        self.item_prices = {
            "Espresso": 10,
            "Latte": 20,
            "Cappuccino": 20,
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

        self.total_label = tk.Label(self.master, text="Total Belanja: $0.00")
        self.total_label.grid(row=1, columnspan=3, padx=10, pady=10)

        self.money_label = tk.Label(self.master, text="Uang Pembeli:")
        self.money_label.grid(row=2, column=0, padx=10, pady=10)

        self.money_entry = tk.Entry(self.master)
        self.money_entry.grid(row=2, column=1, padx=10, pady=10)

        self.pay_button = tk.Button(self.master, text="Bayar", command=self.pay)
        self.pay_button.grid(row=2, column=2, padx=10, pady=10)

    def add_to_cart(self):
        item = self.menu_var.get()
        price = self.item_prices[item]
        self.total_price += price
        self.total_label.config(text=f"Total Belanja: ${self.total_price:.2f}")

    def pay(self):
        amount_paid = float(self.money_entry.get())
        if amount_paid < self.total_price:
            messagebox.showerror("Kesalahan", "Jumlah pembayaran kurang!")
        else:
            change = amount_paid - self.total_price
            messagebox.showinfo("Kembalian", f"Kembalian Anda: ${change:.2f}")
            self.total_price = 0.0
            self.total_label.config(text="Total Belanja: $0.00")

def main():
    root = tk.Tk()
    app = CoffeeShopApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
