class Mobil:
    def __init__(self,merk,Kecepatan,warna):
        self.merk = merk
        self.kecepatan = Kecepatan
        self.warna = warna
    def tambah_kecepatan(self,nilai):
        self.kecepatan += nilai

Supra_Bapak = Mobil(Kecepatan=1000,merk="supra batoks",warna="hitam legam")
print(Supra_Bapak.__dict__)

class Mobil_sport(Mobil):
    def Nitro(self):
        self.kecepatan += 10000
    def tambah_kecepatan(self,nilai):
        super().tambah_kecepatan(nilai)
        print("Kecepatan Bertambah")

Supra_Balap = Mobil_sport(merk="Supra Racing Hell",Kecepatan=1001,warna="Merah Neraka")
Supra_Balap.Nitro()
Supra_Balap.Nitro()
Supra_Balap.tambah_kecepatan(nilai=100)
print(Supra_Balap.__dict__)