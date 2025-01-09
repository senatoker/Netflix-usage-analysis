import pandas as pd
import matplotlib.pyplot as plt


file_path = 'NetflixViewingHistory-3.csv'
df_netflix = pd.read_csv(file_path)


df_netflix['Date'] = pd.to_datetime(df_netflix['Date'], format='%d.%m.%Y')


df_netflix['Title'] = df_netflix['Title'].str.split(':').str[0]


df_netflix = df_netflix.sort_values(by='Date')


df_netflix['Previous_Title'] = df_netflix['Title'].shift(1)  
df_netflix['Previous_Date'] = df_netflix['Date'].shift(1)    


df_netflix['Consecutive'] = (df_netflix['Title'] == df_netflix['Previous_Title']) & \
                            (df_netflix['Date'] - df_netflix['Previous_Date']).dt.days == 1


df_netflix['Consecutive_Count'] = df_netflix.groupby('Title').cumcount() + 1


df_netflix['Group'] = (df_netflix['Title'] != df_netflix['Previous_Title']).cumsum()


long_binge_titles = df_netflix[df_netflix['Consecutive_Count'] >= 5]


if long_binge_titles.empty:
    print("Could not found.")
else:

    df_imdb = pd.read_csv('imdbdata.csv', encoding='ISO-8859-1')
    df_imdb['Genres'] = df_imdb['Genres'].str.split(', ')

    def get_genres(title):
        genres = df_imdb[df_imdb['Title'] == title]['Genres'].values
        return genres[0] if len(genres) > 0 else None

    long_binge_titles['Genres'] = long_binge_titles['Title'].apply(get_genres)

 
    genre_counts = long_binge_titles['Genres'].explode().value_counts()


    if genre_counts.empty:
        print("Could not found.")
    else:

        fig, ax = plt.subplots(figsize=(12, 8))  
        genre_counts.plot(kind='bar', color='lightseagreen', ax=ax)

      
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='right')

    
        ax.set_title('Genres watched for 5 or more consecutive days')
        ax.set_xlabel('Genre')
        ax.set_ylabel('Days watched')

      
        ax.set_ylim(0, genre_counts.max() + 1)


        plt.tight_layout()
        plt.show()


    binge_results = long_binge_titles[['Title', 'Consecutive_Count', 'Genres']].drop_duplicates()
    print(f"Series:\n{binge_results}")