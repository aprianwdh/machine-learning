# # -----------------------for--------------------
# #menggunakan list
# data_list = [1,2,3,4,5,6,7,8,9]
# for i in data_list:print(i)
# #menggunakan range
# for i in range(10):print(i)
# for i in range(1,10,2):print(i)


# # -----------------------while--------------------
# counter = 1
# while counter <= 5:
#     print(counter)
#     counter += 1

# # -----------------------Nasted List--------------------
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)

# # -----------------------Break--------------------
# for huruf in "bismillah s.kom":
#     if huruf == " ":
#         break
#     print(f"huruf saat ini = {huruf}")
    
# # -----------------------countinue--------------------
# for huruf in "bismillah s.kom":
#     if huruf == " ":
#         continue
#     print(f"huruf saat ini = {huruf}")


# # -----------------------else setealh for--------------------
# data = [1,2,3,4,5]

# for i in data:
#     if i == 9:
#         print("angka ditemukan")
#         break
#     else:
#         print("data tidak ditemukan")
#         break

# # -----------------------else setealh while--------------------
# counter = 0
# while counter < 3:
#     print(counter)
#     counter+=1
# else:
#     print("berhenti")

# -----------------------else setealh while--------------------
data1 = [1,2,3,4,5]
data2 = []

for i in data1:
    data2.append(i**2)
print(data2)
