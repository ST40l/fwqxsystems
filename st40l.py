import requests
from bs4 import BeautifulSoup

il = input("Bir il girin: ").lower()

url = f"https://www.harita.gov.tr/iller/{il}.html"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    
    internet_sayisi = soup.find("div", class_="InternetSayisi")
    
    if internet_sayisi:
        internet_sayisi = internet_sayisi.get_text()
        turksat = "Türksat" in internet_sayisi
        turktelekom = "Türk Telekom" in internet_sayisi
        turkcell = "Turkcell" in internet_sayisi
        
        print(f"{il.capitalize()} ilindeki internet sayısı: {internet_sayisi}")
        
        if turksat:
            print("Türksat internet hizmeti mevcut.")
        if turktelekom:
            print("Türk Telekom internet hizmeti mevcut.")
        if turkcell:
            print("Turkcell internet hizmeti mevcut.")
    else:
        print("İnternet sayısı bilgisi bulunamadı.")
else:
    print("İl bulunamadı veya sayfaya erişim sağlanamadı.")
