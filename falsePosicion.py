def falsa_posicionProcess(ecuacion, a, b, tol=1e-6, max_iter=100):
    # Variable para contar el número de iteraciones
    iteracion = 0
    # Lista para almacenar los datos de cada iteración
    iteraciones = []

    # Aplicar el método de la falsa posición
    while iteracion < max_iter:
        iteracion += 1

        # Calcular el valor de la función en los extremos del intervalo
        fa = ecuacion(a)
        fb = ecuacion(b)

        # Calcular la siguiente aproximación de la raíz mediante la interpolación lineal
        x = a - (fa * (b - a)) / (fb - fa)
        fx = ecuacion(x)

        # Guardar datos de la iteración en la lista
        iteraciones.append({
            "iteracion": iteracion,
            "a": a,
            "b": b,
            "x": x,
            "fx": fx
        })

        # Comprobar si se ha encontrado una solución aceptable
        if abs(fx) < tol:
            return x, iteraciones

        # Actualizar los extremos del intervalo para la siguiente iteración
        if fa * fx < 0:
            b = x
        else:
            a = x

    # Si se alcanza el número máximo de iteraciones sin convergencia
    print("El método de la falsa posición no convergió después de", max_iter, "iteraciones.")
    return None, iteraciones

