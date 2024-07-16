import os
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as json_file:
            data = json.load(json_file)
            items_list = data.get('items', [])  # Use .get() to handle missing key gracefully
    except FileNotFoundError:
        items_list = []  # Handle file not found error

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

