from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():

    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/api/v1/<station>/<date>')
def temp(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df["TG"] = df['   TG'].loc[df['   TG'] != -9999] / 10
    temperature = df["TG"].loc[df['    DATE'] == date].squeeze()
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True, port=5001)
