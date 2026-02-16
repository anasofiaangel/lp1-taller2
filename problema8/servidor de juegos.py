import socket
import threading

BUFFER_SIZE = 1024

class TicTacToeServer:
    def __init__(self, host="0.0.0.0", port=9999):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(10)
        print(f"[INFO] Servidor de juegos en {host}:{port}")

        self.clients = []
        self.players = []
        self.board = [" "] * 9
        self.current_turn = "X"

    def broadcast(self, message):
        """Envía un mensaje a todos los clientes (jugadores y espectadores)."""
        for client in self.clients:
            try:
                client.sendall(message.encode())
            except:
                self.clients.remove(client)

    def print_board(self):
        """Devuelve el tablero como string."""
        b = self.board
        return f"""
        {b[0]} | {b[1]} | {b[2]}
        ---------
        {b[3]} | {b[4]} | {b[5]}
        ---------
        {b[6]} | {b[7]} | {b[8]}
        """

    def check_winner(self):
        """Verifica si hay un ganador."""
        combos = [
            (0,1,2), (3,4,5), (6,7,8),  # filas
            (0,3,6), (1,4,7), (2,5,8),  # columnas
            (0,4,8), (2,4,6)            # diagonales
        ]
        for a,b,c in combos:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]
        if " " not in self.board:
            return "Empate"
        return None

    def handle_client(self, client, addr):
        self.clients.append(client)
        print(f"[INFO] Cliente conectado: {addr}")

        if len(self.players) < 2:
            symbol = "X" if len(self.players) == 0 else "O"
            self.players.append((client, symbol))
            client.sendall(f"Eres jugador {symbol}\n".encode())
        else:
            client.sendall("Eres espectador\n".encode())

        self.broadcast("[INFO] Nuevo cliente conectado\n")
        self.broadcast(self.print_board())

        while True:
            try:
                data = client.recv(BUFFER_SIZE).decode().strip()
                if not data:
                    break

                # Solo jugadores pueden hacer movimientos
                for p_client, symbol in self.players:
                    if client == p_client and symbol == self.current_turn:
                        if data.isdigit():
                            pos = int(data)
                            if 0 <= pos < 9 and self.board[pos] == " ":
                                self.board[pos] = symbol
                                winner = self.check_winner()
                                if winner:
                                    self.broadcast(f"\n{self.print_board()}\n")
                                    self.broadcast(f"[INFO] Resultado: {winner}\n")
                                    self.board = [" "] * 9
                                    self.current_turn = "X"
                                else:
                                    self.current_turn = "O" if self.current_turn == "X" else "X"
                                    self.broadcast(f"\n{self.print_board()}\n")
                                    self.broadcast(f"Turno de {self.current_turn}\n")
                            else:
                                client.sendall("[ERROR] Movimiento inválido\n".encode())
                        else:
                            client.sendall("[ERROR] Ingresa un número de 0 a 8\n".encode())
            except:
                break

        client.close()
        self.clients.remove(client)
        print(f"[INFO] Cliente desconectado: {addr}")

    def start(self):
        while True:
            client, addr = self.server.accept()
            threading.Thread(target=self.handle_client, args=(client, addr)).start()


if __name__ == "__main__":
    server = TicTacToeServer()
    server.start()