def mencari_luas_segitiga(alas,tinggi):
    hasil = 1/2*alas*tinggi
    return hasil



#-----------menggunakan keyword only----------
def greating(*,nama,pesan):
    '''
    keyword only mengharuskan kita menuliskan nama="...." dan pesan="......"
    '''
    return f'halo {nama} {pesan}' 



#----------------mengguakan positional only-----------------
def great(nama,pesan,/):
    '''
    mengharuskan kita mematuhi urutan parameter
    '''
    return f"halo {nama} {pesan}"


#----------------Var-Positional (Variadic Positional Parameter---------------
def penjumlahan(*args):
    total = sum(args)
    return total


# --------------Var-Keyword (Variadic Keyword Parameter------------
def kwargs(**kwargs):
    '''
    Parameter ini dapat menampung jumlah keyword argument yang bervariasi saat pemanggilan fungsi. 
    '''
    info = ''
    for key,value in kwargs.items():
        info += f"{key} : {value}\n"
    return info
    

#-----------Lambda Function------------------------
mencari_keliling = lambda panjang,lebar : 2*(panjang+lebar)

if __name__ == "__main__":
    print(mencari_luas_segitiga(10,12))
    print(greating(nama="api",pesan="yu ken dudis"))
    print(great("widi","to be rich or die"))
    print(penjumlahan(1,2))
    print(kwargs(key = "aku",value = "kamu"))
    print(mencari_keliling(10,12))

