from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("spam_detection_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        message = request.form['message']

        message_vector = vectorizer.transform([message])
        prediction = model.predict(message_vector)[0]

    except Exception as e:
        print("Prediction error:", e)
        prediction = "Error"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
