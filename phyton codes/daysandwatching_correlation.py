import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

# Load the CSV file
file_path = 'NetflixViewingHistory-3.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Convert the 'Date' column to datetime format and add the day of the week
data['Date'] = pd.to_datetime(data['Date'], format='%d.%m.%Y')
data['DayOfWeek'] = data['Date'].dt.day_name()

# Count the number of views per day of the week
day_counts = data['DayOfWeek'].value_counts().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
)

# Chi-square test for independence
observed = day_counts.values
expected = [sum(observed) / 7] * 7  # Assuming equal distribution across days
chi2, p_value, _, _ = chi2_contingency([observed, expected])

# Plot the data
plt.figure(figsize=(10, 6))
sns.barplot(x=day_counts.index, y=day_counts.values, palette="viridis")
plt.title("Number of Views by Day of the Week")
plt.xlabel("Day of the Week")
plt.ylabel("Number of Views")
plt.xticks(rotation=45)

# Annotate the plot with the p-value
p_text = f"P-value: {p_value:.2e}"  # Scientific format
plt.text(0.5, max(day_counts.values) * 0.9, p_text, fontsize=12, color='red', ha='center')

plt.show()

# Print results to the console
print("View Counts by Day of the Week:")
print(day_counts)
print("\nChi-square Test Results:")
print(f"Chi2 Value: {chi2:.2f}")
print(f"P-value: {p_value:.2e}")

# Hypothesis test conclusion
alpha = 0.05
if p_value < alpha:
    print("\nConclusion: There is a significant relationship between days of the week and viewing habits (p < 0.05).")
else:
    print("\nConclusion: There is no significant relationship between days of the week and viewing habits (p >= 0.05).")
