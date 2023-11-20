from flask import Flask, render_template, request
from random import sample
from werkzeug.utils import secure_filename
import os
from melanoma import Melanoma as Melanoma

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/registrar-archivo', methods=['POST'])
def registarArchivo():
    #Script para archivo
    file                = request.files['archivo']
    basepath            = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
    filename            = secure_filename(file.filename) #Nombre original del archivo
    extension           = os.path.splitext(filename)[1]
    nuevoNombreFile     = stringAleatorio() + extension
    upload_path         = os.path.join (basepath, 'static/archivos', nuevoNombreFile)
    file.save(upload_path)
    mela = Melanoma()
    return mela.consultar(upload_path, nuevoNombreFile)

def stringAleatorio():
    #Generando string aleatorio
    string_aleatorio     = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud             = 20
    secuencia            = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio

#Declarando nombre de la aplicación e inicializando
if __name__ == '__main__':
    app.run(debug=True)
