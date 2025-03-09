from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/api/v1/<station>/<date>')
def temp(station, date):
    station = 10
    date = 20030225
    temperature = 0.2
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)
