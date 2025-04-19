# Command Injection
## En esta sección se trata de llevar a cabo un ataque del tipo Commnad Injection sobre el servidor DVWA. 
## Nivel-LOW
El Command Injection es un tipo de vulnerabilidad de seguridad que permite a un atacante ejecutar comandos arbitrarios en el sistema operativo del servidor a través de una aplicación vulnerable. 

Se elige la opción correspondiente en el menú.\
Como se ve en la imagen, se intenta acceder a archivo passwd del servidor enviando el comando **192.168.0.35; cat /etc/passwd** a través del formulario.\
Esto es posible porque el servidor permite enviar pings y no tiene una validación adecuada.\
La IP introducida corresponde con la del servidor DVWA.
![Ataque Commnad Injection](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/commnad_injection/asset/command_injection.png)\
Se podría acceder a otros archivos e incluso borrarlos o modificarlos.

## Nivel: Medium

En este caso DVWA introduce un protección básica. Filtra las entradas buscando **&&** y **;** para eliminarlas. \
Pero no detecta **&**, así que se usará este parámetro. Se prueba un comando muy similar al anterior pero con **&**, que no es filtrado.

```
127.0.0.1 & cat /etc/passwd
```

![Command Injection Medium](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/commnad_injection/asset/com_injection_med.png)


