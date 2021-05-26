from flask import Flask, render_template, request

#importamos la libreria de Flask


# creamos un objeto de Flask
app = Flask(__name__)

#creamos una ruta a raíz o página principal
@app.route("/")

#creamos una función para mostrar index.html
def index():
    return render_template('index.html')

@app.route('/in_contacto', methods=['POST'])
def contacto():
    if request.method == 'POST':
        nombre= request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']
        print(nombre)
        print(telefono)
        print(email)
    return 'Datos recibidos'

def quienesSomos():
    return render_template('quienesomos.html')

#Creamos una condicional para tener un archivo de ejecución
#se ejecuta en terminal con: python nombredelarchivo.py
if __name__ == '__main__':
    #escuche siempre por el puerto 80
    app.run(port=80, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
