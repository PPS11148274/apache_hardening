# RA3_1 CSP


INTRODUCCIÓN:
Política de Seguridad del Contenido o ( CSP ) ‑ del inglés Content Security Policy ‑ es una capa
de seguridad adicional que ayuda a prevenir y mitigar algunos tipos de ataque, incluyendo Cross
Site Scripting ( XSS ) y ataques de inyección de datos. Estos ataques son usados con diversos
propósitos, desde robar información hasta desfiguración de sitios o distribución de malware.
En esta tarea se añadira la política a un serividor Apache.

# Carga la imagen desde hub docker
```
$ docker pull pps11148274/hardenowasp:latest
```
# Lanza el contenedor
```
$ sudo docker run --detach --rm -p 8080:80 -p 8181:443 --name="harnowasp" hardenowasp
```
