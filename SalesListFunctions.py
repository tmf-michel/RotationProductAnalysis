from lifestore_file import lifestore_sales
from CommonFunctions import changeIdToName, sort, numberToMonth

# Función para extraer las ventas mensuales de productos en un diccionario, 
# Recibe como parámetro una lista, en este caso lifestore_sales
def monthlySalesByProduct(lst, year):
  # Lista de diccionarios equivalentes a cada mes del año
  productsMonth = [
    {},{},{},{},{},{},{},{},{},{},{},{}
  ]
  for product in lst:
    # Si el producto no pertenece al año deseado
    # Terminar iteración
    strYear = '/{}'.format(year)
    if strYear not in product[3]:
      continue
    # Si el producto está marcado como devuelto
    # Terminar la iteración del for
    if product[4] == 1:
      continue
    product_id = product[1]                     # ID de cada producto vendidos
    # Obtener el mes de la venta y convertirlo en entero
    # Ej. 27/06/2020 el mes es '06' y se convierte a 6
    month = int(product[3].split('/')[1])
    # Preguntar si el producto ya se registro en el mes correspondiente
    prod_qty = productsMonth[month-1].get(product_id)
    # Si no se ha guardado previamente el producto
    if prod_qty == None:
      # Agregar el producto ID y cantidad de 1 venta
      productsMonth[month-1].setdefault(product_id,1)
    # El producto ya estába guardado
    else:
      # Se le suma una venta más
      productsMonth[month-1][product_id] = prod_qty+1
      # productsMonth = [ {product_id, sales_qty} ]
  return productsMonth

# Función que muestra los datos de los productos mas vendidos de forma cruda 
def mostSelledProductsMonthly(qty, year):
  # Crear una lista de diccionarios por mes con las ventas de la forma
  # lst = [ {product_id: sales_qty} ]
  lst = monthlySalesByProduct(lifestore_sales, year)
  # Por cada mes...
  for i in range(len(lst)):
    # Recuperar el mes en cuestión
    month = numberToMonth(i+1)
    # 2 funciones en 1
    # Paso 1
    # Reemplazar los IDs de los productos por el nombre de los mismos de la forma dictionary = {product_id: sales_qty} utilizando la funcion  changeIdToName(dictionary)
    # Paso 2
    # Ordenar el diccionario de acuerdo al número de ventas de mayor a menor usando la función sort(dictionary, qty) donde diccionary es el diccionario con la función y qty es el tamaño del arreglo de tuplas a devolver
    sortList = sort(changeIdToName(lst[i]), qty)
    arr = []
    # Se cambia la lista de tuplas por una lista de listas
    for item in sortList:
      arr.append([item[0], item[1]])
    if len(arr) <= 0:
      arr.append(['NA', 0])
    # Encabezados de la tabla
    Tabla = """\
                                {:^0}                                 
+------------------------------------------------------------------------+
|                    TOP 5 de Productos más vendidos                     |
+------------------------------------------------------------------------+
| Producto                                                        Ventas |
|------------------------------------------------------------------------|
{}
+------------------------------------------------------------------------+\
"""
    # Se agregan los datos a la tabla
    # .format() se utiliza para reemplazar los {} del string Tabla por los datos del arreglo
    # {:<} => alinea los datos a la izquierda
    # {:>} => alinea los datos a la derecha
    # {:<65} => alineando 65 caracteres a la izquierda Aqui va el nombre del producto
    # {:>4} 0> alineando 4 caracteres a la derecha. Aquí va el número de ventas del producto
    Tabla = (Tabla.format(month, '\n'.join("| {:<65} {:>4} |".format(*fila)
      for fila in arr)))
    print (Tabla)     #Imprimiendo la tabla
  
  
  

# Función principal, tiene como parámetros la cantidad de datos que queremos presentar
def mostSelledProductsMonthlyRaw(qty, year):
  # Crear una lista de diccionarios por mes con las ventas de la forma
  # lst = [ {product_id: sales_qty} ]
  lst = monthlySalesByProduct(lifestore_sales, year)
  monthlySales ={}
  # Por cada mes...
  for i in range(len(lst)):
    # Recuperar el mes en cuestión
    month = numberToMonth(i+1)
    # 2 funciones en 1
    # Paso 1
    # Reemplazar los IDs de los productos por el nombre de los mismos de la forma dictionary = {product_id: sales_qty} utilizando la funcion  changeIdToName(dictionary)
    # Paso 2
    # Ordenar el diccionario de acuerdo al número de ventas de mayor a menor usando la función sort(dictionary, qty) donde diccionary es el diccionario con la función y qty es el tamaño del arreglo de tuplas a devolver
    sortList = sort(changeIdToName(lst[i]), qty)
    arr = []
    # Se cambia la lista de tuplas por una lista de listas
    for item in sortList:
      arr.append([item[0], item[1]])
    monthlySales.update({month:arr})
  return monthlySales
    


