# RA3_3 Reglas OWASP

INTRODUCCIÓN:
Pero la OWASP provee una configuración por defecto que incluye una protección para las reglas más comunes. Así que lo mejor es empezar por este conjunto de reglas y luego ir añadiendo las propias.
Una solución de compromiso para no dar todas las reglas, se muestra una configuración que tiene OWASP. Para instalarlo en nuestro servidor.
# Archivo dockerfile para construir la imagen
```
FROM waf:latest
# el modulo modsecurity se ha cargado en la imagen base
#crea el directorio rules
#RUN mkdir /etc/modsecurity/rules
#copia el archivo de setup de crs
COPY /etc/modsecurity/crs-setup.conf /etc/modsecurity/crs-setup.conf 
#Copia el archivo de configuración security2.conf
COPY /etc/apache2/mods-enabled/security2.conf /etc/apache2/mods-enabled/security2.conf
#copia el archivo del servidor por defecto 000-default.conf
COPY /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/000-default.conf
# copia las reglas
#COPY  /home/joseadmin/owasp-modsecurity-crs/rules/*.* /etc/modsecurity/rules
#asigna permisos
RUN chown -R www-data:www-data /var/www/html
RUN chown -R www-data:www-data /etc/modsecurity
RUN chmod -R 775 /var/www/html
RUN chmod -R 775 /etc/modsecurity
#expone los puertos
EXPOSE 80
EXPOSE 443
#ejectua apache ne primer plano
CMD ["apache2ctl", "-D", "FOREGROUND"]
``` 
# Carga la imagen desde hub docker
```
$ docker pull 11148274/owasp:latest
```
# Lanza el contenedor
```
$ sudo docker run --detach --rm -p 8080:80 -p 8181:443 --name="owasp" owasp
```
