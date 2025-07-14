import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt

df = pd.read_csv('data/shows.csv')
df = df.dropna()
df = df[df['release_year'] != 'Unknown']
df['release_year'] = df['release_year'].astype(int)

X = df[['platform', 'release_year']]
y = df['rating']

encoder = OneHotEncoder(sparse_output=False)
X_encoded = encoder.fit_transform(X[['platform']])
X_final = pd.DataFrame(X_encoded, columns=encoder.get_feature_names_out(['platform']))
X_final['release_year'] = X['release_year'].reset_index(drop=True)

X_train, X_test, y_train, y_test = train_test_split(X_final, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Mean Absolute Error (MAE):", round(mae, 3))
print("R-squared (R²):", round(r2, 3))

plt.figure(figsize=(6,6))
plt.scatter(y_test, predictions, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel("Actual Ratings")
plt.ylabel("Predicted Ratings")
plt.title("Actual vs Predicted Ratings")
plt.tight_layout()
plt.savefig('ml/actual_vs_predicted.png')
plt.show()