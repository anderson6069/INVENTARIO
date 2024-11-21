class Participante:
    def __init__(self, nombre, correo, celular, edad, genero):
        self.nombre = nombre
        self.correo = correo
        self.celular = celular
        self.edad = edad
        self.genero = genero

    def __str__(self):
        return f"{self.nombre} - {self.correo}"
