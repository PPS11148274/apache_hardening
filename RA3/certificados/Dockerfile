FROM ubuntu/apache2:latest
#carga los módulos necesarios
RUN a2enmod ssl
#crea directorio para certificados
RUN mkdir /etc/apache2/ssl
#copia los certificados
COPY /etc/apache2/ssl/apache.crt /etc/apache2/ssl/apache.crt
COPY /etc/apache2/ssl/apache.key /etc/apache2/ssl/apache.key
#copia el archivo de configuración
COPY /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
#asigna los permisos necesarios
RUN chown -R www-data:www-data /var/www
RUN chmod -R 775 /var/www
#Carga el sitio seguro www.dominioseguro.com cargando el default-ssl.conf
RUN a2ensite default-ssl.conf
#expone los puertos

EXPOSE 80
EXPOSE 443
#ejectua apache ne primer plano
CMD ["apache2ctl", "-D", "FOREGROUND"]

