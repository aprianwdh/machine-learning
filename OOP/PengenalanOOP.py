# #membuat class
# class Modil:
#     warna = "merah"

# #membuat pbject
# mobil_1 = Modil()
# print(mobil_1.warna)
# mobil_1.warna = "hijau"
# print(mobil_1.warna)

# #class constructor
# class Motor:
#     #atribut instance
#     def __init__(self,warna,merek,kecepatan):
#         self.warna = warna
#         self.merek = merek
#         self.kecepatan = kecepatan

# motor_1 = Motor(warna="merah",merek="Mazda",kecepatan="9999")
# print(f"warna = {motor_1.warna}  merek = {motor_1.merek} kecepatan = {motor_1.kecepatan}")
# motor_2 = Motor(warna="pink",merek="Lambo",kecepatan="99999")
# print(f"warna = {motor_2.warna}  merek = {motor_2.merek} kecepatan = {motor_2.kecepatan}")

#dekorator
def dekorator(func):
    def wraped():
        print("sebelum dieksekusi")
        func()
        print("sesudah dieksekusi")
    return wraped

@dekorator
def say_hello():
    print("hello world")


say_hello()

#object method
class rudal:
    def __init__(self,merk,ukuran,kecepatan):
        self.merek = merk
        self.ukuran = ukuran
        self.kecepatan = kecepatan

    def tambah_kecepatan(self,nilai):
        self.kecepatan += nilai

rudal_hitam = rudal(merk="Pohong Afrika",ukuran=1000,kecepatan=100)
print(rudal_hitam.__dict__)
rudal_hitam.tambah_kecepatan(100)
print(rudal_hitam.__dict__)

#static method
class hello:
    def __init__(self,nama):
        self.nama  = nama
        print(f"Selamat Datang {nama}")

    @staticmethod
    def Perkenalan():
        print("Hallo saya Someone")

apriw = hello("apriw")

hello.Perkenalan()
hello("apriw")