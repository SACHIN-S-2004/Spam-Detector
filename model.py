from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import pandas as pd

df = pd.read_csv("spam.csv", encoding="latin-1")
df = df[["v1", "v2"]]
df["v1"] = df["v1"].map({
    "ham": 0,
    "spam": 1
})

df["v1"].value_counts()

X = df["v2"]
y = df["v1"]

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_df=0.95,
    min_df=2
)

X_vec = vectorizer.fit_transform(X)

nb_model = MultinomialNB()
nb_model.fit(X_vec, y)

# Save model 
joblib.dump(nb_model, "spam_detection_model.pkl")
# Save vectorizer
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

print("Model trained and saved!")
