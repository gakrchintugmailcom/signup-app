from flask import Flask, render_template, request, redirect, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'users.json'

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    user = {
        'name': request.form['name'],
        'email': request.form['email'],
        'password': request.form['password']
    }

    with open(DATA_FILE, 'r+') as f:
        data = json.load(f)
        data.append(user)
        f.seek(0)
        json.dump(data, f, indent=2)

    return f"User {user['name']} registered successfully!"

@app.route('/users', methods=['GET'])
def users():
    with open(DATA_FILE) as f:
        return jsonify(json.load(f))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
