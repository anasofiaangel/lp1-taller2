#!/usr/bin/env python3
"""
Problema 4: Servidor HTTP básico - Cliente
Objetivo: Crear un cliente HTTP que realice una petición GET a un servidor web local
"""

import http.client

#  Definir la dirección y puerto del servidor HTTP
host = "localhost"   # o "0.0.0.0" para aceptar conexiones externas
port = 8080          # puedes cambiarlo al puerto que prefieras

# Crear servidor
server = HTTPServer((host, port), SimpleHTTPRequestHandler)

print(f"Servidor iniciado en http://{host}:{port}")
server.serve_forever()

#  Crear una conexión HTTP con el servidor
conn = http.client.HTTPConnection(host, port)
# HTTPConnection permite establecer conexiones HTTP con servidores

#  Realizar una petición GET al path raíz ('/')
# request() envía la petición HTTP al servidor
# Primer parámetro: método HTTP (GET, POST, etc.)
# Segundo parámetro: path del recurso solicitado
conn.request("GET", "/")

# Obtener la respuesta del servidor
# getresponse() devuelve un objeto HTTPResponse con los datos de la respuesta
response = conn.getresponse()

#  Leer el contenido de la respuesta
# read() devuelve el cuerpo de la respuesta en bytes
data = response.read()

#  Decodificar los datos de bytes a string e imprimirlos
# decode() convierte los bytes a string usando UTF-8 por defecto
print("Código de estado:", response.status)
print("Razón:", response.reason)
print("Contenido:", data.decode())

#  Cerrar la conexión con el servidor
conn.close()


