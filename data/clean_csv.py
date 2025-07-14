import pandas as pd

df = pd.read_csv('data/shows.csv')

clean_df = df[['title', 'platform', 'rating', 'release_year']]

clean_df = clean_df.dropna()

clean_df.to_csv('data/shows_clean.csv', index=False)

print("Saved shows_clean.csv successfully.")
