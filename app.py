from werkzeug.security import generate_password_hash, check_password_hash

from flask import Flask, render_template, url_for, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Column, Integer, String
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///shop1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.secret_key = 'afwAKFLKMNLAlkfmakSKFNAlKfnLAKSnflkanfl21431OKFOAokfko32ro###@Okfokefoekfo'



class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    male_female = db.Column(db.String(10), nullable=False)
    title = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    img = db.Column(db.Text)

    def __repr__(self):
        return self.title


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String, nullable=True)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)

    pr = db.relationship('Profiles', backref='users', uselist=False)

    def __repr__(self):
        return f'user {self.id}'


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    old = db.Column (db.Integer)
    city = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Это юзер из профиля {self.id}'




@app.route('/register', methods=("POST", "GET"))
def register():
    if request.method == 'POST':
        try:
            hash1 = generate_password_hash(request.form['password'])
            u = user(email=request.form['email'], password=hash1)
            db.session.add(u)
            db.session.flush()

            p = Profiles(name=request.form['name'], old=request.form['old'], city=request.form['city'], user_id=u.id)
            db.session.add(p)
            db.session.commit()
        except:
            db.session.rollback()
            print("Ошибка добавления в БД")

    return render_template("register.html")



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/mens-shoes', methods=("GET", "POST"))
def mens_shoes():
    if request.method == 'POST':
        # приводим оба параметра к числу что бы сессия не материлась
        id = int(request.form['id'])
        qty = int(request.form['qty'])
        # проверяем совпадения id product_id и если оно есть, то прибавляем количество qty к уже существующему
        matching = [d for d in session['cart'] if d['id'] == id]
        if matching:
            matching[0]['qty'] += qty

        session["cart"].append(dict({'id': id, 'qty': qty}))  # добавляем товар к сессии в виде словаря

        return redirect(url_for('basket'))
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


@app.route('/basket', methods=("POST", "GET"))
def basket():
    # if request.method == "POST":
    #     session['id'] = request.form['id']
    #     session['title'] = request.form['title']
    #     session['img'] = request.form['img']

    return render_template("basket.html", session=session)


if __name__ == "__main__":
    app.run(debug=True)
