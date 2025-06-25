import tkinter as tk
import time

# crear una ventana principal
ventana=tk.Tk()
ventana.title("Reloj Digital")
ventana.geometry("300x100")
ventana.config(bg="#414040")

# Crear un reloj digital que muestre la hora actual y se actualice cada segundo
reloj=tk.Label(ventana, font=("Helvetica", 48), bg="black", fg="white")

# Función para actualizar la hora en el reloj
def hora() : 
    tiempo_actual=time.strftime("%H:%M:%S")
    reloj.config(text=tiempo_actual)
    ventana.after(1000, hora)

# Añadir el reloj centrado a la ventana
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)
reloj.grid(row=0, column=0, sticky="nsew")

hora()

ventana.mainloop()