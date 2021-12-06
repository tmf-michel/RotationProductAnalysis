from lifestore_file import lifestore_products, lifestore_sales 
from SalesListFunctions import salesByProduct, monthlySalesByProduct
from CommonFunctions import sortInverse, numberToMonth

# def qtyByCategory():
#   cat = {}
#   # lifestore_products = [id_product, name, price, category, stock]
#   for item in lifestore_products:
#     cat_qty = cat.get(item[3])
#     if cat_qty == None:
#       # Agregar el producto ID y cantidad de 1
#       cat.setdefault(item[3],1)
#     else:
#       cat[item[3]] = cat_qty+1
#   print("Cat: \n", cat)

# SI
def productsByCategory():
  categories = {}
  for product in lifestore_products:
    category = categories.get(product[3])
    if category == None:
      categories.setdefault(product[3], {product[0]: product[1].split(',')[0]})
    else:
      categories[product[3]].update({product[0]:product[1].split(',')[0]})
  # print(categories)
  # categories = {category: {product_id: product_name}}
  return categories

# si
def sortByCategoriesSales(prodByCategories, year):
  sales = salesByProduct(lifestore_sales, year)
  # print(sales)
  categoriesDict = {}
  for category in prodByCategories:
    dict1 = {}
    # print(prodByCategories)
    for product in prodByCategories[category]:
      # print(product, ':', prodByCategories[category][product])
      if product in sales:
        dict1.update({product: sales[product]})
    dict1 = sortInverse(dict1, len(dict1))
    categoriesDict.update({category: dict1})
  # print(categoriesDict)
  return categoriesDict

def lessSelledByCategory(qty, year):
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
    
