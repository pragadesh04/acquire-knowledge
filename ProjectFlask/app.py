from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    titles = ["C","Java","Python","JavaScripts","Flask","end"]
    logged = False
    return render_template("index.html", titles = titles, logged = logged)

@app.route('/home/<name>')
def home(name):
    # return "<h1>this is home</h1>"
    names = ["apple", "orange", "pineapple"]
    profile = {"name":name, "age":23}
    return render_template("home.html", name = name, names=names, profile = profile)



if __name__ == '__main__':
    app.run(debug=True)