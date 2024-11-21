from app.encuesta import Encuesta
from app.pregunta import Pregunta
from app.persona import Persona
from app.estudio import Estudio
from app.coordinador import Coordinador

# Crear un coordinador
coordinador = Coordinador("Joaquín")

# Crear preguntas
pregunta1 = Pregunta("¿Cómo calificaría nuestro servicio?", "opcion_multiple", [
                     "Excelente", "Bueno", "Regular", "Malo"])
pregunta2 = Pregunta("¿Qué mejorarías en nuestro servicio?", "abierta")

# Crear una encuesta
encuesta = coordinador.crear_encuesta(
    "Encuesta de Satisfacción", [pregunta1, pregunta2])

# Crear participantes
participante1 = Persona("Ana Gómez", "ana.gomez@example.com", 30, "Femenino")
participante2 = Persona(
    "Carlos Pérez", "carlos.perez@example.com", 40, "Masculino")

# Crear un estudio
estudio = Estudio(encuesta, [participante1, participante2])

# Registrar respuestas
estudio.registrar_respuesta(participante1, {
                            pregunta1.texto: "Bueno", pregunta2.texto: "Más rapidez en el servicio"})
estudio.registrar_respuesta(participante2, {
                            pregunta1.texto: "Excelente", pregunta2.texto: "Nada, todo está perfecto"})

# Generar informe
print(estudio.generar_informe())

# Mostrar detalles
print(coordinador)
print(estudio)
