# Preparación del entorno
## En este trabajo se va a instalar un servidor con múltiple vulnerabilidades con el objetivo de analizarlarlas por separado y ver como se comportan. Se Emplean diferentes niveles de dificultad.
En primer se clona el repositorio del servidor DVWA desde https://github.com/digininja/DVWA.git.\
Se mueve ahora el contenido de la carpeta creada (DVWA) a la carpeta del servidor apache y se modifica el nombre del archivo de configuración de la distribución.
```
sudo mv DVWA /var/www/html
sudo cp /var/www/html/DVWA/config/config.inc.php.dist config.inc.php
```
A continuación se inicia apache y mariadb.
```
sudo systemctl start apache2
sudo systemctl start mariadb
```
Una vez hecho esto se crea la Base de Datos, usuario y contraseña como se ve en la imagen inferior.\
![Crea base de datos](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/asset/crea_bd.png)
Ahora ya se puede acceder al servidor DVWA desde el navegador como se ve.\
![Acceso al servidor DVWA](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/asset/acceso_DVWA.png)\
El último paso una vez preparado todo el entorno es entrar al servidor con las credenciales (admin/password).
![Servidor DVWA](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/asset/DVWA.png)\
