print("\nPenggunaan Break pada Looping")
print("--------------------\n")
a = 0
b = float (input("Masukan angka anda : "))
while a < b: # a < b adalah syarat
    print(a)
    if a == 5: # Seleksi kondisi
        break # break point
    a += 1 # increment