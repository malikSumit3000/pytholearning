from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

data = pd.read_csv('data_small/stations.txt', skiprows=17)
station_data = data[["STAID", "STANAME                                 "]][0:101].to_html()


@app.route('/')
def home():
    return render_template("home.html", data=station_data)


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


@app.route('/api/v1/<station>')
def stat_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df["TG"] = df['   TG'].loc[df['   TG'] != -9999] / 10
    station_all_data = df[['    DATE', "TG"]].to_html()
    return render_template('station.html', data=station_all_data)


@app.route('/api/v1/yearly/<station>/<year>')
def stat_annual_data(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["TG"] = df['   TG'].loc[df['   TG'] != -9999] / 10
    df = df[df["    DATE"].astype(str).str.startswith(str(year))]
    annual_data = df[['    DATE', "TG"]].to_html()
    return render_template("yearly.html", data=annual_data)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