# Función para extraer las ventas por productos en un diccionario, 
# Recibe como parámetro una lista, en este caso lifestore_sales
def salesByProduct(lst, year):
  products = {}                               # Iniciando diccionario vacío a devolver
  # Bucle para explorar todos los productos o ventas de la lista
  # lifestore_sales = [id_sale, id_product, score, date, refund]
  for product in lst:
    product_id = product[1]                   # Extraemos en una variable el ID
    # Verificamos si el ID ya se guardó en el diccionario a devolver
    # y se guarda el valor en prod_qty
    # Si aun no existe la key del product_id .get() devuelve None
    prod_qty = products.get(product_id)
    
    # Si el producto no pertenece al año deseado
    # Terminar iteración
    strYear = '/{}'.format(year)
    if strYear not in product[3]:
      continue
    # Si el producto está marcado como devuelto
    # Terminar la iteración del for
    if product[4] == 1:
      continue
    
    # Si no se ha guardado previamente el producto
    if prod_qty == None:
      # Agregar el producto ID y cantidad de 1 venta
      products.setdefault(product_id,1)
    
    # El producto ya estába guardado
    else:
      # Se le suma una venta más
      products[product_id] = prod_qty+1

  ###########################################################################
  # Pasos extra para los productos que no se vendieron
  # notSelledProducts = {}    
  # for seq in range(len(lifestore_products)):
  #   if lifestore_products[seq][0] not in products:
  #     notSelledProducts.update({lifestore_products[seq][0]:0})
  ########################################################################### 

  # Diccionario a devolver de la forma
  # products = {product_id: sales_qty}
  return products

# Función principal, tiene como parámetros la cantidad de datos que queremos presentar
def mostSelledProducts(qty, year):
  # LLamando a funcion secundaria  que regresa una lista de listas
  arr = mostSelledProductsRaw(qty, year)
  # arr = ['product_name', 'product_sales']

  # Encabezados de la tabla
  Tabla = """\
+------------------------------------------------------------------------+
|                 TOP 5 de Productos más vendidos en el año              |
+------------------------------------------------------------------------+
| Producto                                                        Ventas |
|------------------------------------------------------------------------|
{}
+------------------------------------------------------------------------+\
"""
# Se agregan los datos a la tabla
# .format() se utiliza para reemplazar los {} del string Tabla por los datos del arreglo
# {:<} => alinea los datos a la izquierda
# {:>} => alinea los datos a la derecha
# {:<65} => alineando 65 caracteres a la izquierda Aqui va el nombre del producto
# {:>4} 0> alineando 4 caracteres a la derecha. Aquí va el número de ventas del producto
  Tabla = (Tabla.format('\n'.join("| {:<65} {:>4} |".format(*fila)
    for fila in arr)))
  print (Tabla)     #Imprimiendo la tabla


# Función que muestra los datos de los productos mas vendidos de forma cruda 
def mostSelledProductsRaw(qty, year):
  # 3 funciones en 1
  # Paso 1
  # # Crear un diccionario de la forma dictionary = {product_id: sales_qty} utilizando la lista de ventas y la función  salesByProduct(lifestore_sales)
  # Paso 2
  # Reemplazar los IDs de los productos por el nombre de los mismos de la forma dictionary = {product_id: sales_qty} utilizando la funcion  changeIdToName(dictionary)
  # Paso 3
  # Ordenar el diccionario de acuerdo al número de ventas de mayor a menor usando la función sort(dictionary, qty) donde diccionary es el diccionario con la función y qty es el tamaño del arreglo de tuplas a devolver
  sortList = sort(changeIdToName(salesByProduct(lifestore_sales, year)), qty)
  arr = []
  # Se cambia la lista de tuplas por una lista de listas
  for item in sortList:
    arr.append([item[0], item[1]])
  return arr