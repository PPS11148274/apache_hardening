# RA3_2 WAF Web application Firewall

INTRODUCCIÓN:
Un firewall de aplicaciones web (WAF) es un tipo de firewall que supervisa, filtra o bloquea el tráfico HTTP hacia y desde una aplicación web. Se diferencia de un firewall normal en que puede filtrar el contenido de aplicaciones web específicas, mientras que un firewall de red protege el tráfico entre los servidores. Al inspeccionar el tráfico HTTP un WAF protege a las aplicaciones web contra ataques como los de inyección SQL, XSS y falsificación de petición de sitios cruzados (CSRF).

# Carga la imagen desde hub docker
```
$ docker pull 11148274/waf:latest
```
# Lanza el contenedor
```
$ sudo docker run --detach --rm -p 8080:80 -p 8181:443 --name="waf" waf
```
