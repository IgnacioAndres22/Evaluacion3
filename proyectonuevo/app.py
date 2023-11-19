from flask import Flask, render_template, request

app = Flask(__name__)
#ruta principal en este caso main
@app.route('/')
def main():
    return render_template('main.html')
#ejercicio 1
@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')
#Calcula el promedio
@app.route('/calcular_promedio', methods=['POST'])
def calcular_promedio():
    nota1 = float(request.form['nota1'])
    nota2 = float(request.form['nota2'])
    nota3 = float(request.form['nota3'])
    asistencia = float(request.form['asistencia'])
    promedio = (nota1 + nota2 + nota3) / 3
    estado = 'Aprobado' if promedio >= 40 and asistencia >= 75 else 'Reprobado'

    return render_template('ejercicio1.html', resultado=f'Promedio: {promedio}, Estado: {estado}')
#ejercicio2
@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')
#comprueba cual nombre es mas largo
@app.route('/comparar_nombres', methods=['POST'])
def comparar_nombres():
    nombre1 = request.form['nombre1']
    nombre2 = request.form['nombre2']
    nombre3 = request.form['nombre3']

    # Encuentra el nombre más largo y la cantidad de caracteres
    nombres = [nombre1, nombre2, nombre3]
    nombre_mas_largo = max(nombres, key=len)
    longitud_mas_larga = len(nombre_mas_largo)

    return render_template('ejercicio2.html', resultado=f'El nombre más largo es: {nombre_mas_largo}, con {longitud_mas_larga} caracteres.')

if __name__ == '__main__':
    app.run(debug=True)