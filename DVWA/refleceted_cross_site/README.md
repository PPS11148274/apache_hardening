# Reflected Cross Site
El XSS Reflected (Cross-Site Scripting Reflejado) es un tipo de vulnerabilidad de seguridad web donde un atacante inyecta código malicioso que es ejecutado por el navegador de la víctima, pero el código proviene de una respuesta del servidor que "refleja" la entrada proporcionada por el usuario sin la debida sanitización.

## Level: Low
En este nivel de seguriad, es suficiente con introducir el script en el dialogo para que se ejecute. El script introducido, \
genera un cuadro de dialogo con una alerta.
```
<script>alert("Te pillé")</script>
```
![Ejecuta script low](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/refleceted_cross_site/asset/ejecuta_script_low.png)
## Level: Medium

En este nivel DVWA introduce un control de entradas muy básico, no se puede utilizar <script> pero si que se puede utilizar <SCRIPT>. \
Esto es debido a que la función utilizada **str_replace()** para el filtrado es sensible a las mayúsculas/minúsculas, se introduce en el dialogo:
```
<SCRIPT>alert("Te pillé")</SCRIPT>
```
![Ejecuta script malicioso](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/refleceted_cross_site/asset/ejecuta_script.png)
## Mitigación
  - Sanitización y validación de entradas.
  - Codificación de salida (Output Encoding).
  - Cabeceras HTTP de seguridad.
  - Implementación de CSP (Content Security Policy).


