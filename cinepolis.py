from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_total(cantidad_boletos, usa_tarjeta):
    precio = 12  # price per ticket
    total = cantidad_boletos * precio


    if cantidad_boletos > 5:
        total *= 0.85 
    elif 3 <= cantidad_boletos <= 5:
        total *= 0.90 

    if usa_tarjeta:
        total *= 0.90 

    return total



if __name__ == "__main__":
    app.run(debug=True, port=3000)
