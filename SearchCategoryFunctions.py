from SearchListFunctions import queriesByProduct
from SalesCategoryFunctions import productsByCategory, printTable
from CommonFunctions import sortInverse

def lessSearchedByCategory(qty):
  prodByCategories = productsByCategory()
  # # print(prodByCategories)
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
    printTable(category.upper(), qty, "buscados", "Búsquedas",arrCategory)
  # print(categoryDict)

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

def sortByCategoriesSearches(prodByCategories):
  # lifestore_searches = [id_search, id product]
  searches = queriesByProduct()
  # print(searches)
  categoriesDict = {}
  for category in prodByCategories:
    dict1 = {}
    # print(prodByCategories)
    for product in prodByCategories[category]:
      # print(product, ':', prodByCategories[category][product])
      if product in searches:
        dict1.update({product: searches[product]})
    dict1 = sortInverse(dict1, len(dict1))
    categoriesDict.update({category: dict1})
  # print(categoriesDict)
  return categoriesDict