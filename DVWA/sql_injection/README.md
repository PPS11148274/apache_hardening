# SQL Injection
Este ejercicio consiste en aprovechar la falta de sanitización en las entradas de formularios para inyectar
código SQL.
## Nivel: Low
Se accede desde el botón correspondiente (SQL injection) al formulario de entrada. Desde aquí se puede injectar el código
SQL deseado. \
Una muestra de esto, es buscar los usuarios y contraseñas del sistema en la BD. Para eso, en la entrada del formulario se coloca esto:
```
‘ UNION SELECT user, password FROM users#
```
En la imagen siguiente se ve el resultado que produce este comando SQL. \
![Resulado SQL injection](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/sql_injection/asset/resultado_SQL_injection.png) \
Como se ve en la imagen, se obtienen los nombres y el hash de la contraseña.
## Nivel: Medium
El nivel medio utiliza una forma de protección contra inyecciones SQL, con la función mysql_real_escape_string(). \
Sin embargo, debido a que la consulta SQL no tiene comillas alrededor del parámetro, esto no protegerá completamente la consulta de ser alterada. \
El cuadro de texto se ha sustituido por una lista desplegable predefinida y utiliza POST para enviar el formulario.
