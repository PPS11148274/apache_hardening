# RA3_2 WAF Web application Firewall

INTRODUCCIÓN:
Un firewall de aplicaciones web (WAF) es un tipo de firewall que supervisa, filtra o bloquea el tráfico HTTP hacia y desde una aplicación web. Se diferencia de un firewall normal en que puede filtrar el contenido de aplicaciones web específicas, mientras que un firewall de red protege el tráfico entre los servidores. Al inspeccionar el tráfico HTTP un WAF protege a las aplicaciones web contra ataques como los de inyección SQL, XSS y falsificación de petición de sitios cruzados (CSRF).
# Archivo dockerfile para construir la imagen
```
FROM hardenowasp:latest
# instala el modulo modsecurity
RUN apt update 
RUN apt install -y libapache2-mod-security2
#carga los módulos necesarios
RUN a2enmod security2
#copia el archivo de onfiguración modsecurity.conf modificado
COPY /etc/modsecurity/modsecurity.conf /etc/modsecurity/modsecurity.conf
#Copia el post.php
COPY /var/www/html/post.php /var/www/html/post.php
#cambia permisos y propietario de post.php
RUN chown -R www-data:www-data /var/www/html
RUN chmod -R 775 /var/www/html
#expone los puertos
EXPOSE 80
EXPOSE 443
#ejectua apache ne primer plano
CMD ["apache2ctl", "-D", "FOREGROUND"]
``` 
# Carga la imagen desde hub docker
```
$ docker pull 11148274/waf:latest
```
# Lanza el contenedor
```
$ sudo docker run --detach --rm -p 8080:80 -p 8181:443 --name="waf" waf
```
