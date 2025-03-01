# RA3_1 CSP


INTRODUCCIÓN:
Política de Seguridad del Contenido o ( CSP ) ‑ del inglés Content Security Policy ‑ es una capa
de seguridad adicional que ayuda a prevenir y mitigar algunos tipos de ataque, incluyendo Cross
Site Scripting ( XSS ) y ataques de inyección de datos. Estos ataques son usados con diversos
propósitos, desde robar información hasta desfiguración de sitios o distribución de malware.
En esta tarea se añadira la política a un serividor Apache.

# Aplica HSTS

* Eliminar autoindex para que no aparecta ningún resultado si el recurso no se encuentra:
```
 $ sudo a2dismod autoindex -f
```
* Eliminar información del servidor modificando en el archivo /etc/apache2/apache2.conf
 ```
 Servertokens ProductOnly
 ServerSignature Off
```
# fuerza la conexión HTTPS
Habilitar el módulo Headers y el módulo ssl
```
$ Sudo a2enmod headers
$ sudo a2enmod ssl
```


Intro...

![IMG](URL_IMG)

Example code:

```
$ git clone https://github.com/openssh/openssh-portable
$ patch -p1 < ~/path/to/openssh.patch
$ autoreconf
$ ./configure
$ make
```

# Task_2
