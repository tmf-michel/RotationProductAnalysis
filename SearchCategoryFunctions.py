from SearchListFunctions import queriesByProduct
from SalesCategoryFunctions import productsByCategory, printTable
from CommonFunctions import sortInverse

# Función para imprimir en versión tabla los prudctos menos buscados
# por categoría
def lessSearchedByCategory(qty):
  # Obtener los productos dividos por categoría
  prodByCategories = productsByCategory()
  # # print(prodByCategories)
  # Obtener las búscquedas de cada producto por categorías
  sortedCategories = sortByCategoriesSearches(prodByCategories)
  # sortedCategories = { category: {product_id: seaches_qty} }
  categoryDict = {}
  # Bucle para convertir en lista el diccionario sortedCategories
  # para poder imprimirlo en pantalla en formato Tabla
  for category in sortedCategories:
    arrCategory = []
    for product in sortedCategories[category]:
      arrCategory.append([product[0],prodByCategories[category][product[0]], product[1]])
    arrCategory = arrCategory[:qty]
    arrCategory.reverse()
    # Si no hay ventas se agrega una lista que indica que no hubo ventas
    if len(arrCategory) == 0:
      arrCategory = [['-','SIN VENTAS','-']]
    # Si las búscquedas fueron menos a las que se requieren buscar, se agrega un NA a cada búsqueda faltante
    elif len(arrCategory) < qty:
      for i in range(len(arrCategory), qty):
        arrCategory.append(['NA','NA','NA'])
    categoryDict.update({category:arrCategory})
    # Se imprime en formato tabla
    printTable(category.upper(), qty, "buscados", "Búsquedas",arrCategory)
  # print(categoryDict)

# Función para mostrar los productos menos buscados por categoría
# Función igual a lessSearchedByCategoryRaw() sin imprimir en formato tabla
def lessSearchedByCategoryRaw(qty):
  prodByCategories = productsByCategory()
  # print(prodByCategories)
  sortedCategories = sortByCategoriesSearches(prodByCategories)
  # print(sortedCategories)
  categoryDict = {}
  for category in sortedCategories:
    arrCategory = []
    for product in sortedCategories[category]:
      arrCategory.append([product[0],prodByCategories[category][product[0]], product[1]])
    arrCategory = arrCategory[:qty]
    arrCategory.reverse()
    if len(arrCategory) == 0:
      arrCategory = [['-','SIN VENTAS','-']]
    elif len(arrCategory) < qty:
      for i in range(len(arrCategory), qty):
        arrCategory.append(['NA','NA','NA'])
    categoryDict.update({category:arrCategory})
  return categoryDict


# Organizar las búscquedas por categoría
def sortByCategoriesSearches(prodByCategories):
  # lifestore_searches = [id_search, id product]
  # Diccionario con los ID de los porductos y su cantidad de búsquedas
  searches = queriesByProduct()
  # searches = {product_id_1: searchQty, 3: 34}
  categoriesDict = {}
  # Bucle para agregar cada productos con sus búscquedas a su categoría correspondiente
  for category in prodByCategories:
    dict1 = {}
    # print(prodByCategories)
    # Bucle interno para comparar los productos ya divididos por categorías y agregarle su cantidad de búsquedas
    for product in prodByCategories[category]:
      # print(product, ':', prodByCategories[category][product])
      if product in searches:
        dict1.update({product: searches[product]})
    dict1 = sortInverse(dict1, len(dict1))
    categoriesDict.update({category: dict1})
  # categoriesDict = { category: {product_id: seaches_qty} }
  return categoriesDict

def categoriesSearched():
  prodByCategories = productsByCategory()
  searches = queriesByProduct()
  # searches = { product_id: searchQty}
  categories = {}
  print('+-------------------------------+')
  print('| {0:^29} |'.format('BÚSQUEDAS POR CATEGORÍA'))
  print('+-------------------------------+')
  print('| {0:^17} | {1:^9} |'.format('Categoría', 'Búsquedas'))
  print('+-------------------|-----------+')
  for category in prodByCategories:
    searchTimes = 0
  #   dict1 = {}
    for product in prodByCategories[category]:
      if product in searches:
        searchTimes += searches[product]
    print('| {0:<17} | {1:>9} |'.format(category, searchTimes))
    categories.update({category: searchTimes})
  print('+-------------------------------+')
