import sympy as sp
from flask import Flask, jsonify

def secant_method(equation, variable, x0, x1, tol=1e-6, max_iter=50):
    results = []
    iter = 0
    x = variable
    f = equation
    while iter < max_iter:
        fx0 = f.evalf(subs={x: x0})
        fx1 = f.evalf(subs={x: x1})
        result = {"iteracion": str(iter), "x0": str(round(x0, 6)), "x1": str(round(x1, 6)), "f(x0)": str(round(fx0, 6)), "f(x1)": str(round(fx1, 6))}
        results.append(result)
        if abs(fx1) < tol:
            return str(round(x1, 6)), results
        if fx1 - fx0 == 0:
            return None, results
        x_next = x1 - ((fx1 * (x1 - x0)) / (fx1 - fx0))
        x0 = x1
        x1 = x_next
        iter += 1
    return str(round(x1, 6)), results