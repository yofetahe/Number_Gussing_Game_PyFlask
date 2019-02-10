from flask import Flask, render_template, session, request, redirect
import random

app = Flask("__name__")
app.secret_key = "development_key"

@app.route("/")
def index():
    x = random.randint(0,100)
    session['number'] = x
    session['trial'] = 0
    return render_template("index.html")

@app.route("/guess_number", methods=['POST'])
def guessNumber():
    y = request.form['givenValue']

    session['value'] = request.form['givenValue']
    session['trial'] = int(session['trial']) + 1

    if int(session['trial']) == 5:
        return redirect("/final_trial")

    if int(session['number']) == int(y):
        return redirect("/correct_result")
    else:
        return redirect("/incorrect_result")

@app.route("/incorrect_result")
def incorrect_result():
    y = session['value']
    guess_status = 'You tried ' + str(session['trial']) + ' times. Try Again.'
    
    if int(y) > (int(session['number']) + 20):
        guess_status = 'You tried ' + str(session['trial']) + ' times. Your guess is to high'
    if int(y) < (int(session['number']) - 20): 
        guess_status = 'You tried ' + str(session['trial']) + ' times. Your guess is to low'

    return render_template("index.html", result='incorrect', guess_result=guess_status)

@app.route("/correct_result")
def correct_result():
    guess_result = 'Wow!!! You Got it. The Number was ' + str(session['number'])
    return render_template("result.html", guess_result=guess_result)

@app.route("/final_trial")
def final_result():
    guess_result = 'Sorry, you tried ' + str(session['trial']) + ' times. The number was ' + str(session['number'])
    return render_template("result.html", guess_result=guess_result)

if __name__ == '__main__':
    app.run(debug=True)