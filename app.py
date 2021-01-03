from flask import Flask, render_template, request
from menu import create_dict, add, edit, delete, calculate_total
app = Flask(__name__)

# get different sections from text file (ex: entrees, sides, etc.)
f = open('sample.txt', 'r')
file_content = f.read()
menu, truck_name = create_dict(file_content)
sections = menu.keys()
f.close()
anchor = None
cart = []
total = 0.0

@app.route('/')
def landing():
    cart = []
    total = 0.0
    return render_template('index.html', truck_name=truck_name, sections=sections, menu=menu, total=total)

@app.route('/scroll')
def scroll():
    req = request.args
    anchor = req['section']
    return render_template('index.html', truck_name=truck_name, scroll=anchor, sections=sections, menu=menu, total=total)

@app.route('/add', methods=['POST'])
def add_to_cart():
    req = request.form
    item = req['item']
    count = req['count']
    price = req['price']
    newCart = add(cart, item, count, price)
    total = calculate_total(newCart)
    return render_template('index.html', truck_name=truck_name, scroll=anchor, sections=sections, menu=menu, cart=newCart, total=total)

@app.route('/edit', methods=['POST'])
def edit_cart():
    req = request.form
    item = req['item']
    count = req['count']
    price = req['price']
    newCart = edit(cart, item, count, price)
    total = calculate_total(newCart)
    return render_template('index.html', truck_name=truck_name, scroll=anchor, sections=sections, menu=menu, cart=newCart, total=total)

@app.route('/delete', methods=['POST'])
def delete_from_cart():
    req = request.form
    item = req['item']
    newCart = delete(cart, item)
    total = calculate_total(newCart)
    return render_template('index.html', truck_name=truck_name, scroll=anchor, sections=sections, menu=menu, cart=newCart, total=total)

if __name__ == '__main__':
    app.run()