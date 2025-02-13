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

@app.route('/cinepolis')
def cinepolis():
    return render_template('cinepolis.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form['nombre']
    cantidad = int(request.form['cantidad'])
    cantidad_boletos = int(request.form['boletos'])
    tarjeta = request.form['tarjeta']

    usa_tarjeta = tarjeta == 'si'
    if cantidad_boletos > 7 * cantidad:
        return render_template('cinepolis.html', error="No pueden comprar más de 7 boletos por persona.")
    

    total = calcular_total(cantidad_boletos, usa_tarjeta)
    
    resOp = f"${total:.2f}"

    return render_template('cinepolis.html', resOp=resOp)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
