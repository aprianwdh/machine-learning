import numpy as np

# matriks = np.array([[13,2,34,56],
#                     [16,3,65,43],
#                     [3,4,34,45]])

# print(matriks[2,1])

# # data = np.array([0 for i in range(5)] for j in range(3))
# # print(data)

# #-----------------Perkalian pada matriks dengan angka skalar-----------------
# hasil = matriks * 2
# print(hasil)
# #atau
# hasil = np.multiply(matriks,2)

#------------------perkalian matriks kali matriks--------------------------

data1 = np.array([[4,5],
                 [2,6]])
data2 = np.array([[1,2],
                 [3,4]])

hasil = np.dot(data1,data2)
print(hasil)