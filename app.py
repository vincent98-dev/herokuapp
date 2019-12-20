from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Ciao mondo!"

@app.route('/info')
def info():
    return "informazioni"


if __name__ == '__main__':
    app.run()
