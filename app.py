import os
from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def hello():
    return redirect("https://ahorn.netlify.com/", code=302)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
