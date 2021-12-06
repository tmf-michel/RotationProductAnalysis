

from lifestore_file import lifestore_products, lifestore_searches
from CommonFunctions import changeIdToName, sort

"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]

lifestore_products = [id_product, name, price, category, stock]
"""
# Función para organizar por veces buscadas cada producto
def queriesByProduct():
  arr = lifestore_searches                  # Lista de búscquedas
  products = {}                             # Diccionario a devolver
  # Bucle para recorrer cada venta en la lista
  
  for product in arr:
    product_id = product[1]                 # Guardar en variable el ID del producto buscado
    # Extraemos el el nnúmero de busquedas correspondiente al product_id de la búsqueda
    prod_qty = products.get(product_id)
    #No se encontró el ID en el diccionario products por lo tanto prod_qty = Non
    if prod_qty == None:
      # Agregar el producto ID y cantidad de 1
      products.setdefault(product_id,1)
    # El ID del producto si está en el diccionario
    else:
      # Se se le suma una búsqueda más
      products[product_id] = prod_qty+1
  
  #########################################################################################
  # Codigo extra para productos no buscados
  # notSearchedProducts = {}
  # for seq in range(len(lifestore_products)):
  #   if lifestore_products[seq][0] not in products:
  #     notSearchedProducts.update({lifestore_products[seq][0]:0})
  # #########################################################################################
  # Example:
  # products = {product_id_1: searchQty, 3: 34}
  return products

# Función principal para mostrar los productos más buscados
# Versión para imprimir en pantalla
def mostSearchedProducts(qty):
  # Función para mostrar los productos más buscados en forma de lista
  arr = mostSearchedProductsRaw(qty)
# Imprime la tabla en buen formato
  Tabla = """\
+------------------------------------------------------------------------+
|                   TOP 10 de Productos más buscados                     |
+------------------------------------------------------------------------+
| Producto                                                     Búsquedas |
|------------------------------------------------------------------------|
{}
+------------------------------------------------------------------------+\
"""
  Tabla = (Tabla.format('\n'.join("| {:<65} {:>4} |".format(*fila)
    for fila in arr)))
  print (Tabla)

# Función donde se obtienen los productos más buscados
def mostSearchedProductsRaw(qty):
  # 3 pasos en 1
  # Paso 1
  # queriesByProduct()
  # Regresa los IDs de cada producto y las veces que fueron buscados
  # Paso 2
  # changeIdToName()
  # Reemplaza los IDs por el nombre de cada producto
  # Paso 3
  # sort(dic, qty)
  # Regresa una lista de tuplas ordenadas en forma descendente, y lo corta en la posición qty-1
  sortList = sort(changeIdToName(queriesByProduct()), qty)
  # Bucle para pasar de una lista de tuplas a una lista de listas
  # Entrada sortList = [(product_name, times_searched)]
  # Salida arr = [[product_name, times_searched]]
  arr = []
  for item in sortList:
    arr.append([item[0], item[1]])
  return arr