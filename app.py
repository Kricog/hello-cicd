from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Container Apps!"

@app.route("/health")
def health():
    return "ok", 200
