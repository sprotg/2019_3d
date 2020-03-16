from flask import Flask
from flask import request
from flask import g
from flask import render_template
from flask import session
from flask import redirect
from flask import url_for
from random import randint
from math import tan, radians

app = Flask(__name__)
app.secret_key = 'very secret string'

answers = {}

def my_render(template, **kwargs):
    return render_template(template, **kwargs)

@app.route("/")
@app.route("/home")
def home():
    return my_render('home.html')

@app.route("/geometri")
def geometri():
    return my_render('geometri.html', title="Klassisk geometri")

@app.route("/analgeo")
def analgeo():
    return my_render('analytiskgeo.html', title="Analytisk geometri")

@app.route("/opg", methods=['GET'])
def opg():
    opg_id = int(request.args['opg_id'])
    if opg_id == 1:
        return generate_skaering_to_linjer()
    else:
        #Tilføj selv flere opgaver...
        return my_render('skaeringtolinjer.html', title="Skæring mellem to linjer")


@app.route("/submit_answer", methods=['POST'])
def submit_answer():
    question_id = request.args['qid']
    svar = request.form['svar']
    opgave_id = request.args['oid']

    if answers[question_id] == svar:
        result = True
    else:
        result = False
    return my_render('result.html', result = result, return_opg=opgave_id)

def register_answer(answer):
    id = str(len(answers.keys()))
    answers[id] = answer
    return id

def generate_skaering_to_linjer():
    #Vælg et skæringspunkt:
    x = randint(-9,9)
    y = randint(-9,9)
    #Vælg en retning for p:
    a1 = tan(radians(randint(0,89)))
    #Vælg en retning for q:
    a2 = tan(radians(randint(91,179)))
    #Bestem b1
    b1 = y - a1*x
    #Bestem b2
    b2 = y - a2*x
    #Question id bruges til at tjekke resultatet senere.
    qid = register_answer("({},{})".format(x,y))
    return my_render('skaeringtolinjer.html', title="Skæring mellem to linjer", opg_id=qid, a1=a1, a2=a2, b1=b1, b2=b2)

if __name__ == "__main__":
    app.run(debug=True)
