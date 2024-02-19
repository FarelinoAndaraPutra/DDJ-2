data_penjualan = [
    {"produk":"Baju", "jumlah":20},
    {"produk":"Celana", "jumlah":15},
    {"produk":"Sepatu", "jumlah":25},
    {"produk":"Tas", "jumlah":10},
    ]

total_penjualan = 0
for item in data_penjualan:
    total_penjualan += item["jumlah"]

print("total_penjualan : ", total_penjualan)