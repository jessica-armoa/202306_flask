import random
from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'clave ultra secreta'


@app.route('/')
def inicio():
    session['numero'] = random.randint(1, 5)
    session['cantidad_intentos'] = 0
    return render_template('formulario.html')

@app.route('/form', methods=['POST'])
def procesar():
    print(request.form['numero'])
    session['intento'] = int(request.form['numero'])
    session['cantidad_intentos'] += 1
    return redirect('/pista')

@app.route('/pista')
def pista():
    if session['intento'] == session['numero']:
        return render_template('resultado.html',numero=session['intento'], cantidad=session['cantidad_intentos'])

    pista = 'high' if session['intento'] > session['numero'] else 'low'
    return render_template('formulario_pista.html',pista=pista)

@app.route('/restart')
def restart():
    session.pop('numero')
    session.pop('intento')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)