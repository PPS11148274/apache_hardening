# Instalación de certificado en servidor Apache

INTRODUCCIÓN:
En este ejercicio se instala un certificado autofirmado para el servidor Apache
# Carga la imagen desde hub docker
```
$ docker pull 11148274/certificado:latest
```
# Lanza el contenedor
```
$ sudo docker run --detach --rm -p 8080:80 -p 8181:443 --name="certificado" certificado
```
