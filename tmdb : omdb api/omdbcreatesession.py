import requests
import pandas as pd

# OMDb API anahtarınızı buraya ekleyin
api_key = 'bbe924b'

# Netflix verisini yükleyelim
df = pd.read_csv('./data/NetflixViewingHistory-3.csv')

# Tür bilgilerini depolayacak bir liste oluşturuyoruz
genres = []

# Her bir başlık için OMDb API'yi sorgulayacağız
for title in df['Title']:
    # API isteğini yapalım
    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
    response = requests.get(url)
   
    if response.status_code == 200:
        data = response.json()
       
        # Eğer tür bilgisi varsa ekleyelim
        if 'Genre' in data:
            genres.append(data['Genre'])
        else:
            genres.append('Bilgi Yok')  # Eğer genre bilgisi yoksa
    else:
        genres.append('Hata')  # Eğer API isteği başarısız olduysa

# Genre verisini DataFrame'e ekleyelim
df['Genre'] = genres

# Sonuçları gösterelim
import ace_tools as tools; tools.display_dataframe_to_user(name="Netflix Viewing History with Genres", dataframe=df)