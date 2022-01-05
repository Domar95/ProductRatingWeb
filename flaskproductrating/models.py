from datetime import datetime
import timeago
from flaskproductrating import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
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
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    score_taste = db.Column(db.Integer, nullable=False)
    score_health = db.Column(db.Integer, nullable=False)
    picture = db.Column(db.String(20), nullable=True, default='test-product.png')
    price = db.Column(db.Float, nullable=True)
    shop = db.Column(db.String(50), unique=False, nullable=True) #+ osobna klasa
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #+description

    def time_ago(self):
        return timeago.format(self.date, datetime.now())

    def __repr__(self):
        return str(self.__dict__)