import requests
import pandas as pd

API_KEY = 'dde599e590f43753c0e21cae2aa61d80'  # 🔁 Replace this with your TMDB API key
BASE_URL = 'https://api.themoviedb.org/3'

platforms = {
    "Netflix": 213,
    "Hulu": 453,
    "Max": 384,
    "Apple TV+": 2552
}

def fetch_shows(platform_id, platform_name):
    url = f"{BASE_URL}/discover/tv?api_key={API_KEY}&with_networks={platform_id}&sort_by=popularity.desc"
    response = requests.get(url)
    shows = response.json().get('results', [])
    return [
        {
            "title": show["name"],
            "platform": platform_name,
            "rating": show["vote_average"],
            "release_year": show["first_air_date"][:4] if show["first_air_date"] else "Unknown"
        } for show in shows
    ]

all_data = []
for name, id_ in platforms.items():
    all_data.extend(fetch_shows(id_, name))

df = pd.DataFrame(all_data)
df.to_csv('data/shows.csv', index=False)
print("✅ Saved to data/shows.csv")
