from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route('/hi')
def hello():
    return "Hi bro"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')

    # Store the lead in a CSV file
    with open('leads.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email])

    return render_template('output.html')


app.run()
