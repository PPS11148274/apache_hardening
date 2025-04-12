# Brute force
En este ejercicio se trata de vulnerar las credenciales del servidor DVWA utilizando la herramienta de Kali Hydra.
## Nivel: Low
Se accede desde la página inicial de DVWA al botón "Brute Force" y se pone cuaquier cosa para ver exactamente el mensaje de error generado,
que hará falta con posterioridad.\
![Home de DVWA con brute force](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/brute_force/asset/p_inicio_BF.png) \
En la imagen anterior se ve (en rojo) el mensaje de error generado. Además, en la parte inferior derecha se puede ver el identificador
de sesión de la cookie (PHPSESSID), este código es necesario para el comando hydra. \
En la siguiente imagen se ve enmarcado en rojo el comando hydra necesario. Se debe sustituir el identificado PHPSESSID por el que te proporcione
tu navegador.

