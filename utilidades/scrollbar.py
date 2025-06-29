import tkinter as tk
from tkinter import ttk


def crear_area_con_scroll(ventana_padre):
    canvas = tk.Canvas(ventana_padre, bg="#def3f3", highlightthickness=0)
    scrollbar = ttk.Scrollbar(ventana_padre, orient="vertical", command=canvas.yview,)
    frame_interno = tk.Frame(canvas)
    #color de fondo para el recuadro donde se encuentran los campos de entrada
    frame_interno.configure(bg="#def3f3")

    frame_interno.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=frame_interno, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return frame_interno
