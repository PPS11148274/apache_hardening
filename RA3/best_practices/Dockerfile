FROM owasp:latest
#Desactiva autoindex
RUN a2dismod autoindex -f
#carga los módulos necesarios
RUN a2enmod ssl
#crea directorio para certificados
RUN mkdir /etc/apache2/ssl
#copia los certificados
COPY /etc/apache2/ssl/website.crt /etc/apache2/ssl/website.crt
COPY /etc/apache2/ssl/website1.key /etc/apache2/ssl/website1.key
#copia los archivos de configuración
COPY /etc/apache2/sites-available/website1.conf /etc/apache2/sites-available/website1.conf
COPY /etc/apache2/apache2.conf /etc/apache2/apache2.conf
#asigna los permisos necesarios
RUN groupadd apache 
RUN useradd -g apache apache
RUN chown -R apache:apache /var/www
RUN chmod -R 775 /var/www
RUN chown -R apache:apache /etc/apache2
#Carga el sitio seguro www.website1.com 
RUN a2ensite website1.conf
#expone los puertos

EXPOSE 80
EXPOSE 443
#ejectua apache ne primer plano
CMD ["apache2ctl", "-D", "FOREGROUND"]

