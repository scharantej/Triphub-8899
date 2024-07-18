
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

travel_options = [
    {'mode': 'train', 'duration': '4 hours'},
    {'mode': 'bus', 'duration': '6 hours'},
    {'mode': 'flight', 'duration': '2 hours'},
    {'mode': 'donkey', 'duration': '1 day'},
    {'mode': 'ferry', 'duration': '3 hours'},
    {'mode': 'bike', 'duration': '8 hours'},
]

@app.route('/')
def home():
    return render_template('home.html', travel_options=travel_options)

@app.route('/schedule', methods=['POST'])
def schedule():
    departure = request.form['departure']
    destination = request.form['destination']
    date = request.form['date']
    mode = request.form['mode']
    
    selected_options = [option for option in travel_options if option['mode'] == mode]
    
    return render_template('schedule.html', selected_options=selected_options)

if __name__ == '__main__':
    app.run(debug=True)
