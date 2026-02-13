#!/usr/bin/env python3
"""
Problema 2: Comunicación bidireccional - Servidor
Objetivo: Crear un servidor TCP que devuelva exactamente lo que recibe del cliente
"""

import socket

# Definir la dirección y puerto del servidor
server_address = ('localhost', 65432)  # Cambia según necesidad

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET: socket de familia IPv4
# SOCK_STREAM: socket de tipo TCP (orientado a conexión)

#  Enlazar el socket a la dirección y puerto especificados
sock.bind(server_address)

#  Poner el socket en modo escucha
sock.listen(1)  # número máximo de conexiones en cola

# El parámetro define el número máximo de conexiones en cola

# Bucle infinito para manejar múltiples conexiones (una a la vez)
while True:

    print("Servidor a la espera de conexiones ...")
    
    #  Aceptar una conexión entrante
    conn, addr = sock.accept()
    print(f"Conexión realizada por {addr}")

    # accept() bloquea hasta que llega una conexión
    # conn: nuevo socket para comunicarse con el cliente
    # addr: dirección y puerto del cliente
    
    print(f"Conexión realizada por {addr}")

    # Recibir datos del cliente (hasta 1024 bytes)
    data = conn.recv(1024)

    # Si no se reciben datos, salir del bucle
    if not data:
        break

    # Mostrar los datos recibidos (en formato bytes)
    print("Datos recibidos:", data)
    
    # Enviar los mismos datos de vuelta al cliente (echo)
     conn.sendall(data)
    
    #  Cerrar la conexión con el cliente actual
    print("Cerrando conexión con el cliente")
        conn.close()


