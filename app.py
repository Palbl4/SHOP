from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/mens-shoes')
def mens_shoes():
    return render_template("mens-shoes.html")


@app.route('/female-shoes')
def female_shoes():
    return render_template("female-shoes.html")


@app.route('/children-shoes')
def children_shoes():
    return render_template("children-shoes.html")


if __name__ == "__main__":
    app.run(debug=True)


