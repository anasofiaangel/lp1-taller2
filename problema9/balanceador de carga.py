import socket
import threading
import random
import time

BUFFER_SIZE = 1024

class LoadBalancer:
    def __init__(self, host="0.0.0.0", port=8888):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(100)
        print(f"[INFO] Balanceador escuchando en {host}:{port}")
        self.backends = []  # lista de servidores disponibles

    def register_backend(self, host, port):
        self.backends.append((host, port))
        print(f"[INFO] Servidor backend registrado: {host}:{port}")

    def health_check(self):
        """Verifica periódicamente si los servidores están vivos."""
        while True:
            for backend in list(self.backends):
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(2)
                    s.connect(backend)
                    s.close()
                except:
                    print(f"[WARN] Servidor caído: {backend}")
                    self.backends.remove(backend)
            time.sleep(5)

    def forward(self, client_socket, backend):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(backend)
            while True:
                data = client_socket.recv(BUFFER_SIZE)
                if not data:
                    break
                s.sendall(data)
                response = s.recv(BUFFER_SIZE)
                client_socket.sendall(response)
            s.close()
        except:
            client_socket.sendall(b"[ERROR] Backend no disponible")
        client_socket.close()

    def start(self):
        threading.Thread(target=self.health_check).start()
        while True:
            client_socket, addr = self.server.accept()
            print(f"[INFO] Cliente conectado: {addr}")
            if self.backends:
                backend = random.choice(self.backends)
                threading.Thread(target=self.forward, args=(client_socket, backend)).start()
            else:
                client_socket.sendall(b"[ERROR] No hay servidores disponibles")
                client_socket.close()


if __name__ == "__main__":
    lb = LoadBalancer()
    # Ejemplo: registrar manualmente servidores
    lb.register_backend("127.0.0.1", 5000)
    lb.register_backend("127.0.0.1", 5001)
    lb.start()