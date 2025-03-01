FROM owasp:latest
#crea el directorio de logs
RUN mkdir /var/log/mod_evasive
# instala el modulo mod_evasive
RUN apt install libapache2-mod-evasive -y
#copia el archivo de configuración ya modificado
COPY /etc/apache2/mods-enabled/evasive.conf /etc/apache2/mods-enabled/evasive.conf  
#asigna permisos
RUN chown -R www-data:www-data /var/log/mod_evasive
#expone los puertos
EXPOSE 80
EXPOSE 443
#ejectua apache ne primer plano
CMD ["apache2ctl", "-D", "FOREGROUND"]

