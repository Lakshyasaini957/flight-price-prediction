import pandas as pd
import numpy
import sklearn

app = Flask(__name__)

# ❌ MODEL REMOVE (deployment ke liye)
# import pickle
# model = pickle.load(open("flight_rf.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        try:
            date_dep = request.form["Dep_Time"]
            Journey_day = int(pd.to_datetime(date_dep).day)
            Journey_month = int(pd.to_datetime(date_dep).month)

            Dep_hour = int(pd.to_datetime(date_dep).hour)
            Dep_min = int(pd.to_datetime(date_dep).minute)

            date_arr = request.form["Arrival_Time"]
            Arrival_hour = int(pd.to_datetime(date_arr).hour)
            Arrival_min = int(pd.to_datetime(date_arr).minute)

            dur_hour = abs(Arrival_hour - Dep_hour)
            dur_min = abs(Arrival_min - Dep_min)

            Total_stops = int(request.form["stops"])

            # 🔥 DUMMY PREDICTION (IMPORTANT)
            output = 5000 + (Total_stops * 1000) + (dur_hour * 200)

            return render_template(
                'index.html',
                prediction_text=f"Your Flight price is Rs. {output}"
            )

        except Exception as e:
            return render_template(
                'index.html',
                prediction_text="Error: Please enter valid inputs"
            )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
