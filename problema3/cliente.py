#!/usr/bin/env python3
"""
Problema 3: Chat simple con múltiples clientes - Cliente
Objetivo: Crear un cliente de chat que se conecte a un servidor y permita enviar/recibir mensajes en tiempo real
"""

import socket
import threading

def receive_messages():
    """
    Función ejecutada en un hilo separado para recibir mensajes del servidor
    de forma continua sin bloquear el hilo principal.
    """
    while True:
        # Recibir mensajes del servidor (hasta 1024 bytes) y decodificarlos
 message = client_socket.recv(1024).decode("utf-8")
            if not message:
                # Si el servidor cierra la conexión
                print("Conexión cerrada por el servidor.")
                break

        # Imprimir el mensaje recibido
        print(message)
        except Exception as e:
            print(f"Error al recibir mensaje: {e}")
            break


# Solicitar nombre de usuario al cliente
client_name = input("Cuál es tu nombre? ")

# Crear un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET: socket de familia IPv4
# SOCK_STREAM: socket de tipo TCP (orientado a conexión)

#  Conectar el socket al servidor en la dirección y puerto especificados
server_address = ("127.0.0.1", 12345)  # Cambia la IP y puerto según tu servidor
client_socket.connect(server_address)

#  Enviar el nombre del cliente al servidor (codificado a bytes)
client_socket.send(client_name.encode("utf-8"))

# Crear y iniciar un hilo para recibir mensajes del servidor
# target: función que se ejecutará en el hilo
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Bucle principal en el hilo principal para enviar mensajes al servidor
while True:
    # Solicitar mensaje al usuario por consola
    message = input("Mensaje: ")
    #  Codificar el mensaje a bytes y enviarlo al servidor
client_socket.send(message.encode("utf-8"))
