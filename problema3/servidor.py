#!/usr/bin/env python3
"""
Problema 3: Chat simple con múltiples clientes - Servidor
Objetivo: Crear un servidor de chat que maneje múltiples clientes simultáneamente usando threads
"""

import socket
import threading

# Definir la dirección y puerto del servidor
server_address = ("127.0.0.1", 12345)  # IP local y puerto 12345


# Lista para mantener todos los sockets de clientes conectados
clients = []

def handle_client(client_socket, client_name):
    """
    Maneja la comunicación con un cliente específico en un hilo separado.
    
    Args:
        client_socket: Socket del cliente
        client_name: Nombre del cliente
    """
    while True:
        try:
            # Recibir datos del cliente (hasta 1024 bytes)
            data = client_socket.recv(1024).decode("utf-8")
print(f"Mensaje recibido: {data}")

            # Si no se reciben datos, el cliente se desconectó
            if not data:
                break
                
            # Formatear el mensaje con el nombre del cliente
            message = f"{client_name}: {data.decode()}"
            
            # Imprimir el mensaje en el servidor
            print(message)
            
            # Retransmitir el mensaje a todos los clientes excepto al remitente
 broadcast(message, client_socket)

        except:
            break

            
        except ConnectionResetError:
            # Manejar desconexión inesperada del cliente
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(message, sender_socket):
    """
    Envía un mensaje a todos los clientes conectados excepto al remitente.
    
    Args:
        message: Mensaje a enviar (string)
        sender_socket: Socket del cliente que envió el mensaje original
    """
    for client in clients:
        if client != sender_socket:
            # Enviar el mensaje codificado a bytes a cada cliente
                client.send(message.encode("utf-8"))
            except:
                # Si falla el envío, eliminar cliente de la lista
                clients.remove(client)


# Crear un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# AF_INET: socket de familia IPv4
# SOCK_STREAM: socket de tipo TCP (orientado a conexión)

# Enlazar el socket a la dirección y puerto especificados
server_socket.bind(server_address)
print(f"Servidor enlazado en {server_address[0]}:{server_address[1]}")

# Poner el socket en modo escucha
server_socket.listen(5)  # El argumento indica el número máximo de conexiones en cola
print(f"Servidor escuchando en {server_address[0]}:{server_address[1]}")

# El parámetro define el número máximo de conexiones en cola

print("Servidor a la espera de conexiones ...")

# Bucle principal para aceptar conexiones entrantes
while True:
    # Aceptar una conexión entrante
    client_socket, client_address = server_socket.accept()
print(f"Conexión establecida con {client_address}")
    # client: nuevo socket para comunicarse con el cliente
    # addr: dirección y puerto del cliente
    
    print(f"Conexión realizada por {addr}")
    
    # Recibir el nombre del cliente (hasta 1024 bytes) y decodificarlo
    client_name = client_socket.recv(1024).decode("utf-8")
print(f"Nombre del cliente: {client_name}")
    #  Agregar el socket del cliente a la lista de clientes conectados
     clients.append(client_socket)
    # Enviar mensaje de confirmación de conexión al cliente
    client.send("ya estás conectado!".encode())
    
    # Notificar a todos los clientes que un nuevo usuario se unió al chat
    broadcast(f"{client_name} se ha unido al Chat.", client)
    
    # Crear e iniciar un hilo para manejar la comunicación con este cliente
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

if _name_ == "_main_":
    start_server()
    # target: función que se ejecutará en el hilo
    # args: argumentos que se pasarán a la función
    client_handler = # ...
    client_handler.start()