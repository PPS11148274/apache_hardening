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
