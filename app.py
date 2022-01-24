from flask import Flask

app = Flask(__name__)
@app.route("/")
def methode():
    return "Dit is een test"

