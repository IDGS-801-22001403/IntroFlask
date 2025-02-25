from flask import Flask, render_template, request
from cinepolis import *
from zodiaco import *
from flask import g
from flask import flash
import forms
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.secret_key='esta es una clave secreta'
csrf=CSRFProtect()



@app.before_request
def before_request():
    g.user = "mario"
    print("before 1")

@app.after_request
def after_request(response):
    print("after 1")


@app.route('/')
def index():
    nom='none'
    titulo="IDGS801"
    lista=["pedro","juan","christian"]
    nom=g.user
    print("index 2 {}.format(g.user)")
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
# cinepolis
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

#zodiaco
@app.route('/zodiaco', methods=['GET', 'POST'])
def zodiaco():
    nombre = apellidoP =apellidoM = edad = signo = imagen = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidoP = request.form['apellidoP']
        apellidoM = request.form['apellidoM']
        anio = int(request.form['anio'])
        edad = calcular_edad(anio)
        signo, imagen =  obtener_signo(anio)
    return render_template('zodiaco.html', nombre=nombre, apellidoP=apellidoP, apellidoM=apellidoM, edad=edad, signo=signo, imagen=imagen)

#alumnos
@app.route("/Alumnos", methods=['GET','POST'])
def alumnos():
    mat=''
    nom=''
    ape=''
    email=''
    alumno_clas=forms.UserForm(request.form)
    if request.method == 'POST':
        mat = alumno_clas.matricula.data
        nom = alumno_clas.nombre.data
        ape = alumno_clas.apellido.data
        email = alumno_clas.correo.data

        mensaje ='Bienvenido {}'.format(nom)
        flash (mensaje)#es una lista donde se muestran todos los mensajes que se van creando

    return render_template("Alumnos.html",form=alumno_clas,mat=mat,nom=nom,ape=ape,email=email)

#para la pagina de errores 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404




if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000)
