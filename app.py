from flask import Flask, render_template, request
import pandas as pd
import joblib

# Create Flask app
app = Flask(__name__)

# Load model and scaler
model = joblib.load("floods.save")
scaler = joblib.load("transform.save")

# Home Page
@app.route("/")
def home():
    return render_template("home.html")

# Prediction Page
@app.route("/predict")
def predict():
    return render_template("index.html")

# Prediction Logic
@app.route("/result", methods=["POST"])
def result():

    temp = float(request.form["Temp"])
    humidity = float(request.form["Humidity"])
    cloud = float(request.form["Cloud Cover"])
    annual = float(request.form["ANNUAL"])
    janfeb = float(request.form["Jan-Feb"])
    marmay = float(request.form["Mar-May"])
    junsep = float(request.form["Jun-Sep"])
    octdec = float(request.form["Oct-Dec"])
    avgjune = float(request.form["avgjune"])
    sub = float(request.form["sub"])

    data = pd.DataFrame([[temp, humidity, cloud,
                          annual, janfeb, marmay,
                          junsep, octdec,
                          avgjune, sub]],
                        columns=[
                            "Temp",
                            "Humidity",
                            "Cloud Cover",
                            "ANNUAL",
                            "Jan-Feb",
                            "Mar-May",
                            "Jun-Sep",
                            "Oct-Dec",
                            "avgjune",
                            "sub"
                        ])

    data = scaler.transform(data)

    prediction = model.predict(data)

    if prediction[0] == 1:
        return render_template("chance.html")

    else:
        return render_template("no_chance.html")


if __name__ == "__main__":
    app.run(debug=True)