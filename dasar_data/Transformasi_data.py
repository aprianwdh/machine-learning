# membuat data menjadi upper case
data = "ini adAlah daTa"
print(data.upper())

# membuat data menjadi lower case
print(data.lower())

# menghapus space pada kiri data
data = "        ini data"
print(data.lstrip())

# menghapus space pada kanan data
data = "ini data       "
print(data.rstrip())

# menghapus space pada kanan dan kiri data
data = "        ini data             "
print(data.strip())

# menghapus yang selain space pada data
data = "CodeCodeDataCode"
print(data.strip("Code"))

# menemukan suatu kata pada awal string
data = "kamu adalah orang hebat"
print(data.startswith("kamu"))

# menemukan suatu kata pada akhir string
data = "kamu adalah orang hebat"
print(data.endswith("hebat"))

# menggabungkan string
data = " widhi "
print(data.join(["aprian","wibowo"]))

# memisahkan string
print("kamu luar biasa".split())

# mengganti elemet string
data = "kamu adalah pemenang"
print(data.replace("kamu","aku"))

# mengecek string apakah upper semua (bersifat boolean)
data = "KAMU SUKA?"
print(data.isupper())

# mengecek string apakah lower semua (bersifat boolean)
data = "KAMU SUKA?"
print(data.islower())

# mengecek apakah semua huruf alpabet (bersifat boolean)
data = "qwerty123"
print(data.isalpha())

# mengecek apakah semua huruf alpaber atau numerik atau dua duanya(bersifat boolean)
data = "qwerty"
print(data.isalnum())

# mengecek apakah semua huruf numerika / angka (bersifat boolean)
data = "qwerty123"
print(data.isdecimal())

# mengecak apakah hanya berisi white space
data = "        \n"
print(data.isspace())

# mengecek apakah berisi huruf kapital pada setiap kata pertamanya. 
data = "Ini Title Ya"
print(data.istitle())

# zfill() bertujuan untuk menambahkan nilai nol (0) di depan sebuah string dengan panjang tertentu.
data = "123345"#panjang data = 6
print(data.zfill(10))#akan ditambah 4 menjadi 10 panjangnya

# Metode rjust() berguna untuk merapikan pencetakan teks. 
# Dengan metode rjust() ini, Anda dapat membuat teks menjadi rata kanan sehingga tampilannya lebih rapi.
print("I Love Myself".rjust(20,"="))

# ljust()
print("I Love Myself".ljust(20,"="))

#center()
print("I Love Myself".center(20,"="))
print("I Love My Dream".center(20,"="))

