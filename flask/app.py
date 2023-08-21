import json
from flask import Flask, render_template, Response
import random
import time

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("dashboard.html")


def generate_data():
    while True:
        data = {
            "temperature": random.uniform(20, 30),
            "humidity": random.uniform(40, 60),
            "pressure": random.uniform(900, 1100),
        }
        yield f"data: {json.dumps(data)}\n\n"
        time.sleep(0.5)


@app.route("/stream")
def stream():
    return Response(generate_data(), content_type="text/event-stream")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
