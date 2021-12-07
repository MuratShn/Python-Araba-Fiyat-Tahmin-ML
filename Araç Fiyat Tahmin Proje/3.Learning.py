from numpy.core.records import array
import pandas as pd     
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression

#km fiyat oluyo

df = pd.read_csv("Fiat-Egea.csv")
fiyat = df["Km"].values

df = (df[(df["Km"]>30.0)& (df["Km"]<499.0)])

"""sns.relplot(
    data=fiyat
)
plt.show()
"""
df = df.apply(pd.to_numeric)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

x = (df.iloc[:,0:12])
y = df.iloc[:,12]



from sklearn.preprocessing import PolynomialFeatures
X = x.values

Y = y.values

print((X[0]))
t = [1	,0	,0	,0	,0	,1	,1	,0	,0,	0	,2017	,52]


poly_reg = PolynomialFeatures(degree=2) #2 dereceden polinom objesi olustur
x_poly = poly_reg.fit_transform(X) #degerlere üst eklıyo degreyı kac verıresek x^0 dan x^deggreye kadar verileri polinomal dünyaya ceviriyoruz
lr2 = LinearRegression()
lr2.fit(x_poly,y)


print("""
      ---------------
      Arabanız düz Vites ise = 1
      Otomatik ise = 2
      Manuel ise = 3
      ---------------
      """
      )
a1 = int(input())

print("""
      ---------------
      Arabanız Dizel ise = 1
      Benzin/Lpg ise = 2
      Benzin = 3
      ---------------
      """
      )
a2=int(input())

print("""
      ---------------
      Arabanız 1300vealtı ise = 1
      1601-1800 ise = 2
      1301-1600 ise = 3
      6000veüzeri ise = 4
      ---------------
      """
      )
a3 = int(input())

a4 = int(input("Arabanın Yılı kaç //2017:  "))

a5 = float(input("Araba kaç km'de // 150.0:  "))

tahmin = []

if a1 == 1:
    tahmin.append(1)
    tahmin.append(0)
    tahmin.append(0)
elif a1==2:
    tahmin.append(0)
    tahmin.append(1)
    tahmin.append(0)
elif a1==3:
    tahmin.append(0)
    tahmin.append(0)
    tahmin.append(1)
    
if a2 == 1:
    tahmin.append(1)
    tahmin.append(0)
    tahmin.append(0)
elif a2==2:
    tahmin.append(0)
    tahmin.append(1)
    tahmin.append(0)
elif a2==3:
    tahmin.append(0)
    tahmin.append(0)
    tahmin.append(1)

if a3 == 1:
    tahmin.append(1)
    tahmin.append(0)
    tahmin.append(0)
    tahmin.append(0)
elif a3==2:
    tahmin.append(0)
    tahmin.append(1)
    tahmin.append(0)
    tahmin.append(0)
elif a3==3:
    tahmin.append(0)
    tahmin.append(0)
    tahmin.append(1)
    tahmin.append(0)
elif a3==4:
    tahmin.append(0)
    tahmin.append(0)
    tahmin.append(0)
    tahmin.append(1)

tahmin.append(a4)
tahmin.append(a5)
print(tahmin)

sonuc = (lr2.predict(poly_reg.fit_transform([tahmin])))

print(f"Tahmini Fiyat : {sonuc}")












## Düz = 1,0,0
## Otomatik = 0,1,0
## Yarı Otomatik = 0,0,1

## Dizel = 1,0,0
## Benzin/Lpg = 0,1,0
## Benzin = 0,0,1

## 1300vealtı = 1,0,0,0 
## 1601-1800 = 0,1,0,0
## 1301-1600 = 0,0,1,0
## 6000veüzeri = 1,0,0,1

#