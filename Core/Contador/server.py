from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'clave ultra secreta'



@app.route('/')
def contar():
  session['contador'] = 0
  return redirect('/contador')

@app.route('/contador')
def mostrar():
  session['contador'] += 1
  return render_template('contador.html')

if __name__=="__main__":
    app.run(debug=True)