from flask import Flask, render_template

app = Flask(__name__)

my_products = [
        {
            'name': 'Ketchup Tortex',
            'category': 'Ketchup',
            'date': '2021-12-10',
            'score_taste': 70,
            'score_health': 60,
            'picture': 'zdjecie4.jpg',
            'price': '4,00',
            'shop': 'Biedronka',
            'index': 0
        },
        {
            'name': 'Mirinda',
            'category': 'Napoje',
            'date': '2021-12-11',
            'score_taste': 70,
            'score_health': 50,
            'picture': 'zdjecie5.jpg',
            'price': '5,00',
            'shop': 'Lidl',
            'index': 0
        },
                {
            'name': 'Ketchup Tortex1',
            'category': 'Ketchup',
            'date': '2021-12-10',
            'score_taste': 70,
            'score_health': 60,
            'picture': 'zdjecie4.jpg',
            'price': '4,00',
            'shop': 'Biedronka',
            'index': 0
        },
                {
            'name': 'Ketchup Tortex2',
            'category': 'Ketchup',
            'date': '2021-12-10',
            'score_taste': 70,
            'score_health': 60,
            'picture': 'zdjecie4.jpg',
            'price': '4,00',
            'shop': 'Biedronka',
            'index': 0
        },
                {
            'name': 'Ketchup Tortex3',
            'category': 'Ketchup',
            'date': '2021-12-10',
            'score_taste': 70,
            'score_health': 60,
            'picture': 'zdjecie4.jpg',
            'price': '4,00',
            'shop': 'Biedronka',
            'index': 0
        },
                {
            'name': 'Ketchup Tortex',
            'category': 'Ketchup',
            'date': '2021-12-10',
            'score_taste': 70,
            'score_health': 60,
            'picture': 'zdjecie4.jpg',
            'price': '4,00',
            'shop': 'Biedronka',
            'index': 0
        },
                {
            'name': 'Ketchup Tortex',
            'category': 'Ketchup',
            'date': '2021-12-10',
            'score_taste': 70,
            'score_health': 60,
            'picture': 'zdjecie4.jpg',
            'price': '4,00',
            'shop': 'Biedronka',
            'index': 0
        },
                {
            'name': 'Ketchup Tortex',
            'category': 'Ketchup',
            'date': '2021-12-10',
            'score_taste': 70,
            'score_health': 60,
            'picture': 'zdjecie4.jpg',
            'price': '4,00',
            'shop': 'Biedronka',
            'index': 0
        },
                {
            'name': 'Ketchup Tortex',
            'category': 'Ketchup',
            'date': '2021-12-10',
            'score_taste': 70,
            'score_health': 60,
            'picture': 'zdjecie4.jpg',
            'price': '4,00',
            'shop': 'Biedronka',
            'index': 0
        },
                {
            'name': 'Ketchup Tortex',
            'category': 'Ketchup',
            'date': '2021-12-10',
            'score_taste': 70,
            'score_health': 60,
            'picture': 'zdjecie4.jpg',
            'price': '4,00',
            'shop': 'Biedronka',
            'index': 0
        },
                {
            'name': 'Ketchup Tortex',
            'category': 'Ketchup',
            'date': '2021-12-10',
            'score_taste': 70,
            'score_health': 60,
            'picture': 'zdjecie4.jpg',
            'price': '4,00',
            'shop': 'Biedronka',
            'index': 0
        }
    ]

@app.route("/home")
@app.route("/")
def hello_world():
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

if __name__ == '__main__':
    app.run(debug=True)