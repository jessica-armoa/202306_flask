from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'clave ultra secreta'

@app.route('/')
def inicio():
  return render_template('formulario.html')

@app.route('/process', methods=['POST'])
def process():
  print(request.form)
  session['name'] = request.form['name']
  session['location'] = request.form['location']
  session['language'] = request.form['language']
  session['comments'] = request.form['comments']
  return redirect('/result')

@app.route('/result')
def result():
  return render_template('resultado.html')

if __name__=="__main__":
    app.run(debug=True)