import secrets
import os
from PIL import Image
from flask import render_template, flash, redirect, request
from flask_login.utils import login_user
from flaskproductrating import app, db, bcrypt
from flaskproductrating.forms import RegistrationForm, LoginForm, UpdateAccountForm, ProductForm
from flaskproductrating.models import User, Product
from flask.helpers import url_for
from flask_login import login_user, current_user, logout_user, login_required

# sample data
from flaskproductrating.products import default_products
my_products = default_products

@app.route("/home")
@app.route("/")
def home():
    products = Product.query.all()
    return render_template('home.html', products = products)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')
    
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'{user.username}, your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture, folder):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static', folder, picture_fn)

    output_size = (125, 125)
    img = Image.open(form_picture)
    img.thumbnail(output_size)
    img.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data, 'profile_pics')
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title="Account", image_file=image_file, form=form)


@app.route('/product/new', methods=['GET', 'POST'])
@login_required
def new_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data, category=form.category.data, score_taste=form.score_taste.data, score_health=form.score_health.data,
                        price=form.price.data, shop=form.shop.data, user_id=current_user.id)
        print(form.picture.data)
        print(product.picture)
        if form.picture.data:
            picture_file = save_picture(form.picture.data, 'product_pics')
            print(picture_file)
            product.picture = picture_file
        db.session.add(product)
        db.session.commit()
        flash('Your product has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_product.html', title='New Product', form=form)


@app.route('/product/<int:product_id>')
def product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', title=product.name, product=product)
