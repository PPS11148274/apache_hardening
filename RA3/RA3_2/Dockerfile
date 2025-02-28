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

