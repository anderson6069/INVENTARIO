class Encuesta:
    def __init__(self, titulo):
        self.titulo = titulo
        self.preguntas = []
        self.estado = "Borrador"
        self.version = 1

    def guardar(self):
        print(f"Encuesta '{self.titulo}' guardada como borrador.")

    def publicar(self):
        if self.preguntas:
            self.estado = "Publicado"
            print(f"Encuesta '{self.titulo}' publicada.")
        else:
            print("La encuesta debe tener al menos una pregunta")

    def versionar(self):
        self.version += 1
        print(f"Versión de encuesta '{
              self.titulo}' actualizada a {self.version}.")
