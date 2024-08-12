from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/submit_fetch', methods=['POST'])
def submit_fetch():
    data = request.get_json()
    username = data.get('username')
    return f'Hello, {username}!'

if __name__ == "__main__":
    
    app.run(debug=True)