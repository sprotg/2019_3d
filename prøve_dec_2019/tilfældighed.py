from flask import Flask
from flask import render_template
from flask import g
import sqlite3
import random

app = Flask(__name__)

def _get_db():
    db = g.get('_database', None)
    if db is None:
        db = g._databdase = sqlite3.connect('terningekast.db')
    return db

def create_db_table():
    c = _get_db().cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS terninger(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tal INTEGER);""")
    _get_db.commit()


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', tal = random.random())


if __name__ == "__main__":
    with app.app_context():
        create_db_table()

    app.run(debug=True)
