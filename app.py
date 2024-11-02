from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def helloworld():
    r = request.get('https://lab.gchungsy5.workers.dev/', verify=False)
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
