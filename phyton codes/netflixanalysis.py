import pandas as pd

df_imdb = pd.read_csv('imdbdata.csv', encoding='ISO-8859-1')

df_imdb['Genres'] = df_imdb['Genres'].str.split(',')

genre_counts = df_imdb['Genres'].explode().value_counts()

print(genre_counts)