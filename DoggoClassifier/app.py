from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to the DoggoFindr API!"

@app.route('/breed', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Test"
    else:
        return "Use POST method to use /breed endpoint"
