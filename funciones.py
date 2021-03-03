# Constantes
palabrasReservadas = ['FOR', 'TO', 'DO', 'PRINTF', 'NEXT']
operadores = ['=', '(', ')']


# funcion para leer el contenido de un Text
def leerText(text):
  content = text.get(1.0, "end-1c")
  # print(content)
  return content

# Convierte un texto multi-lineas a una lista para iterar, usando los enter's
#
# de: """ string multi
#     linea
#     que queremos obtener"""
#
# a:  ['string multi', 'linea', 'que queremos obtener']
def convertirTextoALista(texto):
  lista = texto.splitlines()
  # print(lista)
  return lista

# Convierte un texto a una lista para iterar, usando los espacios en blanco
#
# de: 'este es un string a dividir'
#
# a:  ['este', 'es', 'un', 'string', 'a', 'dividir']
def dividirStringPorEspacios(texto):
  lista = texto.split()
  # print(lista)
  return lista

