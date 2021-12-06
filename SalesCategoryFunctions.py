from lifestore_file import lifestore_products, lifestore_sales 
from SalesListFunctions import salesByProduct, monthlySalesByProduct
from CommonFunctions import sortInverse, numberToMonth

# Función para organizar los productos dentro de cada categoria
def productsByCategory():
  categories = {}
  # Bucle principal que copia los ID y categorias de cada producto y los organiza
  # en un diccionario categories{}
  for product in lifestore_products:
    category = categories.get(product[3])
    if category == None:
      categories.setdefault(product[3], {product[0]: product[1].split(',')[0]})
    else:
      categories[product[3]].update({product[0]:product[1].split(',')[0]})
  # categories = {category: {product_id: product_name}}
  return categories

# Función para organizar las ventas por categoría
def sortByCategoriesSales(prodByCategories, year):
  # Se obtiene los ids de cada producto como key del diccionario, y las ventas como value
  sales = salesByProduct(lifestore_sales, year)
  # sales = {product_id: sales_qty}
  categoriesDict = {}
  # Bucle para extraer el id y las ventas desde sales, y las categorías desde proByCategories y juntarlas
  for category in prodByCategories:
    dict1 = {}
    # Bucle secundario para extraer el product_id de cada categoría
    for product in prodByCategories[category]:
      # Si el product_id se vendió se agrega al diccionario con sus ventas respectivas
      if product in sales:
        dict1.update({product: sales[product]})
    # Se organizan de forma ascendente 
    dict1 = sortInverse(dict1, len(dict1))
    # Se pegan a la categoría correspondiente
    categoriesDict.update({category: dict1})
  # categoriesDict = { category: { product_id: sales_qty } }
  return categoriesDict

# Función para obtener los productos menos vendidos por categoría
# Recibe como parámetros la cantidad de datos a mostrar, y el año deseado
def lessSelledByCategory(qty, year):
  
  prodByCategories = productsByCategory()
  # prodByategories = {category: {product_id: product_name}}
  
  sortedCategories = sortByCategoriesSales(prodByCategories, year)
  # sortedCategories = { category: { product_id: sales_qty } }
  
  categoryDict = {}
  for category in sortedCategories:
    arrCategory = []
    for product in sortedCategories[category]:
      arrCategory.append([product[0],prodByCategories[category][product[0]], product[1]])
    arrCategory = arrCategory[:qty]
    categoryDict.update({category:arrCategory})
    printTable(category.upper(), qty, "vendidos", "   Ventas",arrCategory)
  # print(categoryDict)

def printTable(category, num, titleType, typeSub, arr):
  Tabla = """\
                                {0}           
+-----------------------------------------------------------------------------+
                    Los {1} {0} menos {2}                    
+-----------------------------------------------------------------------------+
| ID                               Nombre                           {3} |
|-----------------------------------------------------------------------------|
{4}
+-----------------------------------------------------------------------------+\
"""
  Tabla = (Tabla.format(category, num, titleType, typeSub,'\n'.join("| {:<4} {:^65} {:>4} |".format(*fila)
    for fila in arr)))
  print (Tabla)
  print('\n')

def lessSelledByCategoryRaw(qty, year):
  prodByCategories = productsByCategory()
  # print(prodByCategories)
  sortedCategories = sortByCategoriesSales(prodByCategories, year)
  # print(sortedCategories)
  categoryDict = {}
  for category in sortedCategories:
    arrCategory = []
    for product in sortedCategories[category]:
      arrCategory.append([product[0],prodByCategories[category][product[0]], product[1]])
    arrCategory = arrCategory[:qty]
    categoryDict.update({category:arrCategory})
  return categoryDict

