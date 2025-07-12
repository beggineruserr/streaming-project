import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv('data/shows.csv')
df = df.dropna()

# Bar chart – Average rating by platform
avg_ratings = df.groupby('platform')['rating'].mean().sort_values(ascending=False)
plt.figure(figsize=(8,5))
avg_ratings.plot(kind='bar', color='skyblue')
plt.title('Average Show Rating by Platform')
plt.ylabel('Average Rating')
plt.xlabel('Platform')
plt.tight_layout()
plt.savefig('data/avg_rating_by_platform.png')
plt.show()

# Line chart – Average rating over time by platform
df = df[df['release_year'] != 'Unknown']
df['release_year'] = df['release_year'].astype(int)

year_platform_avg = df.groupby(['release_year', 'platform'])['rating'].mean().reset_index()
plt.figure(figsize=(10,6))
for platform in df['platform'].unique():
    subset = year_platform_avg[year_platform_avg['platform'] == platform]
    plt.plot(subset['release_year'], subset['rating'], label=platform)

plt.title('Average Rating Over Time by Platform')
plt.xlabel('Release Year')
plt.ylabel('Average Rating')
plt.legend()
plt.tight_layout()
plt.savefig('data/ratings_over_time.png')
plt.show()
