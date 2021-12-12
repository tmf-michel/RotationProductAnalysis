from src.lifestore_file import lifestore_products
import operator       # librería ocupada por las funciones sort() en itemgetter()

# Función para reemplazar los IDs por los nombres de los productos en un diccionario
def changeIdToName(dic):
  products = lifestore_products
  #Buscar el Nombre por id y cambiarla por el nombre
  # lifestore_products = [id_product, name, price, category, stock]
  prod_sales = {}                   # Diccionario a devolver
  # Bucle para buscar cada producto en la lista lifestore_products
  for prod in products:
    # Si el diccionario a devolver tiene la misma longitud que el diccionario original
    # Salir del for, porque ya se recorrieron todos los productos del diccionario
    # Se ahorran recursos al no recorrer toda la lista original de forma necesaria
    if len(prod_sales) >= len(dic):
      break
    # Bucle para recorrer cada producto en el diccionario
    for key in dic:
      # si el ID de lifestore_products ubicado en prod[0] es igual al ID del diccionario
      if prod[0] == key:
        # Cambiando el ID por el nombre
        # prod[1].split(',')[0] => El nombre es muy largo, se divide en cada coma ',' y solo se toma la primera parte
        # setdefault('value', 'key')
        prod_sales.setdefault(prod[1].split(',')[0], dic[key])
        continue
  # dic = {product_id, value}
  # Devolviendo el diccionario de la forma
  # prod_sales = {product_name, value}
  return prod_sales

# Función para ordenar un diccionario de forma descendente
# Entra un diccionario
# Devuelve una lista de tuplas ordenados por sus items
def sort(dic, qty):
  dic_sort = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
  # Regresa lista de tuplas ordenadas por items, y se corta en la posición qty-1
  return dic_sort[:qty]

# Función para ordenar un diccionario de forma ascendente
def sortInverse(dic, qty):
  # Regresa lista de tuplas ordenadas por items, y se corta en la posición qty-1
  dic_sort_inverse = sorted(dic.items(), key=operator.itemgetter(1), reverse=False)
  return dic_sort_inverse[:qty]

# Función para 'limpiar' la pantalla, una serie de saltos de línea
def clear():
  print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

def numberToMonth(num):
  if num == 1 or num == '01 ' or num == '1':
    return 'Enero'
  elif num == 2 or num == '02' or num == '2':
    return 'Febrero'
  elif num == 3 or num == '03' or num == '3':
    return 'Marzo'
  elif num == 4 or num == '04' or num == '4':
    return 'Abril'
  elif num == 5 or num == '05' or num == '5':
    return 'Mayo'
  elif num == 6 or num == '06' or num == '6':
    return 'Junio'
  elif num == 7 or num == '07' or num == '7':
    return 'Julio'
  elif num == 8 or num == '08' or num == '8':
    return 'Agosto'
  elif num == 9 or num == '09' or num == '9':
    return 'Septiembre'
  elif num == 10 or num == '10':
    return 'Octubre'
  elif num == 11 or num == '11':
    return 'Noviembre'
  elif num == 12 or num == '12':
    return 'Diciembre'
  