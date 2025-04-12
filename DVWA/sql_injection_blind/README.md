# SQL Injection (blind)
Este ejercicio es muy similar a SQL injection, salvo que en este caso hacen preguntas de verdadero o falso a la BD. \
La información, se deduce de la respuesta de la BD. \
Este ataque se utiliza a menudo cuando la aplicación web está configurada para mostrar mensajes de error genéricos, \
pero no ha sanitizado las entradas de formularios. Cuando un atacante explota la inyección SQL, \
a veces la aplicación web muestra mensajes de error de la base de datos quejándose de que la sintaxis de la consulta SQL es incorrecta. \
La inyección SQL "blind" es casi idéntica a la inyección SQL normal, la única diferencia es la forma en que se recuperan los datos de la base de datos. \
Cuando la base de datos no envía datos a la página web, se puede utilizar este método. \ 
Esto hace que explotar la vulnerabilidad de inyección SQL sea más difícil, pero no imposible.
## Nivel: Low
En este caso entramos en la opción correspondiente y colocamos el comando:
```
1’ and sleep(5)#
```
La BD tardará 5 segundos en responder, si es así se puede obtener información de la BD. \
Se puede averiguar así la longitud del nombre de la base de datos probando estos comandos:
```
1’ length(database)())=’1
```
Se va cambiando el segundo “1” por (2,3,4,5…) hasta encontrar uno que de positivo, como se ve en la imagen siguiente (enmarcado en rojo).
![Resultado SQL injection blind] (https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/sql_injection_blind/asset/result_sql_blind.png). \



