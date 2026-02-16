import json

class ChatSystem:
    def __init__(self, persistence_file="salas.json"):
        self.salas = {}  # {nombre_sala: {"usuarios": set()}}
        self.usuarios = {}  # {usuario: sala_actual}
        self.persistence_file = persistence_file
        self._cargar_salas()

    def _guardar_salas(self):
        with open(self.persistence_file, "w") as f:
            json.dump({sala: list(data["usuarios"]) for sala, data in self.salas.items()}, f)

    def _cargar_salas(self):
        try:
            with open(self.persistence_file, "r") as f:
                data = json.load(f)
                self.salas = {sala: {"usuarios": set(usuarios)} for sala, usuarios in data.items()}
        except FileNotFoundError:
            self.salas = {}

    def create_sala(self, nombre):
        if nombre in self.salas:
            return f"La sala '{nombre}' ya existe."
        self.salas[nombre] = {"usuarios": set()}
        self._guardar_salas()
        return f"Sala '{nombre}' creada."

    def join_sala(self, usuario, nombre):
        if nombre not in self.salas:
            return f"La sala '{nombre}' no existe."
        # Si el usuario estaba en otra sala, lo sacamos
        if usuario in self.usuarios:
            self.leave_sala(usuario)
        self.salas[nombre]["usuarios"].add(usuario)
        self.usuarios[usuario] = nombre
        self._guardar_salas()
        return f"{usuario} se unió a la sala '{nombre}'."

    def leave_sala(self, usuario):
        if usuario not in self.usuarios:
            return f"{usuario} no está en ninguna sala."
        sala = self.usuarios[usuario]
        self.salas[sala]["usuarios"].discard(usuario)
        del self.usuarios[usuario]
        self._guardar_salas()
        return f"{usuario} salió de la sala '{sala}'."

    def listar_usuarios(self, nombre):
        if nombre not in self.salas:
            return f"La sala '{nombre}' no existe."
        return list(self.salas[nombre]["usuarios"])

    def mensaje_privado(self, remitente, destinatario, mensaje):
        if remitente not in self.usuarios:
            return f"{remitente} no está en ninguna sala."
        if destinatario not in self.usuarios:
            return f"{destinatario} no está en ninguna sala."
        return f"[Privado] {remitente} -> {destinatario}: {mensaje}"


# Ejemplo de uso
chat = ChatSystem()

print(chat.create_sala("General"))
print(chat.join_sala("Alice", "General"))
print(chat.join_sala("Bob", "General"))
print(chat.listar_usuarios("General"))
print(chat.mensaje_privado("Alice", "Bob", "Hola Bob!"))
print(chat.leave_sala("Alice"))