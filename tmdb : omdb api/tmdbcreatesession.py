import pandas as pd
from imdb import IMDb


df = pd.read_csv('/mnt/data/NetflixViewingHistory-3.csv')


ia = IMDb()


genres = []


for title in df['Title']:
    try:

        movies = ia.search_movie(title)
       
        if movies:
   
            movie = ia.get_movie(movies[0].movieID)
           
            
            movie_genres = movie.get('genres', 'Bilgi Yok')
            genres.append(', '.join(movie_genres)) 
        else:
            genres.append('Dizi/Yer Bulunamadı')  
    except Exception as e:
        genres.append(f'Hata: {str(e)}')  


df['Genre'] = genres

import ace_tools as tools; tools.display_dataframe_to_user(name="Netflix Viewing History with IMDb Genres", dataframe=df)
