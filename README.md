<h1>Para usar la api rest solo son peticiones post a las endpoints siguientes</h1>
<p>/biseccion  ---> Encuentra la raiz por el metodo de biseccion</p>
<p>/falsePosition  ---> Encuentra la raiz por el metodo de falsa posicion</p>
<p>/raphson ---> Encuentra la raiz de una ecuacion usando el metodo de newtom raphson</p>
<p>/secantMethod  ---> Encuentra la raiz de una ecuacion por el metodo de la secante</p>





<h2>Parametros a enviar en el del biseccion</h2>
<p>Ejemplo de uso</p>
<pre>
{
  "ecuacion": "x**2 - 4",
  "a": 0,
  "b": 2
}
</pre>
<h2>Parametros a enviar por el metodo de falsa posicion</h2>
<p>Ejemplo de uso</p>
<pre>
{
  "ecuacion": "x**3 - 2*x - 5",
  "a": 1,
  "b": 3
}
</pre>
<h2>Parametros a enviar por el metodo de newton rapson</h2>
<p>Ejemplo de uso</p>
<pre>
{
  "equation": "x**2 - 4",
  "variable": "x",
  "x0": 2
}
</pre>

<h2>Parametros a enviar por el metodo de la secante</h2>
<p>Ejemplo de uso</p>
<pre>
{
  "ecuacion": "x**3 - 4*x**2 + 3*x - 6",
  "variable": "x",
  "x0": 2.0,
  "x1": 3.0
}
</pre>

<h1>nomenclatura de las ecuaciones</h1>
<h2>tipo:  x**n = x^n</p>
<h3>Ejemplos</h3>
<p>x**2 = x^2</p>
<p>x**3 = x^3</p>
<h2>tipo: n*x = nx</p>
<h3>Ejemplos:</h3>
<p>2*x</p>
<p>4*x</p>
<h2>funciones trigonometrica</h2>
<p>Uso</p>
<p>sin(x)</p>
<p>cos(x)</p>
<p>tan(x)</p>
<h2>Ejemplo con euler</h2>
<p>3*e</p>
<p>e + 1</p>
<p>Nota: pueden existir mas forma de ecuaciones pero ya es de probarse XD</p>


