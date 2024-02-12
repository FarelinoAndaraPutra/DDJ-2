print("\npenggunaan continue pada looping")
print("-------------------\n")
a= 0
b = float(input("Masukan angka anda"))
while a < b: # a < b adalah syarat
    a += 1 # increment
    if a == 5: # seleksi kondisi
        continue # continue point
    print(a)