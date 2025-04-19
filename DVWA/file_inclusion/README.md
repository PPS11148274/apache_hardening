# File inclusion
Una vulnerabilidad **File Inclusion** se produce cuando una aplicación web incorpora archivos externos en sus operaciones basadas en la entrada proporcionada por el usuario sin validar adecuadamente la entrada. \
Esto puede permitir a los atacantes manipular el contenido de los archivos incluidos o incluso ejecutar código malicioso.
En esta sección se ejemplifica un ataque aprovechado esta vulnerabilidad.
## Level: Low and Medium
Se accede a la opción correspondiente (File Inclusion) y se ve que se pueden elegri entre tres archivos. \
En al parámetro **page** aparece el nombre del archivo, y esto se puede modificar para mostrar lo que el atacante desee.

![Acceso file include](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/file_inclusion/asset/Inicio%20file%20include.png)

![Carga file1](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/file_inclusion/asset/file1.png) 

En la barra de direcciones se cambia el parámetro **page** y se pone el que se quiere ver, en este ejempo: **/etc/passwd.** \
Como se ve en la imagen siguiente, se muestra el contenido del archivo deseado.

![Muestra /etc/passwd](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/file_inclusion/asset/passwd.png)

## Level: Medium

En este nivel, DVWA intenta eliminar todas las cadenas que se ajustan al formato http://, https://, ../ o ..\., así se protegen contra la inclusión de archivos remotos con las dos primeras cadenas y contra la inclusión de archivos locales con las dos últimas. \
La función utilizada para validar las entradas (str_replace()) es sensible a las mayúsculas, así que se puede usar HTTP en vez de http. \

Esta acción es útil si se quiere ejecutar un archivo, si se quiere ejecutar un comando como en el nivel Low, no es necesario modificar nada, \
funciona exactamente igual.

## Mitigación
  - Validación y sanitización estrica de las entradas.
  - Normalización de rutas.
  - Desactivar RFI (allow_url_include=Off) en php.ini.
  - Configuración de PHP (open_basedir) para restringir los directorios accesibles por PHP.
  - Restringir permisos.
  - Configurar WAF.


