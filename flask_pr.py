from flask import Flask, render_template, flash, redirect
from flask.helpers import url_for
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = 'QZJTt6VHV8rAsk3hkMMo3Zn8XzDxinj7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    products = db.relationship('Product', backref='created_by', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    category = db.Column(db.String(50), unique=False, nullable=False) #+ osobna klasa
    date =  db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    score_taste = db.Column(db.Integer, nullable=False)
    score_health = db.Column(db.Integer, nullable=False)
    picture = db.Column(db.String(20), nullable=False, default='default.jpg')
    price = db.Column(db.Float, nullable=True)
    shop = db.Column(db.String(50), unique=False, nullable=False) #+ osobna klasa
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return str(self.__dict__)

# sample data
from products import default_products
my_products = default_products

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html', products = my_products)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/new-product")
def new_product():
    return "<h1>Add New Product</h1>"
    
@app.route("/change-product")
def change_product():
    return "<h1>Change Product</h1>"

@app.route("/delete-product")
def delete_product():
    return "<h1>Delete Product</h1>"

@app.route("/save-file")
def save_file():
    return "<h1>Save file</h1>"

@app.route("/load-file")
def load_file():
    return "<h1>Load file</h1>"

@app.route("/clear-products")
def clear_products():
    return "<h1>Clear Products</h1>"

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'kaka@tlen.pl' and form.password.data == '123':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)