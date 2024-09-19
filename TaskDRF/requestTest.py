import requests

# Giriş URL'si
login_url = "http://localhost:8000/api/auth/login/"  # Gerçek host'unuzu burada kullanın

# Kullanıcı kimlik bilgileri
payload = {
    "username": "mert",  # Gerçek kullanıcı adınızı buraya yazın
    "password": "mert"   # Gerçek şifrenizi buraya yazın
}

# Başlıklar
headers = {
    "Content-Type": "application/json"
}

# Giriş isteği gönder
response = requests.post(login_url, json=payload, headers=headers)
token=""
# Yanıtı kontrol et
if response.status_code == 200:
    response_data = response.json()
    # Token'ı yanıt verilerinden alın
    token = response_data.get('key')  # veya 'token', API'nizin döndürdüğü anahtara bağlı olarak
    print("Token:", token)
else:
    print("Giriş başarısız:", response.status_code, response.text)





# Korunan kaynak URL'si
protected_url = 'http://127.0.0.1:8000/api/user/'

# Yetkilendirilmiş istek yapmak için başlıkları güncelleyin
auth_headers = {
    "Authorization": f"Token {token}",  # Token'ı Authorization başlığına ekleyin
    "Content-Type": "application/json"
}

# GET isteği gönder
response = requests.get(protected_url, headers=auth_headers)

# Yanıtı kontrol et
if response.status_code == 200:
    print("Başarılı:", response.json())
else:
    print("Hata:", response.status_code, response.text)




import requests

# Çıkış URL'si
logout_url = "http://localhost:8000/api/auth/logout/"

# Başlıklar (Token'ı ekleyin)
auth_headers = {
    "Authorization": f"Token {token}",  # Token'ı buraya ekleyin
    "Content-Type": "application/json"
}

# Çıkış isteği gönder
response = requests.post(logout_url, headers=auth_headers)

# Yanıtı kontrol et
if response.status_code == 200:
    print("Çıkış başarılı")
else:
    print("Çıkış başarısız:", response.status_code, response.text)
