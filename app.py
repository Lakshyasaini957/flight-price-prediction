from flask import Flask, request, render_template
from flask_cors import cross_origin

app = Flask(__name__)


@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        try:
            # simple dummy inputs (no pandas)
            Total_stops = int(request.form["stops"])

            # dummy logic
            output = 5000 + (Total_stops * 1000)

            return render_template(
                'index.html',
                prediction_text=f"Your Flight price is Rs. {output}"
            )

        except:
            return render_template(
                'index.html',
                prediction_text="Error: Please enter valid inputs"
            )

    return render_template("index.html")


if __name__ == "__main__":
    app.run()
