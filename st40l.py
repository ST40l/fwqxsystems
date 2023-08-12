import requests

def get_data(api_url, params):
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()  # Gelen veriyi JSON formatından Python nesnesine çeviriyoruz
        return data
    else:
        return None

il = input("Bir il adı girin: ")
url = f"https://www.harita.gov.tr/sunum/{il}"

# İnternet verisi için istek
internet_params = {
    "il": il
}
internet_veri = get_data(url, internet_params)  # api_url yerine url kullanmalısınız

if internet_veri:
    internet_degeri = internet_veri.get("internet_verisi")
    
    if internet_degeri is not None:
        print(f"{il} ilindeki internet verisi: {internet_degeri}")
    else:
        print(f"{il} iline ait internet verisi bulunamadı.")
else:
    print(f"{il} için internet verisi çekilemedi veya hata oluştu.")

# IP adresleri için istek
ip_params = {
    "il": il
}
ip_veri = get_data(url, ip_params)  # api_url yerine url kullanmalısınız

if ip_veri:
    ip_listesi = ip_veri.get("ip_list")
    
    if ip_listesi:
        print(f"{il} iline ait IP adresleri:")
        for ip in ip_listesi:
            print(ip)
    else:
        print(f"{il} iline ait IP adresi bilgisi bulunamadı.")
else:
    print(f"{il} için IP adresi verisi çekilemedi veya hata oluştu.")
