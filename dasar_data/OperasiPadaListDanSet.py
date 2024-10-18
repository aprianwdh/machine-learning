# untuk menghitung jumlah panjang data
data = [1,2,3,4,5,6,7,8,9,9,1,2,3,4,1,2,3]
print(data)
print(len(data))

# mengubah list menjadi set
print(set(data))

# mengubah list menjadi tupple
print(tuple(data))

# menentukan nilai minimal dan maximal
print(max(data))
print(min(data))

# count (menghitung berapa kali nilai muncul)
var = [1,2,3,4,1,23,412,41,23,241,4,12,421,4,214,14,]
print(var.count(4))#bisa juga mengunakan huruf

# in and not in
kalimat = "I Love My Dream"
print("Dream" in kalimat)
print("Dream" not in kalimat)

# Memberukan nilai pada variabel
anime = ["Hyouka","Slice Of Life","24"]

# cara 1:#
# nama_anime = anime[0]
# genre_anime = anime[1]
# total_episode = anime[2]
#cara 2:#
nama_anime,genre_anime,total_episode = anime

print(f'''
Nama Anime \t= {nama_anime}
Genre \t\t= {genre_anime}
total episode \t= {total_episode}
''')

# mengurutkan data
unsort = [1,3,2,4,6,7,8,11,23,45,12]
unsort.sort()
print(unsort)
# reverse data
unsort.sort(reverse=True)
print(unsort)

misad = [12334,24124,214124]
print(len(misad))



