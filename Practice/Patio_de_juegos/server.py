from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def jugar_default():
    return jugar(3)

@app.route('/play/<cantidad>')
@app.route('/play/<cantidad>/<color>')
def jugar(cantidad,color="turquoise"):
    if(not isinstance(cantidad,int)):
        try:
            cantidad = int(cantidad)
        except ValueError:
            return "Error! En la ruta /play/(cantidad) 'cantidad' debe ser un numero"
    return render_template('index.html',cantidad=cantidad, color=color)


if __name__=="__main__":
    app.run(debug=True)