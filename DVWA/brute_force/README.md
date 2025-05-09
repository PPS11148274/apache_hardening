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
![Lanza comando hidra](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/brute_force/asset/comando_hydra.png) \
En la imagen anterior se ve el comando hydra en funcionamiento. El problema es que tras varias horas no ha conseguido las credenciales. \
Tal vez con otro equipo más potente se pueda acelerar el proceso. \
Como esto no funciona, se prueba una alternativa con una SQL injectión, se pone el comando SQL y cualquier contraseña aleatoria, como se ve a continuación.
![SQL_injection brute force](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/brute_force/asset/SQL_injection.png)
Se ve el acceso permitido en la imagen siguiente.
![Acceso permitido](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/brute_force/asset/Brute_OK.png)

## Mitigación

Para prevenir esta vulnerabilidad:

  - Implementar CAPTCHA.
  - Limitar intentos fallidos y bloquear IPs temporalmente.
  - Usar autenticación de dos factores (2FA).
  - Aplicar un delay incremental entre intentos fallidos.
