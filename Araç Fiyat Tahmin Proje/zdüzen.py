import pandas as pd 
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder


iNo=[]
iTarih=[]
aYıl=[]
f=[]
y=[]
v=[]
c=[]
km = []

def düzenle(dosyadi):
    icerik=[]
    with open(dosyadi,"r",encoding="UTF-8") as file:
        
        for i in file.readlines():
            icerik.append(i.split(","))

    for i in icerik:
        iNo.append(int(i[0]))
        iTarih.append((i[1]))
        aYıl.append(int(i[2]))
        f.append(float(i[3]))
        y.append((i[4]))
        v.append(i[5])
        c.append(i[6])
        km.append(float(i[7]))
        
        
düzenle("Volkswagen-polo-satılmıs.txt")
düzenle("Volkswagen-polo-satılmamıs.txt")



df = pd.DataFrame({"İlanNumara":iNo,
                   "İlanTarih":iTarih,
                   "ArabaYıl":aYıl,
                   "Fiyat":f,
                   "Yakıt":y,
                   "Vites":v,
                   "CC":c,
                   "Km":km
                   })



df.drop_duplicates(subset=["İlanNumara"],inplace=True) ## Tekrar eden veriyi silme
df.loc[df['CC']=="Bilmiyorum", 'CC'] = '1300ccvealtı' 
print("********************")
print(df)
print("********************")
fiyat = df.iloc[:,1].values
ayıl = df.iloc[:,0].values


print(df["CC"].unique())
print(df["Yakıt"].unique())
print(df["Vites"].unique())
print(df["CC"].unique())
df.drop(["Vites","Yakıt","CC"],axis=1,inplace=True)


Kmm = df.iloc[:,4].values

df2 = pd.read_csv("Volkswagen-polo.csv")
df2.rename(columns={'Fiyat':'Km'}, inplace=True)
print(df2)
df2["Fiyat"] = Kmm
df2 = df2.loc[:, ~df2.columns.str.contains('^Unnamed')]
df2.rename(columns={'Km': 'Fiyat', 'Fiyat': 'Km'}, inplace=True)
df2.to_csv("Volkswagen-polo.csv")
