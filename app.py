from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    titolo="pagina iniziale"
    bottone="più info"
    testo="Ciao mondo!"
    return render_template("index.html", 
            titolo=titolo,
            testo=testo,
            bottone=bottone)

@app.route('/info')
def info():
    titolo="pagina info"
    bottone="Homepage"
    testo="informazioni"
    return render_template("info.html", 
            titolo=titolo,
            testo=testo) 

if __name__ == '__main__':
    app.run()
