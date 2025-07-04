from flask import Flask, render_template, request
import pickle
import numpy as np



# Load vectorizer and model
vectorizer = pickle.load(open("vectorizer.lb", "rb"))
model = pickle.load(open("spamclassifiermodel.pkl", "rb"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if request.method == "POST":
            messg = str(request.form["mesg"])
            if messg.strip() == "":
                return render_template("result.html", prediction="Please enter a valid message.")
            transformed = vectorizer.transform([messg])
            transformed_data = transformed.toarray()
            pred = model.predict(transformed_data)
            output = str(pred[0])
            return render_template("result.html", prediction=f"{output}")
    except Exception as e:
        return render_template("result.html", prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
