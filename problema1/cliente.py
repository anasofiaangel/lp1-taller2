#!/usr/bin/env python3
"""
Problema 1: Sockets básicos - Cliente
Objetivo: Crear un cliente TCP que se conecte a un servidor e intercambie mensajes básicos
"""

import socket

def cliente_tcp():
    # Crear un socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Dirección y puerto del servidor
    server_address = ('localhost', 65432)  # Cambia 'localhost' y el puerto según tu servidor
    print(f"Conectando a {server_address[0]} en el puerto {server_address[1]}...")
    sock.connect(server_address)

    try:
        # Enviar datos al servidor
        mensaje = "Hola servidor, soy el cliente!"
        print(f"Enviando: {mensaje}")
        sock.sendall(mensaje.encode('utf-8'))

        # Recibir respuesta del servidor
        datos = sock.recv(1024)
        print(f"Recibido: {datos.decode('utf-8')}")

    finally:
        # Cerrar la conexión
        print("Cerrando conexión")
        sock.close()

if __name__ == "__main__":
    cliente_tcp()

