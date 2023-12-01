listUsiaKeluarga = []
listHarga = []
listNamaKeluarga = ["Anak", "Remaja", "Ayah", "Ibu"]
totalHarga = int()
keluarga = True

for i in range(0, len(listNamaKeluarga)):
    listUsiaKeluarga.append(int(input("Masukkan Usia " + listNamaKeluarga[i] + ": " )))

for i in listUsiaKeluarga:
    if i < 10:
        listHarga.append(10000)
    elif i >= 10 and i <= 17:
        listHarga.append(20000)
    elif i >= 18:
        listHarga.append(25000)
    else:
        print("Some errors occured or requirements not fulfilled")

for i in listHarga:
    totalHarga += i

if(keluarga):
    totalHarga = totalHarga - (totalHarga * 0.02)
else:
    totalHarga = totalHarga

print("BIAYA YANG HARUS DIBAYAR AOI SORE SAAT LIBURAN KE KOLAM RENANG")
print("Biaya total yang harud dibayar Aoi Sora adalah: Rp." + str(totalHarga))    
