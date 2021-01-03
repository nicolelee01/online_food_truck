from flask import Flask, render_template, request
from menu import create_dict
app = Flask(__name__)


# get different sections from text file (ex: entrees, sides, etc.)
f = open('sample.txt', 'r')
file_content = f.read()
menu, truck_name = create_dict(file_content)
sections = menu.keys()
f.close()
anchor = None

@app.route('/')
def landing():
    return render_template('index.html', truck_name=truck_name, sections=sections, menu=menu)

@app.route('/scroll')
def scroll():
    req = request.args
    anchor = req['section']
    return render_template('index.html', truck_name=truck_name, scroll=anchor, sections=sections, menu=menu)

@app.route('/add', methods=['POST'])
def add_to_cart():
    req = request.form
    print(req['count'], req['item'])

    return render_template('index.html', truck_name=truck_name, scroll=anchor, sections=sections, menu=menu)

if __name__ == '__main__':
    app.run()