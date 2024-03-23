import sympy as sp
from flask import Flask, jsonify

def newton_raphson(equation, variable, x0, tol=1e-6, max_iter=50):
    results = []
    iter = 0
    x = variable
    f = equation
    df = sp.diff(equation, variable)
    while iter < max_iter:
        fx = f.evalf(subs={x: x0})
        dfx = df.evalf(subs={x: x0})
        result = {"iteracion": str(iter), "x": str(round(x0, 6)), "f(x)": str(round(fx, 6)), "dx(x)": str(round(dfx, 6))}
        results.append(result)
        if abs(fx) < tol:
            return str(round(x0, 6)), results
        if dfx == 0:
            return None, results
        x0 = x0 - fx / dfx
        iter += 1
    return str(round(x0, 6)), results
