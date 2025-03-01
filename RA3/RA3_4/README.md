# RA3_4 Evitar ataques DDoS

INTRODUCCIÓN:
Apache nos provee con un módulo llamado mod_evasive que permite evitar ataques de denegación de servicio (DoS) mediante el escaneo constante de los conexiones entrantes que serán baneadas en el momento que se alcance el umbral establecido en la configuración del módulo. 
# Carga la imagen desde hub docker
```
$ docker pull 11148274/evasive:latest
```
# Lanza el contenedor
```
$ sudo docker run --detach --rm -p 8080:80 -p 8181:443 --name="evasive" evasive
```
