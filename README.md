# Netflix-usage-analysis
2024-2025 CS210 fall term project

# Motivation
As someone who spends a considerable amount of time on both Netflix and Instagram, in this project, I want to better understand my viewing habits and preferences. This projects aims to analyze my Netflix data to uncover patterns such as:

1) Which genres capture my attention the most?
2) Is there a correlation between my watching habits and IMDb ratings?
3) Are there specific behaviors (for example binge-watching) associated with certain genres?
4) Is there a correlation the between days of the week and watching habits?

# Data Sources
I have three main sources of data:

## Netflix Viewing Data:
   I obtained data directly from my Netflix account by downloading my Viewing Activity from the accounting settings. This dataset contains a list of titles of shows or movies I have watched, along with the corresponding dates of viewing. Since this data only includes basic information, I am going to enrich it by fetching additional metadata such as genres, IMDb ratings, release years, and other details using the following:
   1) TMDb API: including: Genres, plot summaries, and release years.
   2) OMDb API: additional Movie details such as IMDb ratings and plot descriptions.
   3) IMDb API: Can be used for further movie and show information. 

I got a raw data from the Netflix website, and this data was including the movie/show names and dates only. I tried to get the genres from TMDB and OMDB API's but they did not work. (I still added the codes I wrote to my repository.) Then I decided to use the metadata of IMDb in order to get genres. I merged the data I got from Netflix website and IMDb metdata and it gave me the exported file imdbdata.csv.

# Data Cleaning and Organization

## Removing irrelevant entries 
I filtered the data to isolate only my activity. My parentes were also using the same Netflix account but after organizing it, I only used my own data.

## Handling Duplicates
Duplicate rows were removed to prevent over-representation of certain entries and maintain the integrity of the data.

## Dealing with Missing or Incomplete Data
Rows with missing or incomplete information, such as movies or shows without genres, were either corrected (when possible) or excluded from the dataset to maintain its quality.

## Handling the Genres Column
Since many entries had multiple genres listed ("Drama, Thriller"), I split these entries into separate categories. This allowed for more detailed analysis by treating each genre independently.

# Hypothesis Formation
Once the data was cleaned and organized, I began preparing it to test my hypothesis regarding my viewing habits:

## Exploring Genre Preferences
Using the cleaned dataset, I categorized the genres I watched most frequently. I calculated percentages for each genre and identified any dominant categories in my viewing history.

## Seeking for a Correlation with IMDb Ratings
By integrating IMDb ratings, I investigated whether I tended to watch higher-rated shows and movies or if there were outliers that defied this trend.

## Exploring Binge-Watching Habits
I used my Netflix data and seeked for the consecutive days I watched the same series. Then I got their genres from IMDb data to understand which genres capture my attention most.

## Seeking for a Correlation Between the Days of the Week and Watching Habits
To uncover patterns in my viewing habits, I analyzed the relationship between the days of the week and the number of shows or movies I watched. The goal was to determine whether specific days exhibited higher or lower viewing activity and if there were any statistically significant differences across the week. This analysis aimed to identify potential correlations and trends that could reveal how my watching behavior varies depending on the day.

# Data Visualization 
First with netflixanalysis.py, I obtained a list of genres their counts in my viewving data: "Thriller": 73,
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
    "Reality-TV": 1.
Then, I used this data to create a bar chart that shows the frequencies of different genres I watched in Netflix (genres.py). Here is the bar chart:

<img width="1466" alt="Screenshot 2025-01-09 at 20 13 27" src="https://github.com/user-attachments/assets/11c77ab6-642a-4ac5-bfe2-8be4a3291b08" />

In order to test my hypothesis.
H0: there is no correlaton between IMDb ratings and my viewing habits.
I wroted the python code imdbratings.py and created a scatter chart. I also calculated the Spearman correlation coefficient, and since it was too small (0.23), it was seen that there is no any significant correlation between rating and my watching habits and we can accept the null hypothesis. 

<img width="1460" alt="Screenshot 2025-01-09 at 20 58 55" src="https://github.com/user-attachments/assets/e8def0e5-3180-4718-9931-2bd5c4854d09" />

Other than that, I seeked for consecutive days I watched the same show with bingewatching.py, and also visualized this data. I looked for 5 or more consecutive days I watched the same thing. This data showed that, even though I mostly watch genres thriller and drama, I liked to watch comedy and drama consecutively and they capture my attention the most. 

<img width="1463" alt="Screenshot 2025-01-09 at 23 09 47" src="https://github.com/user-attachments/assets/0311af51-9760-4544-81e9-031fa0b838c6" />

Lastly, to analyze the relationship between the days of the week and my viewing habits, I plotted a bar graph showing the number of views for each day of the week. The x-axis represents the days (Monday to Sunday), while the y-axis represents the number of views.
H0: There is no correlation between the days of the week and my watching habits. 
To test the hypothesis, a Chi-Square test for independence was performed, comparing the observed number of views with an expected uniform distribution (equal views for each day). Since the calculated p-value is 0.02, which is less than the significance level 0.05, I concluded that the difference was not by chance and I can reject the null hypothesis. (i.e, days and viewing habits are dependent. 

<img width="1099" alt="Screenshot 2025-01-10 at 16 53 40" src="https://github.com/user-attachments/assets/57363db3-9147-4431-bb2d-bf8abcdc777a" />
