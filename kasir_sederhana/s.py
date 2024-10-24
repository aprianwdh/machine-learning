import os
import manajemen_kasir  # Pastikan manajemen_kasir.py memiliki fungsi hitung_diskon

os.system("cls")
harga = 0
diskon = 0

txt = "Selamat Datang Di Kasir Sederhana"
greetings = txt.center(60, "=")
print(greetings)
txt = "Daftar Menu"
greetings = txt.center(60, "=")
print(greetings)

print('''
1. Nasi Goreng \t= Rp.12.000
2. Mie Goreng \t= Rp.10.000
3. Bakso Goreng \t= Rp.15.000
4. Nasi Bakar \t= Rp.13.000
5. Teh/Es Teh \t= Rp.3.000
''')

while True:
    Pesanan = int(input("Masukkan Pesanan (1-5) = "))
    if not isinstance(Pesanan, int) or Pesanan < 1 or Pesanan > 5:
        print("Masukkan pilihan antara 1 hingga 5")
        continue

    while True:
        jumlah = int(input("Masukkan Jumlah = "))
        if not isinstance(jumlah, int) or jumlah < 0:
            print("Jumlah harus berupa angka positif")
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

    yn = input("Masih ingin memesan? (y untuk lanjut, lain untuk selesai): ")
    if yn.lower() != "y":
        break

# Diskon berdasarkan keanggotaan
print('''
    Pilih Keanggotaan:
    1. Gold \t= Diskon 10%
    2. Silver \t= Diskon 5%
    3. Perunggu \t= Tidak ada diskon
''')
Keanggotaan = int(input("Masukkan Keanggotaan (1-3) = "))

if Keanggotaan == 1:
    diskon += 10
elif Keanggotaan == 2:
    diskon += 5
elif Keanggotaan == 3:
    diskon += 0
else:
    print("Pilihan keanggotaan tidak valid, tidak ada diskon yang diberikan.")
    
# Diskon tambahan untuk usia
nama = input("Masukkan Nama Pelanggan: ")
usia = int(input("Masukkan usia pelanggan: "))
if usia >= 65:
    diskon += 5  # Diskon tambahan 5% untuk pelanggan lanjut usia

# Menampilkan hasil akhir
harga_diskon = manajemen_kasir.hitung_diskon(harga, diskon)
print(f"Harga setelah diskon: Rp. {harga_diskon}")
print(f"Terima kasih, {nama}, atas pesanan Anda!")