# prodByCategories = {category: {product_id: product_name}}
def sortByCategoriesMonthlySales(prodByCategories, year):
  # sales = = {product_id: sales_qty}
  # monthlySales = [ {product_id: sales_qty} ]
  sales = monthlySalesByProduct(lifestore_sales, year)
  # print(sales)
  monthlyCategories = []
  for i in range(len(sales)):
    
    categoriesDict = {}
    for category in prodByCategories:
      dict1 = {}
      # print(prodByCategories)
      for product in prodByCategories[category]:
        # print(product, ':', prodByCategories[category][product])
        if product in sales[i]:
          dict1.update({product: sales[i][product]})
      dict1 = sortInverse(dict1, len(dict1))
      categoriesDict.update({category: dict1})
    # print(categoriesDict)
    # categoriesDict = {category: {product: sales_qty} }
    monthlyCategories.append(categoriesDict)
  # monthlyCategories = [ {category: {product: sales_qty} } ]
  return monthlyCategories

def lessSelledByMonthlyCategoryRaw(qty, year):
  prodByCategories = productsByCategory()
  # print(prodByCategories)
  sortedCategories = sortByCategoriesMonthlySales(prodByCategories, year)
  # sortedCategories = [ {category: {product: sales_qty} } ]
  # print(sortedCategories)
  monthlyCategories = []
  for i in range(len(sortedCategories)):
    # Recuperar el mes en cuestión
    month = numberToMonth(i+1)
    categoryDict = {}
    for category in sortedCategories[i]:
      arrCategory = []
      for product in sortedCategories[i][category]:
        arrCategory.append([product[0],prodByCategories[category][product[0]], product[1]])
      arrCategory = arrCategory[:qty]
      categoryDict.update({category:arrCategory})
    monthlyCategories.append({month:categoryDict})
  # print(monthlyCategories)
  return monthlyCategories

def lessSelledByMonthlyCategory(qty, year):
  prodByCategories = productsByCategory()
  # print(prodByCategories)
  sortedCategories = sortByCategoriesMonthlySales(prodByCategories, year)
  # print(sortedCategories)
  for i in range(len(sortedCategories)):
    # Recuperar el mes en cuestión
    month = numberToMonth(i+1)
    print('{:^80}'.format(month.upper()))
    categoryDict = {}
    for category in sortedCategories[i]:
      arrCategory = []
      for product in sortedCategories[i][category]:
        arrCategory.append([product[0],prodByCategories[category][product[0]], product[1]])
      arrCategory = arrCategory[:qty]
      if len(arrCategory) <= 0:
        arrCategory.append(['NA','NA', 0])
      categoryDict.update({category:arrCategory})
      printTable(category.upper(), qty, "vendidos", "   Ventas",arrCategory)

# lifestore_searches = [id_search, id product]
# def productSalesByCategory():
#   prodByCategories = productsByCategory()
#   sales = salesByProduct(lifestore_sales)
#   arrCategory = {}
#   for category in prodByCategories:
#     arr1 = []
#     # print('cat', category)
#     for product in prodByCategories[category]:
#       # print('prod', product)
#       if product['id'] in sales:
#         # HAY QUE AGREGAR EL SALES AL PRODUCTO
#         product.update({'sales': sales[product['id']]})
#         # print("prod update ", product)
#         # categories = {
#         #   "category01": [
#         #     {"id": "1", "name":"product01", "sales": sales_qty}
#         #     ],
#         #   }
#         arr1.append([product['id'], product['name'], product['sales']])
#         continue
#     arrCategory.update({category: arr1})
  # print("\nprodCat\n", prodByCategories)
  # print(arrCategory)
  # return prodByCategories

  # arrCategory = [productId, productName, productSales]
  # return arrCategory



# def principal2():
#   # print(productsByCategory())
#   print(categorySalesProducts())
#   # categories = productSalesByCategory()
#   # # print(categories)
#   # for category in categories:
#   #   print(category,': ', categories[category])
# #     Tabla = """\
# # +------------------------------------------------------------------------+
# # |                    TOP 50 de Productos más vendidos                    |
# # +------------------------------------------------------------------------+
# # | ID                            Producto                          Ventas |
# # |------------------------------------------------------------------------|
# # {}
# # +------------------------------------------------------------------------+\
# # """
# #   Tabla = (Tabla.format('\n'.join("| {:<65} {:>4} |".format(*fila)
# #     for fila in arr)))
# #   print (Tabla)
    
