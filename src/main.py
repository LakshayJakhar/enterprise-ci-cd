import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Railway! is it working let try  :)"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)


def some_function():
    return 42

def nice();
