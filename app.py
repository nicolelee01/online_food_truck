from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def landing():
    return render_template('index.html', truck_name='Rockin\' Rolls')

@app.route('/scroll')
def scroll():
    req = request.args
    anchor = req['section']
    print(anchor)
    return render_template('index.html', truck_name='Rockin\' Rolls', scroll=anchor)


if __name__ == '__main__':
    app.run()