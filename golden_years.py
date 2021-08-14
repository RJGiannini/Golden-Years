from flask import Flask

app = Flask(__golden_years__)

@app.route("/")
def Golden_Years():
    return "<p>Financial Planning for a better retirement!</p>"