import funciones as funciones
import tkinter as tk
window = tk.Tk()

# Configuracion general
title = "Analizador léxico"
window.title(title)
window.geometry("1000x600")
window.resizable(False, False)


# Configuracion del menu
menu = tk.Menu(window)
menuConfiguration = tk.Menu(menu, tearoff=0)
menuConfiguration.add_command(label="Ejecutar Análisis", command=lambda: funciones.convertirTextoALista(funciones.leerText(txtEntrada)))
menuConfiguration.add_separator()
menuConfiguration.add_command(label="Salir", command=window.quit)
menu.add_cascade(label="Archivo", menu=menuConfiguration)
window.config(menu=menu)

# Configuracion del input text
txtEntrada = tk.Text(window)
txtEntrada.grid(column=0, row=1, columnspan=200)
txtEntrada.config(bd=0, padx=5, pady=5)
txtEntrada.focus()

# Configuracion del output text
txtSalida = tk.Text(window, bg="grey")
txtSalida.grid(column=201, row=1, columnspan=200)
txtSalida.config(bd=0, padx=5, pady=5)
txtSalida.focus()




window.mainloop()