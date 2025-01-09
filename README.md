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

## Seeking a correlation with IMDb Ratings
By integrating IMDb ratings, I investigated whether I tended to watch higher-rated shows and movies or if there were outliers that defied this trend.

## Exploring Binge-Watching Habits
I used my Netflix data and seeked for the consecutive days I watched the same series. Then I got their genres from IMDb data to understand which genres capture my attention most.


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


<img width="1470" alt="Screenshot 2025-01-09 at 20 13 27" src="https://github.com/user-attachments/assets/142b40c9-29e2-4c35-bb9a-62eb562b5b99" />

In order to test my hypothesis (H0: there is no correlaton between IMDb ratings and my viewing habits, I wroted the python code imdbratings.py and created a scatter chart. I also calculated the Spearman correlation coefficient, and since it was too small, it was seen that there is really no correlation and we can accept the null hypothesis. 

<img width="1470" alt="Screenshot 2025-01-09 at 20 58 55" src="https://github.com/user-attachments/assets/c00db296-f7ce-4302-9c47-3801b611076a" />

Lastly, I seeked for consecutive days I watched the same show with bingewatching.py, and also visualized this data. I looked for 5 or more consecutive days I watched the same thing. This data showed that, even though I mostly watch genres thriller and drama, I liked to watch comedy and drama consecutively and they capture my attention the most. 
<img width="1470" alt="Screenshot 2025-01-09 at 23 09 47" src="https://github.com/user-attachments/assets/e27b79ed-4ccd-4fe1-a614-fcd50138446f" />



