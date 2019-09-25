from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
@app.route('/index')
def index():
    return render_template('formular.html')

@app.route("/modtag_data", methods=['POST'])
def modtag():
    modtaget_navn = request.form['navn']
    return render_template("vis.html", navn = modtaget_navn)

if __name__ == "__main__":
    app.run(debug=True)
