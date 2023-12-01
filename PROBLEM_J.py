active = True

while active == True:
    usiaMiku = int(input("Masukkan Usia Nakano Miku (10-15 tahun): "))
    hargaKostum = int()

    if usiaMiku >= 10 and usiaMiku <= 12:
        hargaKostum = 50000
    elif usiaMiku >= 13 and usiaMiku <= 15:
        hargaKostum = 70000
    elif usiaMiku <= 10:
        print("-----------------------------------------")
        print("Adek jangan cosplay ya masih bocil")
        hargaKostum = 0
    else:
        print("-----------------------------------------")
        print("Some errors occured or requirements not fulfilled")

    print("-----------------------------------------")

    jumlahTemanMiku = int(input("Masukkan jumlah teman yang akan ikut cosplay (1-3 teman): "))
    print("-----------------------------------------")
    if jumlahTemanMiku < 1:
        print("Cosple ngajak temen lah masa' sendiri aowkwkwk")
    elif jumlahTemanMiku > 3:
        print("Mantap banyak bet ngajak temen aowkwk") 

    print("-----------------------------------------")

    if hargaKostum == 0:
        print("Adek masih kecil jangan cosple, mending belajar biar sukses")
    else:
        print("Biaya total untuk Nakano Miku dan " + str(jumlahTemanMiku) + " teman adalah: " + str(hargaKostum * (jumlahTemanMiku + 1)))
    
    print("-----------------------------------------")

    repeat = input("Apakah ingin mengulang program? (ya/tidak): ")

    if repeat == "ya":
        active = True
    elif repeat == "tidak":
        break
    else: 
        while repeat != "ya" or repeat != "tidak":
            repeat = input("Inputan Anda salah ulangi kembali (ya/tidak): ") 
            if repeat == "ya":
                active = True
                break
            elif repeat == "tidak":
                active = False
                break
            else:
                print("Yang bener masukin bang") 


