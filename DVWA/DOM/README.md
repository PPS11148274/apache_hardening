# Brute Force
## Esta sección del trabajo consiste en intentar entrar en el sistema mediante la furza bruta utilizando hydra.


En primer se clona el repositorio del servidor DVWA desde https://github.com/digininja/DVWA.git.\ Se mueve ahora el contenido de la carpeta creada (DVWA) a la carpeta del servidor apache y se modifica el nombre del archivo de configuración de la distribución.

sudo mv DVWA /var/www/html
sudo cp /var/www/html/DVWA/config/config.inc.php.dist config.inc.php

A continuación se inicia apache y mariadb.

sudo systemctl start apache2
sudo systemctl start mariadb

Una vez hecho esto se crea la Base de Datos, usuario y contraseña como se ve en la imagen inferior.
