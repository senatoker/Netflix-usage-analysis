import requests
import pandas as pd


api_key = 'bbe924b'


df = pd.read_csv('./data/NetflixViewingHistory-3.csv')


genres = []


for title in df['Title']:

    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
    response = requests.get(url)
   
    if response.status_code == 200:
        data = response.json()
       

        if 'Genre' in data:
            genres.append(data['Genre'])
        else:
            genres.append('Bilgi Yok')  
    else:
        genres.append('Hata') 


df['Genre'] = genres


import ace_tools as tools; tools.display_dataframe_to_user(name="Netflix Viewing History with Genres", dataframe=df)
