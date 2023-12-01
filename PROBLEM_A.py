# Request user to input student name
namaSiswa = str(input("Nama Siswa: "))
print("--------------------------------")

# Variables for exam score
print("Inputkan Nilai Siswa: ")
matematika = int(input("Matematika: "))
informatika = int(input("Informatika: "))
biologi = int(input("Biologi: "))
kimia = int(input("Kimia: "))
fisika = int(input("Fisika: "))

# The average of the exam score above 
rerata = float((matematika + informatika + biologi + kimia + fisika ) / 5)
# The variable for score based on average exam score
nilai, comment = str("") 

# Condition to decide whether the student passed or not
if rerata < 70:
    nilai = "K"
    comment = "Tidak Lulus"
elif rerata >= 70 and rerata <= 75:
    nilai = "C"
    comment = "Lulus Bersyarat"
elif rerata >= 76 and rerata <= 85:
    nilai = "B"
    comment = "Lulus"
elif rerata >= 85:
    nilai = "A"
    comment = "Lulus"
else:
    print("Error or point is above or under minimum")

# Printing all the results above
print(namaSiswa + " mendapatkan nilai " + str(rerata) + " ("+nilai+") dan dinyatakan " + comment)