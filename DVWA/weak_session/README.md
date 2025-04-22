# Weak Session
La vulnerabilidad de los identificadores de sesión débiles pone de manifiesto los riesgos de seguridad asociados a estos identificadores predecibles o fáciles de adivinar,
que permiten a los atacantes secuestrar o suplantar sesiones activas adivinando o forzando las cookies de sesión válidas.

## Level: Low

Se accede a la opción Weak Session IDs y se genera una nueva sesión.

![Genera sesión](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/weak_session/asset/genera_sesion.png)

Como se puede ver en la siguiente imagen, si se generan más sesiones, las numera de uno en uno.

![Neva sesión](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/weak_session/asset/nueva_sesion.png)

## Level: Medium

En este caso, al generar nuevas sesiones, ya no se numeran de uno en uno, si no con un número bastante largo.

![Nueva sesión](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/weak_session/asset/gnera_medium_1.png)

![Otra sesión](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/weak_session/asset/genera_medium_2.png)

Si se observa el número con detenimiento, se puede var que es el código de tiempo utilizado por Unix \
Como se conoce la lógica detrás de la generación de la cookie de sesión, se puede adivinar la sesión del usuario víctima,
generando el valor de la cookie según el **timestamp** de Unix.
