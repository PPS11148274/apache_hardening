# Hardening de un servidor Apache

INTRODUCCIÓN:
En este ejercicio se llevan a cabo diferentes configuraciones en el servidor Apache para evitar diferentes vulnerabilidades
# Carga la imagen desde hub docker
```
$ docker pull 11148274/best_practices:latest
```
# Lanza el contenedor
```
$ sudo docker run --detach --rm -p 8080:80 -p 8181:443 --name="best_practices" bestpractices
```
