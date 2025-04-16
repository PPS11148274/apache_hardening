# File inclusion
Una vulnerabilidad de inclusión de archivos se produce cuando una aplicación web incorpora archivos externos en sus operaciones basadas en la entrada proporcionada por el usuario sin validar adecuadamente la entrada. \
Esto puede permitir a los atacantes manipular el contenido de los archivos incluidos o incluso ejecutar código malicioso.
En esta sección se ejemplifica un ataque aprovechado esta vulnerabilidad.
## Level: Low and Medium
Se accede a la opción correspondiente (File Inclusion) y se ve que se pueden elegri entre tres archivos. \
En al parámetro **page** aparece el nombre del archivo, y esto se puede modificar para mostrar lo que el atacante desee.


