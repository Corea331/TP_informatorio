import tkinter as tk
from tkinter import messagebox
import os


def agregar_menu(ventana_padre):
    barra_menu = tk.Menu(ventana_padre)
    ventana_padre.config(menu=barra_menu, bg="#def3f3")

    menu_archivo = tk.Menu(barra_menu, tearoff=0)
    menu_archivo.add_cascade(label="Archivo", menu=menu_archivo)

    def buscar_excel():
        archivo = tk.filedialog.askopenfilename(
            title="Seleccionar archivo Excel",
            filetypes=[("Archivos Excel", "*.xlsx; *.xls")]
        )
        if archivo:
            if os.path.exists(archivo):
                messagebox.showinfo("Archivo seleccionado", f"Archivo: {archivo}")
            else:
                messagebox.showerror("Error", "El archivo no existe.")
        
    def leer_readme():
        archivo = tk.filedialog.askopenfilename(
            title="Abrir README",
            filetypes=[("Archivos de texto", "*.txt")]
        )
        if archivo:
            try:
                with open(archivo, "r" , encoding="utf-8") as file:
                    contenido = file.read()
                    messagebox.showinfo("Contenido de README", contenido[:1000] + ("\n..." if len(contenido) > 1000 else ""))
            except FileNotFoundError:
                messagebox.showerror("Error", "El archivo README.txt no se encontró.")

    menu_archivo.add_command(label="Buscar archivo Excel", command=buscar_excel)
    menu_archivo.add_command(label="Leer README", command=leer_readme)
    menu_archivo.add_separator()
    menu_archivo.add_command(label="Salir", command=ventana_padre.quit)


