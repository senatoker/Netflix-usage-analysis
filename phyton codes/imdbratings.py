import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np


df_imdb = pd.read_csv('imdbdata.csv', encoding='ISO-8859-1')


df_imdb['IMDb Rating'] = pd.to_numeric(df_imdb['IMDb Rating'], errors='coerce')


rating_counts = df_imdb.groupby('IMDb Rating').size()


spearman_corr, p_value_spearman = stats.spearmanr(rating_counts.index, rating_counts.values)


print(f"Spearman Correlation: {spearman_corr}")
print(f"p-value: {p_value_spearman}")


plt.figure(figsize=(10, 6))
plt.scatter(rating_counts.index, rating_counts.values, color='skyblue', alpha=0.7)


plt.text(0.5, 0.1, f"Spearman Correlation = {spearman_corr:.4f}", ha='center', va='center', transform=plt.gca().transAxes, fontsize=12)


plt.title('Correlation IMDb ratings and Watching Habits')
plt.xlabel('IMDb Ratings')
plt.ylabel('Series/Movie Count')


plt.xticks(np.arange(min(rating_counts.index), max(rating_counts.index)+0.1, 0.1), rotation=45)

plt.tight_layout()
plt.show()