import random

angka_random = random.randint(0,100)


jumlah_pemain = int(input("Masukkan Jumlaah Pemain = "))


while True:
    for i in range(jumlah_pemain):
        tebak = int(input(f"Orang ke-{i+1} Masukkan Angkaa 0 - 100 = "))
        print(angka_random)
        if tebak < angka_random:
            print("Lebih Besar")
        elif tebak > angka_random:
            print("Lebih Kecil")
        else:
            print("binggo")
            break
    if tebak == angka_random:
        break



