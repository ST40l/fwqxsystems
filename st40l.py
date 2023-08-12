import requests
from bs4 import BeautifulSoup

def get_city_data(city_name):
    base_url = "https://www.harita.gov.tr/sunum/"
    params = {"ilAdi": city_name}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Verilerin çekilmesi ve işlenmesi burada yapılabilir
        # Örnek olarak, istediğiniz veriyi çekip gösterebilirsiniz
        data = soup.find("div", class_="veri").get_text()

        return data
    else:
        return "Hata: İstek yapılamadı veya geçersiz cevap alındı."

if __name__ == "__main__":
    city_name = input("Bir il adı girin: ")
    city_data = get_city_data(city_name)
    print(city_data)
