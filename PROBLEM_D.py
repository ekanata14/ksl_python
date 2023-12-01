jumlah = int(input("Masukkan Jumlah Pengunjung: "))
listUmurPengunjung = []
harga = []
totalHarga = int()
totalHargaDiskon = float()

for i in range(1, jumlah+1):
    listUmurPengunjung.append(input("Masukkan Umur Pengunjung " + str(i) + " :"))
        
for i in range(0, len(listUmurPengunjung)):
    x = int(listUmurPengunjung[i])

    if x <= 3:
        harga.append(0)
    elif x >= 4 and x <= 10:
        harga.append(25000)
    elif x >= 11 and x <= 16:
        harga.append(30000)
    elif x >= 17:
        harga.append(50000)
    else:
        print("Some errors occured")
    
    totalHarga += harga[i]

if(totalHarga > 100000):
    totalHargaDiskon = totalHarga - (totalHarga * 0.1)
    print("Total sebelum diskon: " + str(totalHarga))
    print("Total setelah diskon: " + str(totalHargaDiskon))
else:
    print("Total sebelum diskon: " + str(0))
    print("Total setelah diskon: " + str(totalHarga))
    

