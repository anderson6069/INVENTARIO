import hashlib


class Usuario:
    def __init__(self, username, password, rol):
        self.username = username
        self.password_hash = self.hash_password(password)
        self.rol = rol

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def autenticar(self, password):
        return self.password_hash == self.hash_password(password)

    def verificar_rol(self, rol):
        return self.rol == rol
