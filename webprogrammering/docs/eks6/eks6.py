from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
@app.route('/index')
def index():
    val = request.args['value']
    return render_template('main.html', v = val)



if __name__ == "__main__":
    app.run(debug=True)
