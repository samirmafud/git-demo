from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Bienvenidos al proyecto de demostración Control de Repositorios con Gitflow"

@app.route('/hello')
def greeting():
    return "Hola mundo"

@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
    nums_sum = a + b
    return f"La suma de los dos números es: + {str(nums_sum)}"