# XSS (DOM)

XSS DOM (Cross-Site Scripting basado en DOM) es un tipo de vulnerabilidad de seguridad que se explota en el lado del cliente, específicamente en el Document Object Model (DOM) del navegador web, sin que el ataque pase por el servidor.

## Level: Low
### Características del XSS DOM en DVWA

En el servidor **DVWA** el **XSS DOM** es una vulnerabilidad intencional que permite:

    - El ataque se produce cuando JavaScript modifica dinámicamente el DOM basado en entradas no validadas.

    - A diferencia de XSS reflejado o almacenado, este tipo no envía el script malicioso al servidor.

En primer lugar, se accede a la opción adecuada (XSS DOM) y se selecciona el idioma.

![Selección Idioma](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/DOM/asset/seleccion_idioma.png)

Como se ve en la barra de direcciones, aparece el idioma seleccionado en el parámetro "default".
Se puede insertar un script en ese parámetro, como el siguiente:

```
<script>alert('Nos la han colado')</script>
```

![Inserta script](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/DOM/asset/inserta_script.png)

En la siguiente imagen se ve el script funcionando.

![Script funcionando](https://github.com/PPS11148274/apache_hardening/blob/main/DVWA/DOM/asset/script_funcionando.png)

## Mitigación
Se pueden tomar varias medidas para prevenir esta vulnerabilidad, como son:

  - Validar y sanitizar todas las entradas del cliente

  - Usar textContent en lugar de innerHTML

  - Implementar CSP (Content Security Policy)

  - Codificar adecuadamente los datos antes de insertarlos en el DOM

