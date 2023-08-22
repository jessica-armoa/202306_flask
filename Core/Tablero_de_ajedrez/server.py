from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<cantidad_x>')
@app.route('/<cantidad_x>/<cantidad_y>')
@app.route('/<cantidad_x>/<cantidad_y>/<color1>')
@app.route('/<cantidad_x>/<cantidad_y>/<color1>/<color2>')
def ajedrez(cantidad_x=8, cantidad_y=8, color1="red", color2="black"):
    if(not isinstance(cantidad_x,int)):
        try:
            cantidad_x = int(cantidad_x)
        except ValueError:
            return "Error! En la ruta /(cantidad) 'cantidad' debe ser un numero"

    if(not isinstance(cantidad_y,int)):
        try:
            cantidad_y = int(cantidad_y)
        except ValueError:
            return "Error! En la ruta /(cantidad)/(cantidad) ambos datos en 'cantidad' deben ser un numero"

    return render_template('ajedrez.html',cantidad_x=cantidad_x, cantidad_y=cantidad_y, color1=color1, color2=color2)


if __name__=="__main__":
    app.run(debug=True)