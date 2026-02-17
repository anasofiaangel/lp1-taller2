import socket
import threading

BUFFER_SIZE = 1024

class BackendServer:
    def __init__(self, host="127.0.0.1", port=0):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(5)
        self.host, self.port = self.server.getsockname()
        self.data_store = []
        self.peers = []  # otros servidores para replicación
        print(f"[INFO] Servidor backend en {self.host}:{self.port}")

    def replicate(self, message):
        """Replica datos a otros servidores registrados."""
        for peer in self.peers:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(peer)
                s.sendall(message.encode())
                s.close()
            except:
                print(f"[WARN] No se pudo replicar a {peer}")

    def handle_client(self, client_socket):
        while True:
            data = client_socket.recv(BUFFER_SIZE).decode()
            if not data:
                break
            print(f"[DATA] Recibido: {data}")
            self.data_store.append(data)
            self.replicate(data)
            client_socket.sendall(f"ACK: {data}".encode())
        client_socket.close()

    def start(self):
        while True:
            client_socket, addr = self.server.accept()
            print(f"[INFO] Cliente conectado: {addr}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()


if __name__ == "__main__":
    server = BackendServer()
    server.start()