import funciones as funciones
import tkinter as tk
palabrasReservadas = ['FOR', 'TO', 'DO', 'PRINTF', 'NEXT']
operadores = ['=', '(', ')','+','-','*','[',']','<','>']


window = tk.Tk()

# Configuracion general
title = "Analizador léxico"
window.title(title)
window.geometry("1000x600")
window.resizable(False, False)


def analizar():
  contador = 0
  contenidoTexto = funciones.leerText(txtEntrada) # 'multiline'
  contenidoLista = funciones.convertirTextoALista(contenidoTexto) # ['lista','de','lineas']
  primerLinea = contenidoLista[0]
  token = ""
  lista=[]
  for char in list(primerLinea):
    print(char)
    if char != " ":
      token = token + char
    else:
      if palabrasReservadas.count(token) > 0:
        lista.append("PR["+token+"]")
      elif token.isnumeric():
        lista.append("NUM["+token+"]")
      elif operadores.count(char) >0:
        lista.append("OP["+char+"]")
      # elif char != " ":
      #   lista.append("ID["+token+"]")
      token = ""
      continue
  
  print(lista)





# Configuracion del menu
menu = tk.Menu(window)
menuConfiguration = tk.Menu(menu, tearoff=0)
#menuConfiguration.add_command(label="Ejecutar Análisis", command=lambda: funciones.convertirTextoALista(funciones.leerText(txtEntrada)))
menuConfiguration.add_command(label="Ejecutar Análisis", command=analizar)
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