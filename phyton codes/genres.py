import matplotlib.pyplot as plt


genre_counts = {
    "Thriller": 73,
    "Drama": 71,
    "Mystery": 53,
    "Comedy": 49,
    "Romance": 35,
    "Sci-Fi": 32,
    "Fantasy": 29,
    "Action": 24,
    "Crime": 22,
    "Adventure": 20,
    "Family": 14,
    "Horror": 11,
    "Animation": 10,
    "History": 6,
    "Biography": 4,
    "War": 3,
    "Music": 2,
    "Short": 1,
    "Documentary": 1,
    "Reality-TV": 1
}


import pandas as pd
genre_df = pd.DataFrame(list(genre_counts.items()), columns=["Genre", "Count"])


genre_df = genre_df.sort_values(by="Count", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(genre_df["Genre"], genre_df["Count"], color='skyblue')
plt.title('Top Genres')
plt.xlabel('Genres')
plt.ylabel('Times watched')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()