import smtplib


class DistribuidorEncuestas:
    def __init__(self, encuesta):
        self.encuesta = encuesta

    def enviar_invitacion(self, participante):
        print(f"Enviando invitación a {participante.correo}...")
        # Lógica para enviar el correo real
        # smtp = smtplib.SMTP('smtp.gmail.com', 587)
        # smtp.sendmail(...)

    def enviar_recordatorio(self, participante):
        print(f"Enviando recordatorio a {participante.correo}...")
