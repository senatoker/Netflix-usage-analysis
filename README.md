# Netflix-usage-analysis
2024-2025 CS210 fall term project

# Motivation
As someone who spends a considerable amount of time on both Netflix and Instagram, in this project, I want to better understand my viewing habits and preferences. This projects aims to analyze my Netflix data to uncover patterns such as:

1) Which genres capture my attention the most?
2) Is there a correlation between my watching habits and IMDb ratings?
3) Are there specific behaviors (for example binge-watching) associated with certain genres?

# Data Sources
I have three main sources of data:

## 1) Netflix Viewing Data:
   I obtained data directly from my Netflix account by downloading my Viewing Activity from the accounting settings. This dataset contains a list of titles of shows or movies I have watched, along with the corresponding dates of viewing. Since this data only includes basic information, I am going to enrich it by fetching additional metadata such as genres, IMDb ratings, release years, and other details using the following:
   1) TMDb API: including: Genres, plot summaries, and release years.
   2) OMDb API: additional Movie details such as IMDb ratings and plot descriptions.
   3) IMDb API: Can be used for further movie and show information such as cast details.

I got a raw data from the Netflix website, and this data was including the movie/show names and dates only. First I cleaned the data and extracted the rows irrelevant  to me (my parents were also using my account, and I only used my own data. Then I tried to get the genres from TMDB and OMDB API's but they did not work. (I still added the codes I wrote to my repository.) 

# Data Visualization 
I also aim to visualize my data since it can help me uncover patterns and trends in my Netflix viewing habits. I am planning to use a time series graph to see how my watching habits change through time (using matplotlib.)
By creating a histogram I am aiming to analyze which genres I watch the most and visualize the distribution.
