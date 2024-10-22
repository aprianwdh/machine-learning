arr = []

n = int(input("masukkan jumlah list = "))

for i in range(0,n):
    arr.append(input("masukkan kata = "))

search = input("kata uang ingin dicari = ")

print(arr.count(search))