tinggi = int(input("Masukkan Tinggi Belah Ketupat: "))

for i in range(1, tinggi + 1):
    for k in range(tinggi, i, -1):
        print(" ", end="")
    for j in range(0, i, 1):
        print("*", end="")
    print("\r")

print("\r")

for i in range(0, tinggi):
    for j in range(0, i, 1):
        print(" ", end="")
    for k in range(tinggi, i, -1):
        print("*", end="")
    print("\r")

