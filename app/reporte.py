import csv


class ReporteResultados:
    def __init__(self, encuesta, respuestas):
        self.encuesta = encuesta
        self.respuestas = respuestas

    def generar_reporte(self):
        print(f"Generando reporte para la encuesta '{
              self.encuesta.titulo}'...")

    def exportar_datos_crudos(self, filename="resultados.csv"):
        with open(filename, "w", newline='') as f:
            writer = csv.writer(f)
            for respuesta in self.respuestas:
                writer.writerow([respuesta.participante.nombre,
                                respuesta.pregunta.texto, respuesta.respuesta])
        print(f"Datos exportados a {filename}.")
