# RA3_3 Reglas OWASP

INTRODUCCIÓN:
Pero la OWASP provee una configuración por defecto que incluye una protección para las reglas más comunes. Así que lo mejor es empezar por este conjunto de reglas y luego ir añadiendo las propias.
Una solución de compromiso para no dar todas las reglas, se muestra una configuración que tiene OWASP. Para instalarlo en nuestro servidor.
# Carga la imagen desde hub docker
```
$ docker pull 11148274/owasp:latest
```
# Lanza el contenedor
```
$ sudo docker run --detach --rm -p 8080:80 -p 8181:443 --name="owasp" owasp
```
