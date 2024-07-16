import os
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def items():
    with open('items.json', 'r') as json_file:
        data = json.load(json_file)
        items_list = data['items']
    
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

