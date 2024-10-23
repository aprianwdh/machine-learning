#Pandas adalah library populer yang digunakan untuk pengelolaan dan analisis data. 
# Library ini menyediakan struktur data dan alat untuk membantu
#  pengguna dalam melakukan manipulasi, pembersihan, 
# transformasi, dan analisis data dengan mudah dan efisien.

import pandas as pd

Data = {
    "Nama":["Aprian","Budi","Siregar"],
    "Tier":["Absolut Demon","Keroco","keroco"],
    "Merek Hp":["SAmsung 16 pro","Kingfinik","Oddo"]
}

df = pd.DataFrame(Data)
print(df)