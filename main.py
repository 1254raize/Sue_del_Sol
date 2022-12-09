from flask import Flask, render_template

SECRET_KEY ="blablabla"

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)