from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route('/index')
def index():
    return render_template('side1.html', content= 'Denne tekst skal ind i skabelonen.')

@app.route("/profile/<user>")
def userprofile(user):
    return render_template('side2.html', username = user)

@app.route("/iteration")
def iteration():
    n = [
{'navn': "Helene"},
{'navn': "Annette"},
{'navn' : "Søren"}
]
    return render_template('side3.html', navne= n)


if __name__ == "__main__":
    app.run(debug=True)
