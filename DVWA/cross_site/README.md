poner en nivel Low # CSRF
El cross-site request forgery (CSRF) consiste en realizar tareas dentro de una aplicación por medio de la ejecución de un enlace en el navegador de la víctima. \
Se envía un enlace que se crea a partir de una petición que contiene la acción maliciosa planeada por el atacente. \
El siguiente códio HTML contiene la acción maliciosa que cambiará la contraseña automáticamente a (12345) al pinchar en el enlace.
## Nivel: Low
```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=dwvice-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<h3>Click to download FIFA 2023</h3>
	<a href="http://localhost/DVWA/vulnerabilities/csrf/?password_new=12345&password_conf=12345&Change=Change#">FIFA 2023</a>
</body>
</html>
```
![Inicio CSRF](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/cross_site/asset/CSRF_cambio_contrase%C3%B1a.png) \
Como se ve en la imagen, en la barra de direcciones aparece la contraseña que el usuario ha cambiado "perico", que luego cambia el atacante con su código malicioso.

![Enlace malicioso](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/cross_site/asset/enlace_malicioso.png)
## Nivel: Medium

El nuevo código comprueba si la cabecera HTTP-Referer coincide con el nombre del servidor (es decir, la petición HTTP «procede» del mismo servidor que la página recién solicitada). Si es así, asume que la petición es válida y continúa. En caso contrario, produce un error. \
Para solucionar esta protección se puede averiguar el "referer" usando **Burp Suite**, pero lo que se hará aquí,
es cargar el archivo fifa.html desde "File Upload" y ejecutarlo después. (se debe poner el nivel Low para cargarlo, luego se cambia a medium nuevamente).

![Programa malicioso](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/cross_site/asset/CSRF_cambio_contras_medium.png)

Al pinchar en el enlace se cambia la contraseña automáticamente a "12345".

![Cambia la contraseña](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/cross_site/asset/cambio_contrasena_medium.png)

Se puede comprobar con el botón "Test credentials" que la contraseña "password" ya no funciona, funciona "12345".

## Mitigación
  - Validación y sanitización de entradas.
  - Escapado de datos (Output Encoding).
  - Uso de Content Security Policy (CSP).
  - Configura WAF.
  - Configurar Cabeceras HTTP de Seguridad.

