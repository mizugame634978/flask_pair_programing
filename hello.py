from flask import Flask

app = Flask(__name__)


@app.route("/japan/<city>")
def hello_a(city):
    return f"hello{city}"
