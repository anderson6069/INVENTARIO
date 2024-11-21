import tkinter as tk
from tkinter import messagebox
from usuario import Usuario
from encuesta import Encuesta
from pregunta import Pregunta
from participante import Participante
from distribuidor import DistribuidorEncuestas
from reporte import ReporteResultados

# Crear algunos datos
usuario_admin = Usuario("admin", "admin123", "Coordinador")
encuesta = Encuesta("Encuesta de Satisfacción")
pregunta = Pregunta("¿Estás satisfecho con el servicio?", "Múltiple")
participante = Participante(
    "Juan Perez", "juan@ejemplo.com", "123456789", 30, "Masculino")

# Funciones de interfaz


def autenticar_usuario():
    username = entry_usuario.get()
    password = entry_contraseña.get()

    if username == usuario_admin.username and usuario_admin.autenticar(password):
        messagebox.showinfo("Éxito", "Autenticación exitosa")
        frame_autenticacion.grid_forget()  # Ocultamos la pantalla de autenticación
        # Mostramos la interfaz de encuestas
        frame_encuestas.grid(row=1, column=0, padx=20, pady=20)
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")


def crear_encuesta():
    titulo = entry_titulo_encuesta.get()
    if titulo:
        encuesta.titulo = titulo
        encuesta.guardar()
        messagebox.showinfo("Éxito", f"Encuesta '{
                            encuesta.titulo}' guardada como borrador.")
    else:
        messagebox.showerror(
            "Error", "Debe ingresar un título para la encuesta.")


def enviar_invitacion():
    distribuidor = DistribuidorEncuestas(encuesta)
    distribuidor.enviar_invitacion(participante)
    messagebox.showinfo("Éxito", "Invitación enviada.")


def generar_reporte():
    reporte = ReporteResultados(encuesta, [])
    reporte.generar_reporte()
    reporte.exportar_datos_crudos()
    messagebox.showinfo("Éxito", "Reporte generado y exportado.")


# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Encuestas")

# Interfaz de autenticación
frame_autenticacion = tk.Frame(root)
frame_autenticacion.grid(row=0, column=0, padx=20, pady=20)

tk.Label(frame_autenticacion, text="Usuario:").grid(row=0, column=0)
entry_usuario = tk.Entry(frame_autenticacion)
entry_usuario.grid(row=0, column=1)

tk.Label(frame_autenticacion, text="Contraseña:").grid(row=1, column=0)
entry_contraseña = tk.Entry(frame_autenticacion, show="*")
entry_contraseña.grid(row=1, column=1)

button_autenticar = tk.Button(
    frame_autenticacion, text="Autenticar", command=autenticar_usuario)
button_autenticar.grid(row=2, column=0, columnspan=2)

# Interfaz para encuestas (oculta inicialmente)
frame_encuestas = tk.Frame(root)

tk.Label(frame_encuestas, text="Título de la Encuesta:").grid(row=0, column=0)
entry_titulo_encuesta = tk.Entry(frame_encuestas)
entry_titulo_encuesta.grid(row=0, column=1)

button_crear_encuesta = tk.Button(
    frame_encuestas, text="Crear Encuesta", command=crear_encuesta)
button_crear_encuesta.grid(row=1, column=0, columnspan=2)

button_enviar_invitacion = tk.Button(
    frame_encuestas, text="Enviar Invitación", command=enviar_invitacion)
button_enviar_invitacion.grid(row=2, column=0, columnspan=2)

button_generar_reporte = tk.Button(
    frame_encuestas, text="Generar Reporte", command=generar_reporte)
button_generar_reporte.grid(row=3, column=0, columnspan=2)

root.mainloop()
