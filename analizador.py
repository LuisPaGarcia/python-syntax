import funciones as funciones
import tkinter as tk
palabrasReservadas = ['FOR', 'TO', 'DO', 'PRINTF', 'NEXT']
operadores = ['=', '(', ')','+','-','*','[',']','<','>']


window = tk.Tk()

# Configuracion general
title = "Analizador léxico"
window.title(title)
window.geometry("1300x600")
window.resizable(False, False)

def algoritmo2(contenidoLista):
  print(enumerate(contenidoLista))
  token = ""
  lista = []
  lenContenidoLista = len(contenidoLista)-1

  for idx, val in enumerate(contenidoLista):
    token = token+val
    if val == " " or val == "\n" or val == "\t":
      if palabrasReservadas.count(token) > 0:
        lista.append("PR["+token+"]")
        token=""
        continue
      
      if operadores.count(token) > 0:
        lista.append("OP["+token+"]")
        token=""
        continue

      if token.isnumeric():
        lista.append("NUM["+token+"]")
        token=""
        continue
  print(lista)


def algoritmo1(contenidoLista):
  for linea in contenidoLista:
    lista=""
    listaDeLinea = linea.split()
    #palabrasReservadas.count(token) > 0:
    for palabra in listaDeLinea:
      # es palabra reservada?
      if palabrasReservadas.count(palabra) > 0:
        lista = lista + "PR["+palabra+"] "
        continue
      
      if operadores.count(palabra) > 0:
        lista = lista + "OP["+palabra+"] "
        continue

      if palabra.isnumeric():
        lista = lista + "NUM["+palabra+"] "
        continue

      if palabra[0] == "\'" and palabra[len(palabra)-1] == "\'" :
        lista = lista + "LT["+palabra+"] "
        continue
        
      lista = lista + "ID["+palabra+"] "

    txtSalida.insert("insert", lista)
    txtSalida.insert("insert", "\n")
    print(lista)

def analizar():
  contador = 0
  contenidoTexto = funciones.leerText(txtEntrada) # 'multiline'
  contenidoLista = funciones.convertirTextoALista(contenidoTexto) # ['lista','de','lineas']
  
  algoritmo1(contenidoLista)
  # algoritmo2(contenidoTexto)




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