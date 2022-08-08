import os
from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask("__name__")
run_with_ngrok(app)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/test')
def hello2():
    return '123!'


if __name__ == "__main__":
    #port = os.environ.get("PORT", 5000)
    #app.run(host="0.0.0.0", port=port)
    app.run()


