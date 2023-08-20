from flask import Flask
app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '¡Hola Mundo!'

@app.route('/dojo')
def dojo():
    return '¡Dojo!'

@app.route('/say/<name>')
def saludo(name):
    if(not name.isalpha()):
        return "/say/(name)\nEn la ruta utilizada 'name' debe ser un texto"
    return "¡Hola, "+name+"!"

@app.route('/repeat/<cantidad>/<palabra>')
def repetir(cantidad, palabra):
    if(not isinstance(cantidad,int)):
        try:
            cantidad = int(cantidad)
        except ValueError:
            return "/repeat/(cantidad)/(palabra)\nEn la ruta utilizada 'cantidad' debe ser un numero"

    if(not palabra.isalpha()):
        return "/repeat/(cantidad)/(palabra)\nEn la ruta utilizada 'palabra' debe ser un texto"

    return (palabra+" ")*int(cantidad)

@app.route('/<otro>')
def otro(otro):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez."

if __name__=="__main__":
    app.run(debug=True)