# Command Injection
## En esta sección se trata de llevar a cabo un ataque del tipo Commnad Injection sobre el servidor DVWA.
Se elige la opción correspondiente en el menú.\
Como se ve en la imagen, se intenta acceder a archivo passwd del servidor enviando el comando **192.168.0.35; cat /etc/passwd** a través del formulario.\
Esto es posible porque el servidor permite enviar pings y no tiene una validación adecuada.\
La IP introducida corresponde con la del servidor DVWA.
![Ataque Commnad Injection](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/commnad_injection/asset/command_injection.png)\
Se podría acceder a otros archivos e incluso borrarlos o modificarlos.


