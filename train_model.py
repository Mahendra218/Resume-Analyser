import os
import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv(r"C:\Users\mmars\OneDrive\Desktop\Ai resume\Resume\Resume.csv")

# Keep only required columns
df = df[['Resume_str', 'Category']]

# Remove missing values
df.dropna(inplace=True)

X = df["Resume_str"]
y = df["Category"]

# TF-IDF
tfidf = TfidfVectorizer(stop_words="english", max_features=5000)
X_vector = tfidf.fit_transform(X)

# Train Model
model = LogisticRegression(max_iter=1000)
model.fit(X_vector, y)

# Create model folder
os.makedirs("model", exist_ok=True)

# Save model
joblib.dump(model, "model/clf.pkl")
joblib.dump(tfidf, "model/tfidf.pkl")

print("Model trained successfully!")