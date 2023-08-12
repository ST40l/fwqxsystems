import requests
from bs4 import BeautifulSoup

def get_internet_data(il):
    url = f"https://www.harita.gov.tr/sunum/{il}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        # İnternet sayfasındaki ilgili veriyi burada çekebilirsiniz
        # Örnek olarak başlığı çekelim:
        title = soup.title.text
        return title
    else:
        return f"Sayfaya erişilemiyor. Hata kodu: {response.status_code}"

il = input("Bir il adı girin: ")
veri = get_internet_data(il)
print("İnternet Verisi:", veri)
