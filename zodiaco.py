from flask import Flask, render_template, request
from datetime import datetime

def calcular_edad(anio_nacimiento):
    anio_actual = datetime.now().year
    return anio_actual - anio_nacimiento

def obtener_signo(anio):
    signos = {
        "Mono": "img/mono.jpg",
        "Gallo": "img/gallo.jpg",
        "Perro": "img/perro.jpg",
        "Cerdo": "img/cerdo.jpg",
        "Rata": "img/rata.jpg",
        "Buey": "img/buey.jpg",
        "Tigre": "img/tigre.jpg",
        "Conejo": "img/conejo.jpg",
        "Dragón": "img/dragon.jpg",
        "Serpiente": "img/serpiente.jpg",
        "Caballo": "img/caballo.jpg",
        "Cabra": "img/cabra.jpg"
    }
    signo = list(signos.keys())[anio % 12]
    return signo, signos[signo]

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)
