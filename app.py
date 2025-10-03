from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

user = {"username": "amelka", "password": "amelka12"}

@app.route('/main')
def main():
    return render_template('nauka.html')

@app.route('/blad')
def fail():
    return render_template('nieudanelogowanie.html')

@app.route('/login', methods = ['POST', 'GET'])
def logowanie():
    if request.method == 'GET':
        return render_template('logowanie.html')
    if request.method == 'POST':
        dane = request.form
        uzyt = dane.get('name')
        haslo = dane.get('haslo')
        if uzyt == user['username'] and haslo == user['password']:
            print('Poszlo prawidlowo')
            return redirect(url_for('main'))
        elif uzyt != user['username'] and haslo != user['password']:
            print('nie udalo sie zalogowac... bo niepoprawne haslo....')
            return redirect(url_for('fail'))

