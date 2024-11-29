# Netflix-usage-analysis
2024-2025 CS210 fall term project

# Motivation
As someone who spends a considerable amount of time on both Netflix and Instagram, in this project, I want to better understand my viewing habits and preferences. This projects aims to analyze my Netflix data to uncover patterns such as:

1) Which genres capture my attention the most?
2) How much time do I spend watching Netflix, and which types of shows or movies keep me engaged the longest?
3) Are there specific behaviors (for example binge-watching) associated with certain genres or times of day?

In addition, I will incorporate my social media activity data to explore whether my social media usage has any notable impact on my Netflix habits. I mainly focus on my Instagram and Twitter usage since I do not use any other social media platform. 

# Data Sources
I have three main sources of data:

## 1) Netflix Viewing Data:
   I obtained data directly from my Netflix account by downloading my Viewing Activity from the accounting settings. This dataset contains a list of titles of shows or movies I have watched, along with the corresponding dates of viewing. Since this data only includes basic information, I am going to enrich it by fetching additional metadata such as genres, IMDb ratings, release years, and other details using the following:
   1) TMDb API: including: Genres, plot summaries, and release years.
   2) OMDb API: additional Movie details such as IMDb ratings and plot descriptions.
   3) IMDb API (not certain) : Can be used for further movie and show information such as cast details.

## 2) Instagram Activity Data:
   I collected the data of my activity on Instagram by using the Data Download feature available on Instagram's settings. This dataset includes my daily acitivity, such as the number of posts and stories. In this project I will mainly focus how much I spent time on Instagram rather than this information, since I am trying to find a correlation between my Instagram time and Netflix habits. 

## 3) Twitter Activity Data:
   Since the Twitter's API doesn't provide direct screen time or usage statistics, I used Screen Time (on IOS) for tracking of my Twitter usage. This will be enough for me since I am dealing with my social media screen time in this project. 

# Data Visualization 
I also aim to visualize my data since it can help me uncover patterns and trends in my Netflix viewing habits, Instagram usage and Twitter activity. I am planning to use a time series graph to see how my watching habits change through time (using matplotlib.)
By creating a bar chart I am aiming to analyze which genres I watch the most and visualize the distribution. Lastly, by using a scatter chart I am planning to analyze the correlation between my socail media screen time and Netflix viewing time. 
