from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/engineer")
def engineer():
    return render_template("engineer.html")

@app.route("/fighter")
def fighter():
    return render_template("fighter.html")

if __name__ == "__main__":
    app.run(debug=True)