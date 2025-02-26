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

