from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/transaction")
def baby():
    return render_template('transaction.html')


