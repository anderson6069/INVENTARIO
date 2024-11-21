class Pregunta:
    def __init__(self, texto, tipo_respuesta):
        self.texto = texto
        self.tipo_respuesta = tipo_respuesta

    def editar_texto(self, nuevo_texto):
        self.texto = nuevo_texto
        print(f"Pregunta actualizada: {self.texto}")

    def cambiar_tipo(self, nuevo_tipo):
        self.tipo_respuesta = nuevo_tipo
        print(f"Tipo de respuesta cambiado a: {self.tipo_respuesta}")
