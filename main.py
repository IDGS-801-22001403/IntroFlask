from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    titulo="IDGS801"
    lista=["pedro","juan","christian"]
    return render_template('index.html',titulo=titulo , lista=lista)


@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route('/hola')
def hola():
    return "<h1>Hola, Mundo!</h1>"

@app.route('/user/<string:user>')
def user(user):
    return f'<h1>Hola, {user}!</h1>'

@app.route('/numero/<int:n>')
def numero(n):
    return f'<h1>El número es: {n}</h1>'

@app.route('/operaciones', methods=['POST', 'GET'])
def operacionesBasicas():
    if request.method == 'POST':
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        print("num1", num1)
        print("num2", num2)
        operacion = request.form.get("opOperacion")
        if operacion == "suma":
            resOp = f"La suma de {num1} y {num2} es: {int(num1) + int(num2)}"
        elif operacion == "resta":
            resOp = f"La resta de {num1} y {num2} es: {int(num1) - int(num2)}"
        elif operacion == "multiplicacion":
            resOp = f"La multiplicación de {num1} y {num2} es: {int(num1) * int(num2)}"
        elif operacion == "division":
            resOp = f"La división de {num1} y {num2} es: {int(num1) / int(num2)}"
        
        return render_template('operaciones.html', resOp=resOp)
    return render_template('operaciones.html', resOp='')

@app.route('/user/<int:id>/<string:username>')
def user2(id, username):
    return f'<h1>El usuario es: {username} con id: {id}</h1>'

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return f'<h1>La suma es: {n1 + n2}</h1>'

@app.route('/default/')
@app.route('/default/<string:param>')
def func(param='juan'):
    return f'''
        <form action="/default/" method="get">
            <label for="param">Ingresa el parámetro:</label>
            <input type="text" id="param" name="param" value="{param}">
            <button type="submit">Enviar</button>
        </form>
        <h1>El parámetro es: {param}</h1>
    '''

if __name__ == "__main__":
    app.run(debug=True, port=3000)
