#!/usr/bin/env python3
"""
Problema 2: Comunicación bidireccional - Cliente
Objetivo: Crear un cliente TCP que envíe un mensaje al servidor y reciba la misma respuesta
"""

import socket

# Definir la dirección y puerto del servidor
server_address = ('localhost', 65432)  # Cambia según tu servidor
# Solicitar mensaje al usuario por consola
message = input("Mensaje: ")

# Crear un socket TCP/IP
# AF_INET: socket de familia IPv4
# SOCK_STREAM: socket de tipo TCP (orientado a conexión)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#  Conectar el socket al servidor en la dirección y puerto especificados
sock.connect(server_address)

# Mostrar mensaje que se va a enviar
print(f"Mensaje '{message}' enviado.")

# Codificar el mensaje a bytes y enviarlo al servidor
sock.sendall(message.encode('utf-8'))

# sendall() asegura que todos los datos sean enviados

# Recibir datos del servidor (hasta 1024 bytes)
data = sock.recv(1024)

# Decodificar e imprimir los datos recibidos
print("Mensaje recibido: ", data.decode())

# Cerrar la conexión con el servidor
sock.close()

