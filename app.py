from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///item.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)





class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    male_female = db.Column(db.String(10), nullable=False)
    title = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    img = db.Column(db.Text)

    def __repr__(self):
        return self.title




@app.route('/')
def index():
    return render_template("index.html")


@app.route('/mens-shoes')
def mens_shoes():
    items = Item.query.order_by(Item.title, Item.male_female, Item.description, Item.img).all()
    return render_template("mens-shoes.html", data=items)


@app.route('/female-shoes')
def female_shoes():
    items = Item.query.all()
    return render_template("female-shoes.html", data=items)


@app.route('/children-shoes')
def children_shoes():
    item = Item.query.all()
    return render_template("children-shoes.html", data=item)



if __name__ == "__main__":
    app.run(debug=True)


