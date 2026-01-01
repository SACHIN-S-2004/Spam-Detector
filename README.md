<div align="center">

# 📩 Spam Detector
### *ML–Powered Message Classification*

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![Flask](https://img.shields.io/badge/Flask-Web_App-green?style=for-the-badge&logo=flask)
![Bootstrap](https://img.shields.io/badge/Bootstrap-UI-purple?style=for-the-badge&logo=bootstrap)

🚀 **Detect whether a message is Spam or Ham using Machine Learning — instantly and accurately**

</div>

---

## 📌 Project Overview

The **Spam Detector** is an end-to-end **Machine Learning + Web Application** that classifies text messages as **Spam** or **Not Spam (Ham)**.

The application features a **simple single-textbox interface** where users can input any message and instantly receive a prediction.  
Behind the scenes, the system uses **Natural Language Processing (NLP)** techniques and a trained ML model to make accurate decisions.

This project demonstrates how classical ML algorithms still outperform complex models in **text classification tasks** when used correctly.

---

## ✨ Key Features

✔️ Minimal and intuitive UI (single input textbox)  
✔️ Real-time spam classification  
✔️ NLP-based text preprocessing  
✔️ Multiple ML models trained and compared  
✔️ Best-performing model deployed to web app  
✔️ Lightweight, fast, and scalable solution  

---

## 🖼️ Sample Screenshots

<div align="center">

### 📱 Webpage - Responsive Design

![alt text](sampleScreenshots/Screenshot%20(1772).png)

### 📊 Prediction Results

![alt text](sampleScreenshots/Screenshot%20(1773).png)

![alt text](sampleScreenshots/Screenshot%20(1774).png)

*Real-time classification results*

</div>

---

## 🧠 Machine Learning Workflow

### 🔹 Text Preprocessing
- Lowercasing text
- Stopword removal
- Vectorization using **TF-IDF**

---

### 🔹 Models Trained & Evaluated

The following algorithms were trained and evaluated in the Jupyter Notebook:

| Model | Description |
|-----|------------|
| 📊 Logistic Regression | Linear classifier for text data |
| 📨 Naive Bayes (Multinomial) | Probabilistic text classifier |

---

## 🏆 Model Selection – Why Naive Bayes?

After performance comparison:

✅ **Naive Bayes outperformed Logistic Regression**  
- Higher accuracy on text data  
- Extremely fast predictions  
- Works exceptionally well with TF-IDF features  
- Lightweight and ideal for real-time web apps  

📌 **Final Decision:**  
➡️ **Multinomial Naive Bayes** was selected for deployment.

---

## 🌐 Web Application Overview

🖥️ **Frontend**
- Single textbox for message input
- Clean and responsive UI
- Instant result display

⚙️ **Backend**
- Flask receives the message
- Preprocessing pipeline applied
- Naive Bayes model predicts spam or ham

📊 **Output**
- Clear classification: **Spam** or **Not Spam**
- User-friendly result display

---

## 🛠️ Tech Stack

| Layer | Technology |
|----|----|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| NLP | TF-IDF Vectorization |
| Model Training | Jupyter Notebook |
| Backend | Flask |
| Frontend | HTML, Bootstrap |

---

## 🚀 How to Run the Project

# Clone the repository
git clone https://github.com/SACHIN-S-2004/Spam-Detector.git

# Navigate to project directory
cd Spam-Detector

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py

---
