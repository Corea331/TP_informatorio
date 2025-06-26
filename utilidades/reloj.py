import tkinter as tk
import time
from datetime import datetime

reloj = None

# Función para crear el reloj
def crear_reloj(ventana_padre):
    global reloj
    reloj = tk.Label(ventana_padre, font=("Arial", 12), bg="black", fg="white")
    reloj.pack(pady=5)
    actualizar()

# Función para actualizar el reloj
def actualizar():
    global reloj
    if reloj:
        hora = time.strftime("%H:%M:%S")
        fecha = datetime.now().strftime("%d/%m/%Y")
        reloj.config(text=f"{fecha} | {hora}")
        reloj.after(1000, actualizar)

# funcion para actualizar la fecha por mes y año
def obtener_mes_anio():
    ahora = datetime.now()
    nombre_mes = ahora.strftime("%B")
    anio = ahora.year
    return nombre_mes, anio