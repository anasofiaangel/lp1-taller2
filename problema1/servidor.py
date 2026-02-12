#!/usr/bin/env python3
"""
Problema 1: Sockets básicos - Servidor
Objetivo: Crear un servidor TCP que acepte una conexión y intercambie mensajes básicos
"""

import socket

def servidor_tcp():
    # Definir dirección y puerto del servidor
    server_address = ('localhost', 65432)  # Cambia según necesidad

    # Crear un socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enlazar el socket a la dirección y puerto especificados
    sock.bind(server_address)

    # Poner el socket en modo escucha
    sock.listen(1)  # máximo 1 conexión en cola

    print("Servidor a la espera de conexiones ...")

    # Aceptar una conexión entrante
    conn, addr = sock.accept()
    print(f"Conexión realizada por {addr}")

    try:
        # Recibir datos del cliente
        datos = conn.recv(1024)
        print(f"Recibido: {datos.decode('utf-8')}")

        # Enviar respuesta al cliente
        respuesta = "Hola cliente, recibí tu mensaje!"
        conn.sendall(respuesta.encode('utf-8'))

    finally:
        # Cerrar la conexión con el cliente
        print("Cerrando conexión con el cliente")
        conn.close()

if __name__ == "__main__":
    servidor_tcp()
