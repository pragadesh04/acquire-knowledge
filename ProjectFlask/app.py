from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>_praga_always_smart_</h1><p>be active not proactive</p>'

name = "home"

@app.route('/home/<name>')
def home(name):
    return "<h1>this is home:{}</h1>".format(name.upper())


if __name__ == '__main__':
    app.run(debug=True)