from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "SRE App Running!"

@app.route("/fail")
def fail():
    if random.random() > 0.7:
        return "Simulated failure", 500
    return "Recovered"

app.run(host="0.0.0.0", port=5000)
