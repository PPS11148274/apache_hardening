# RA3_4 Evitar ataques DDoS

INTRODUCCIÓN:
Apache nos provee con un módulo llamado mod_evasive que permite evitar ataques de denegación de servicio (DoS) mediante el escaneo constante de los conexiones entrantes que serán baneadas en el momento que se alcance el umbral establecido en la configuración del módulo. 
# Archivo dockerfile para construir la imagen
```
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
``` 
# Carga la imagen desde hub docker
```
$ docker pull 11148274/evasive:latest
```
# Lanza el contenedor
```
$ sudo docker run --detach --rm -p 8080:80 -p 8181:443 --name="evasive" evasive
```
