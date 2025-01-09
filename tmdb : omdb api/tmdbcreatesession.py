import pandas as pd
from imdb import IMDb

# Netflix verisini yükleyelim
df = pd.read_csv('/mnt/data/NetflixViewingHistory-3.csv')

# IMDb bağlantısını başlatıyoruz
ia = IMDb()

# Tür bilgilerini depolayacak bir liste oluşturuyoruz
genres = []

# Her bir başlık için IMDb'den tür bilgisi alacağız
for title in df['Title']:
    try:
        # IMDb'den başlık bilgisi al
        movies = ia.search_movie(title)
       
        if movies:
            # İlk sonucu alalım (genellikle doğru başlık ilk sıradadır)
            movie = ia.get_movie(movies[0].movieID)
           
            # Tür bilgilerini alalım
            movie_genres = movie.get('genres', 'Bilgi Yok')
            genres.append(', '.join(movie_genres))  # Türleri virgülle ayıralım
        else:
            genres.append('Dizi/Yer Bulunamadı')  # Başlık bulunamazsa
    except Exception as e:
        genres.append(f'Hata: {str(e)}')  # Hata durumunda bilgi ekleyelim

# Genre verisini DataFrame'e ekleyelim
df['Genre'] = genres

# Sonuçları gösterelim
import ace_tools as tools; tools.display_dataframe_to_user(name="Netflix Viewing History with IMDb Genres", dataframe=df)