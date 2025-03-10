from flask import Flask, render_template
import json

app = Flask("Website")


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v2/<word>/')
def word(word):
    with open('dictionary.json', 'r') as file:
        data = json.load(file)
    if word in data:
        definition = data[f"{word}"]
        return {'word': word,
                'definition': definition}
    else:
        return str("Word not present")


app.run(debug=True)
