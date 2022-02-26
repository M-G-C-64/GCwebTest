from dataclasses import dataclass
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", data = "Sending this seperately")