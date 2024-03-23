from flask import Flask, request, jsonify
from biseccion import biseccionProcess
import numpy as np
from numpy import *
from validateKeys import validateKeysPost
from falsePosicion import falsa_posicionProcess
import sympy as sp
from rapson import newton_raphson
from secante import secant_method
app = Flask(__name__)

@app.route('/biseccion', methods=['POST'])
def procesar_datos():
    # Verificar si la solicitud tiene datos JSON
    if not request.json:
        return jsonify({'error': 'La solicitud debe contener datos JSON'}), 400
    
    # Verificar si la solicitud contiene las claves necesarias
    required_keys = ['ecuacion', 'a', 'b']
    if not all(key in request.json for key in required_keys):
        return jsonify({'error': 'La solicitud debe contener las claves "ecuacion", "a" y "b"'}), 400
    
    # Verificar que los valores de 'a' y 'b' sean numéricos
    try:
        a = float(request.json['a'])
        b = float(request.json['b'])
    except ValueError:
        return jsonify({'error': 'Los valores de "a" y "b" deben ser numéricos'}), 400
    
    ecuacion = request.json['ecuacion']

    
    # Procesar la ecuación
    try:
        def ecuacionCallback(x):
    
            return eval(ecuacion)
        
        raiz, iteraciones = biseccionProcess(ecuacionCallback, a, b)
        resultado = {'raiz': raiz, 'iteraciones': iteraciones}
        return jsonify(resultado)
    except Exception as e:
        return jsonify({'error': str(e)}), 400



#aca ira lo de falsa posicion
@app.route('/falsePosition', methods=['POST'])
def processData():
    if not request.json:
        return jsonify({'error': 'La solicitud debe contener datos JSON'}), 400
    required_keys = ['ecuacion', 'a', 'b'] #verificamos que en nuestro json se envie esos datos
    result = validateKeysPost(required_keys,"Falto uno de los parametros del post",request)
    if result != False: return result
    try:
        a = float(request.json['a'])
        b = float(request.json['b'])
    except ValueError:
        return jsonify({'error': 'Los valores de "a" y "b" deben ser numéricos'}), 400
    
    ecuacion = request.json['ecuacion']
    try:
        def ecuacionCallback(x):
    
            return eval(ecuacion)
        
        raiz, iteraciones = falsa_posicionProcess(ecuacionCallback,a,b)
        resultado = {'raiz': raiz, 'iteraciones': iteraciones}
        return jsonify(resultado)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/raphson', methods=['POST'])
def resolverRaphson():
    data = request.json
    equation = sp.sympify(data['equation'])  # Convierte la ecuación de texto a una expresión simbólica
    variable = sp.symbols(data['variable'])  # Crea el símbolo de la variable
    x0 = data['x0']
    
    # Ejecuta el método de Newton-Raphson
    results = newton_raphson(equation, variable, x0)


    return jsonify(results)

@app.route('/secantMethod', methods=['POST'])
def resolverSecante():
    data = request.json
    equation = sp.sympify(data['ecuacion']) 
    variable = sp.symbols(data['variable'])  
    x0 = data['x0']
    x1 = data['x1']
    
    result, iterations = secant_method(equation, variable, x0, x1)

    return jsonify({"result": result, "iterations": iterations})    

    
    
    
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, timeout_keep_alive=1200)
