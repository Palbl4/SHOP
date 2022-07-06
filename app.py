from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index3.html")


@app.route('/mens_shoes')
def mens_shoes():
    return render_template("men_shoes.html")


@app.route('/female_shoes')
def female_shoes():
    return render_template("female_shoes.html")


@app.route('/children_shoes')
def children_shoes():
    return render_template("children_shoes.html")


if __name__ == "__main__":
    app.run(debug=True)


