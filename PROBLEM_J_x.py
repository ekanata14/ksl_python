def set_active(active):
    return active

def repeat_confirmation():
    repeat = input("Apakah ingin mengulang program? (ya/tidak): ")
    if repeat == "ya":
        set_active(True)
    elif repeat == "tidak":
        set_active(False)
    else:
        print("Inputan Anda salah ulangi kembali")
        set_active(True)
        repeat_confirmation()

active = set_active(True)
while active == True:
    usiaMiku = int(input("Masukkan Usia Nakano Miku (10-15 tahun): "))
    hargaKostum = int()

    if usiaMiku >= 10 and usiaMiku <= 12:
        hargaKostum = 50000
    elif usiaMiku >= 13 and usiaMiku <= 15:
        hargaKostum = 70000
    elif usiaMiku <= 10:
        print("Adek jangan cosplay ya masih bocil")
    else:
        print("Some errors occured or requirements not fulfilled")

    jumlahTemanMiku = int(input("Masukkan jumlah teman yang akan ikut cosplay (1-3 teman): "))
    if jumlahTemanMiku > 3 or jumlahTemanMiku < 1:
        print("Cosple ngajak temen lah masa' sendiri aowkwkwk")

    print("Biaya total untuk Nakano Miku dan " + str(jumlahTemanMiku) + " teman adalah: " + str(hargaKostum * (jumlahTemanMiku + 1)))
    repeat_confirmation()
    


