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
En la imagen siguiente se ve el resultado que produce

