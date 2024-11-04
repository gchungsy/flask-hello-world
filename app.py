from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route("/")
def helloworld():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
    </head>
    <body>
        <h1>Welcome to My Flask App!</h1>
        <p>This is a simple HTML page served by Flask.</p>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
