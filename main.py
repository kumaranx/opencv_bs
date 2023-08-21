from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    # Load and process data from your Python file
    data = read_data_from_file()

    return render_template("index.html", data=data)


def read_data_from_file():
    # Read data from your Python file and return it
    return "Your data from the Python file"


if __name__ == "__main__":
    app.run()
