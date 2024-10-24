import os
import manajemen_kasir

os.system("cls")
harga = 0
diskon = 0
diskon_usia = 0

txt = "Selamat Datang Di Kssir Sederhana"
greatings = txt.center(60,"=")
print(greatings)
txt = "Daftar Menu"
greatings = txt.center(60,"=")
print(greatings)

print('''
1.Nasi Goreng \t= Rp.12.000
2.Mie Goreng \t= Rp.10.000
3.Bakso Goreng \t= Rp.15.000
4.Nasi Bakar \t= Rp.13.000
5.Teh/Es Teh \t= Rp.3.000
''')


while True:
    Pesanan = int(input("Masukkan Pesanan = "))
    if not isinstance(Pesanan,int) or Pesanan < 0:
        print("Harus int dan lebih dari 0")
        continue

    while True:
        jumlah = int(input("Masukan Jumlah = "))
        if not isinstance(jumlah,int) or jumlah < 0:
            print("Harus int dan lebih dari 0")
            continue
        break

    if Pesanan == 1:
        harga += 12000 * jumlah
    elif Pesanan == 2:
        harga += 10000 * jumlah
    elif Pesanan == 3:
        harga += 15000 * jumlah
    elif Pesanan == 4:
        harga += 13000 * jumlah
    elif Pesanan == 5:
        harga += 3000 * jumlah
    else:
        print("Input Salah")

    while True:
        yn = input("y jika lanjut = ")
        if yn != "y":
            break
    
    print('''
    1.Gold \t= Dsikon 10%
    2.Silver \t= Dsikon 5%
    3.Perunggu \t= Dsikon 0%
    ''')
    Keanggotaan = int(input("Masukkan Keanggotaan = "))

    if Keanggotaan == 1:
        diskon += 10
    elif Keanggotaan == 2:
        diskon += 5
    elif Keanggotaan == 3:
        diskon += 0
    else :
        print("keanggotaan salah")

    print('''
    Atas Nama = 
    ''')
    nama = input("Masukkan Nama Pelanggan = ")

    print('''
    Usia
    ''')
    usia = int(input("Masukkan usia pelangggan = "))
    if usia >65:
        diskon += 5

    
    break

harga_diskon = manajemen_kasir.hitung_diskon(harga,diskon)
print(diskon)
print(harga_diskon)



    


