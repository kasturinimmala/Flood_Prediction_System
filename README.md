# 🌊 Flood Prediction System

A Machine Learning-based web application that predicts the possibility of floods using historical weather and rainfall data. The project combines data preprocessing, multiple classification algorithms, and a Flask web application to provide real-time flood predictions.

---

## 📌 Project Overview

Floods are among the most destructive natural disasters, causing significant damage to lives, infrastructure, and agriculture. This project aims to predict flood occurrence using machine learning techniques so that preventive measures can be taken at an early stage.

The application allows users to enter weather-related parameters through a simple web interface and instantly predicts whether a flood is likely to occur.

---

## 🚀 Features

- Data preprocessing and cleaning
- Missing value detection
- Outlier handling using IQR Capping
- Feature Scaling using StandardScaler
- Train-Test Split
- Multiple Machine Learning models
- Model performance comparison
- Best model selection
- Model saving using Joblib
- Flask-based web application
- Interactive frontend using HTML, CSS, and JavaScript
- Real-time flood prediction

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning Libraries
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib

### Data Visualization
- Matplotlib

### Web Development
- Flask
- HTML
- CSS
- JavaScript

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```
Flood_Prediction_System/
│
├── app.py
├── Flood_Prediction_System.ipynb
├── flood dataset.xlsx
├── floods.save
├── transform.save
│
├── templates/
│   ├── home.html
│   ├── index.html
│   ├── chance.html
│   └── no_chance.html
│
├── static/
│   ├── main.css
│   └── main.js
│
├── .gitignore
└── README.md
```

---

## 📊 Dataset

The dataset contains weather and rainfall-related attributes used for flood prediction.

### Features

- Temperature
- Humidity
- Cloud Cover
- Annual Rainfall
- Jan-Feb Rainfall
- Mar-May Rainfall
- Jun-Sep Rainfall
- Oct-Dec Rainfall
- Average June Rainfall
- Subdivision

### Target Variable

- Flood (0 = No Flood, 1 = Flood)

---

## ⚙️ Data Preprocessing

The following preprocessing steps were performed:

- Checking missing values
- Outlier detection using IQR
- Outlier treatment using capping
- Feature scaling using StandardScaler
- Train-Test splitting (80:20)
- Stratified sampling to preserve class distribution

---

## 🤖 Machine Learning Models

The following classification models were trained and evaluated:

- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- XGBoost

Each model was evaluated using:

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## 🏆 Model Performance

| Model | Accuracy |
|--------|----------|
| Decision Tree | 95.65% |
| Random Forest | 95.65% |
| KNN | 86.96% |
| XGBoost | 86.96% |

Random Forest and Decision Tree achieved the highest accuracy on the dataset.

---

## 💾 Model Deployment

The trained model is saved using Joblib.

Saved files:

- floods.save
- transform.save

During prediction:

1. User enters weather parameters.
2. Data is scaled using the saved StandardScaler.
3. The trained model predicts flood occurrence.
4. Result is displayed on the webpage.

---

## 🌐 Running the Project

Clone the repository

```bash
git clone https://github.com/kasturinimmala/Flood_Prediction_System.git
```

Move into the project folder

```bash
cd Flood_Prediction_System
```

Install dependencies

```bash
pip install pandas numpy matplotlib scikit-learn flask xgboost joblib
```

Run the Flask application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000/
```

---

## 📷 Application Screens

- Home Page
- Prediction Form
- Flood Prediction Result
- Safe Prediction Result

---

## 📈 Future Enhancements

- Improve prediction accuracy using larger datasets
- Deploy the application on Render or Railway
- Integrate live weather API
- Interactive dashboard with charts
- User authentication
- Historical prediction logs
- Mobile responsive UI improvements

---

## 👩‍💻 Author

**Kasturi Nimmala**

GitHub:
https://github.com/kasturinimmala

---

## ⭐ If you found this project useful, consider giving it a star!
