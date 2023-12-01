batasLooping = int(input("Masukkan batas looping: "))

for i in range(batasLooping, 0, -1):
    for j in range(1, batasLooping+1, 1):
        if i % 2 == 0 and j % 2 == 0:
            print(i, end="")
            print(j, "=> broo")
        else:
            print(i, end="")
            print(j, "=> bree")