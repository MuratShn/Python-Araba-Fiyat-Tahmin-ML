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


def onehot(isim,index):
 
    le = LabelEncoder()

    a = df[[isim]].values

    a[:,0] = le.fit_transform(df.iloc[:,index])

    ohe = preprocessing.OneHotEncoder()
    a = ohe.fit_transform(a).toarray()
    return a



def main(dfisim):
    ## Vites == Label Encoder 3
    ## Yakıt == Label Encoder 3
    ## CC == Label encoder 4

    print(df.info())
    df.drop_duplicates(subset=["İlanNumara"],inplace=True) ## Tekrar eden veriyi silme
    print("--------------------")
    print(df.info())
    print("--------------")
    print(df["Yakıt"].nunique())
    df.drop(["İlanNumara","İlanTarih"],axis=1,inplace=True)
    print(df.info())
    print(df["CC"].unique())
    df.loc[df['CC']=="Bilmiyorum", 'CC'] = '1300ccvealtı' 
    print("********************")
    print(df)
    print("********************")
    vites = onehot("Vites",3)
    yakıt = onehot("Yakıt",2)
    cc = onehot("CC",4)
    fiyat = df.iloc[:,1].values
    ayıl = df.iloc[:,0].values


    print(df["CC"].unique())
    print(df["Yakıt"].unique())
    print(df["Vites"].unique())
    print(df["CC"].unique())
    df.drop(["Vites","Yakıt","CC"],axis=1,inplace=True)

    geri = df.iloc[:,0:].values
    print(yakıt)
    s = pd.DataFrame(data=vites,columns=["Düz","Otomatik","YarıOtomatik"])
    s2 = pd.DataFrame(data=yakıt,columns=["Benzin","Benzin/Lpg","Dizel"])
    s3 = pd.DataFrame(data=cc,columns=['1300ccvealtı','1301-1600cc','1601-1800cc','1801-2000cc','2001-2500cc','3501-4000cc','6001ccveüzeri'])
    s4 = pd.DataFrame(data=fiyat,columns=["Fiyat"])
    s5 = pd.DataFrame(data=ayıl,columns=["ArabaYıl"])

    ss = pd.concat([s,s2],axis=1)
    ss2 = pd.concat([ss,s3],axis=1)
    ss3 = pd.concat([ss2,s5],axis=1)
    sonuc = pd.concat([ss3,s4],axis=1)
    
    sonuc.to_csv(f"{dfisim}.csv")



    
düzenle("Volkswagen-polo-satılmıs.txt")
düzenle("Volkswagen-polo-satılmamıs.txt") 
    
df = pd.DataFrame({"İlanNumara":iNo,
                   "İlanTarih":iTarih,
                   "ArabaYıl":aYıl,
                   "Fiyat":f,
                   "Yakıt":y,
                   "Vites":v,
                   "CC":c})


main("Volkswagen-polo")


## düzenle = Fiat-egea-satılmıs.txt
## düzenle = Fiat-egea-satılmamıs.txt
## main = Fiat-Egea


## düzenle = Ford-Focus-satılmıs.txt
## düzenle = Ford-Focus-satılmamıs.txt
## main = Ford-Focus


## düzenle = Volkswagen-golf-satılmıs.txt
## düzenle = Volkswagen-golf-satılmamıs.txt
## main = Volkswagen-golf


## düzenle = Volkswagen-polo-satılmıs.txt
## düzenle = Volkswagen-polo-satılmamıs.txt
## main = Volkswagen-polo
