from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'clave ultra secreta'

@app.route('/')
def contar():
  if 'contador' in session:
    session['contador'] += 1
  else:
    session['contador'] = 1
  return render_template('contador.html')

@app.route('/destroy_session')
def destruir():
  session.pop('contador')
  return redirect('/')

if __name__=="__main__":
    app.run(debug=True)