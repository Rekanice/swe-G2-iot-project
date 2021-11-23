from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/quote')
def quote():
    return render_template('quote.html')

@app.route('/joke')
def joke():
    return render_template('joke.html')

@app.route('/fact')
def fact():
    return render_template('fact.html')

@app.route('/misconception')
def misconception():
    return render_template('misconception.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)