from bs4 import BeautifulSoup as bs
import requests

## Linea Polo Golf Jetta Passat Focus Egea
"""
https://www.araba.com/otomobil/fiat-egea?sayfa=1 -
https://www.araba.com/otomobil/ford-focus?sayfa=1 -
https://www.araba.com/otomobil/volkswagen-polo?sayfa=1 -
https://www.araba.com/otomobil/volkswagen-golf?sayfa=1 -
https://www.araba.com/otomobil/volkswagen-jetta?sayfa=1
https://www.araba.com/otomobil/volkswagen-passat?sayfa=1

"""
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
    
ino = []
attrs2=[] ## satılmamıs arabalar ıcın
sattrs = [] ##satılmış arabalar için 

def ilanNo():
    aLink = soup.find_all(("tr",{"class": "table-row     "})) ##Arac linkini alıyoruz
    for i in aLink:
        s = (str)(i.get('data-href'))
        s = s[(s.rfind("-")+1):]
        if s!="None":
            ino.append(s)


def satılmısAracBilgi():
    sayac = 1 
    price = soup.find("div",{"class": "offer-price"}).text
    price = price.strip('# ')
    price = price.replace(" ","")
    price = price.replace("\n","") 
    
    for i in soup.find_all("td"):  ## Araba satılmıs ıse
        if(sayac%2==0 and sayac<16):
            i = str(i.text)
            i = i.strip('# ')
            i = i.replace(" ","")
            i = i.replace("\n","")         
            sattrs.append(i)
        sayac +=1
    sattrs.append(price)

def satılmamısAracBilgi():
    attrs=[]
    price = soup.find("span",{"class": "offer-price"}).text
    price = price.strip('# ')
    price = price.replace(" ","")
    price = price.replace("\n","") 
    
    for i in soup.find_all("span",{"class": "item-text"}): ## satılmayan araclar
        
        i = str(i.text)
        i = i.strip('# ')
        i = i.replace(" ","")
        i = i.replace("\n","") 
        attrs.append(i)


    attrs2.append(attrs[0])
    attrs2.append(attrs[1])
    attrs2.append(attrs[5])
    attrs2.append(attrs[6])
    attrs2.append(attrs[7])
    attrs2.append(attrs[8])
    attrs2.append(attrs[9])
    attrs2.append(price)


for i in range(30,44):
    url = f"https://www.araba.com/otomobil/volkswagen-golf?sayfa={i}"
    print(url)
    response = requests.get(url,headers=headers)
    soup = bs(response.content,"html.parser")
    ilanNo()

for j in ino:
    url = f"https://www.araba.com/ilan/{j}"
    response = requests.get(url,headers=headers)
    soup = bs(response.content,"html.parser")
    selled = soup.find("div",{"class": "sold-text"})
    if selled:
        ##satılmıs araba
        satılmısAracBilgi()
    else:
        ##satılmamıs araba
        satılmamısAracBilgi()
    
##Verileri metin belgesine kopylama

with open("Volkswagen-golf-satılmamıs.txt","a",encoding="UTF-8") as file:
    sayac = 0
    for j in attrs2:
        file.write(j+",")
        sayac +=1
        if sayac == 8:
            file.write("\n")
            sayac = 0

with open("Volkswagen-golf-satılmıs.txt","a",encoding="UTF-8") as file:
    sayac = 0
    for k in sattrs:
        file.write(k+",")
        sayac +=1
        if sayac == 8:
            file.write("\n")
            sayac = 0