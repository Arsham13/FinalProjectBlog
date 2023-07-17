from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'this is a home page...'

app.run(debug=True)