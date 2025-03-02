# RA3_1 CSP


INTRODUCCIÓN:
Política de Seguridad del Contenido o ( CSP ) ‑ del inglés Content Security Policy ‑ es una capa
de seguridad adicional que ayuda a prevenir y mitigar algunos tipos de ataque, incluyendo Cross
Site Scripting ( XSS ) y ataques de inyección de datos. Estos ataques son usados con diversos
propósitos, desde robar información hasta desfiguración de sitios o distribución de malware.
En esta tarea se añadira la política a un serividor Apache.
#### En primer lugar es necesario crear en _/etc/apache2/sites-available_ el archivo de configuración de nuestro sitio website1.conf e introducir las siguientes modificaciones
<image src="/RA3/RA3_1/header y ssl.png" alt="Modificación del archivo website1.conf">
<p>Habilita módulos header y ssl </p>
<p>Con los siguientes comando se habilitan los módulos necesarios para esta práctica</p>

* $ sudo a2enmod headers
* $ sudo a2enmod ssl

  
# Archivo dockerfile
Con el siguiente dockerfile se construye la imagen necesaria para el despliegue
```
FROM ubuntu/apache2:latest
# copia los ficheros de configuración de los sitios
COPY /etc/apache2/sites-available/website1.conf /etc/apache2/sites-available/website1.conf
COPY /etc/apache2/sites-available/website2.conf /etc/apache2/sites-available/website2.conf
COPY /etc/apache2/apache2.conf                  /etc/apache2/apache2.conf
#carga los módulos necesarios
RUN a2enmod ssl
RUN a2enmod headers
RUN a2dismod -f autoindex
RUN a2ensite website1.conf
RUN a2ensite website2.conf
#copia los certificados
COPY /etc/ssl/certs/clavedocker.crt /etc/ssl/certs/clavedocker.crt
COPY /etc/ssl/private/clavedocker.key /etc/ssl/private/clavedocker.key
#copia el contenido de los sitios
COPY /var/www/website1 /var/www/website1/
COPY /var/www/website2 /var/www/website2/
#asigna los permisos necesarios
RUN chown -R www-data:www-data /var/www
RUN chmod -R 775 /var/www
#expone los puertos
EXPOSE 80
EXPOSE 443
#ejectua apache ne primer plano
CMD ["apache2ctl", "-D", "FOREGROUND"]
```

# Carga la imagen desde hub docker
```
$ docker pull pps11148274/hardenowasp:latest
```
# Lanza el contenedor
```
$ sudo docker run --detach --rm -p 8080:80 -p 8181:443 --name="harnowasp" hardenowasp
```
