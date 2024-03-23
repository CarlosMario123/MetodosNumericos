from scipy.optimize import bisect
def biseccionProcess(ecuacion, a, b):
    # Variable para contar el número de iteraciones
    iteracion = 0
    xa = 0
    xb = 0
    # Lista para almacenar los datos de cada iteración
    iteraciones = []

    def funcion(x):
        nonlocal iteracion, xa, xb
        iteracion += 1
        fxp = 0

        if iteracion <= 2:
            xa = a
            xb = b
        else:
            xp = (xa + xb) / 2
            fxp = ecuacion(xp)
            if fxp < 0:
                xa = x
            else:
                xb = x

        # Guardar datos de la iteración en la lista
        iteraciones.append({
            "iteracion": iteracion,
            "xa": xa,
            "xb": xb,
            "x": x,
            "fxp": fxp
        })

        result = ecuacion(x)
        return result

    # Aplicar el método de bisección
    raiz = bisect(funcion, a, b)

    return raiz, iteraciones
