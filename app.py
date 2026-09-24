from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to My Flask Application!"


@app.route("/about")
def about():
    return "This is a Python Flask application using GitHub Actions."


@app.route("/contact")
def contact():
    return "Contact page of my Flask application."


if __name__ == "__main__":
    app.run(debug=True)