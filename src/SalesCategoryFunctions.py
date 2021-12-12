from src.lifestore_file import lifestore_products, lifestore_sales 
from src.SalesListFunctions import salesByProduct, monthlySalesByProduct
from src.CommonFunctions import sortInverse, numberToMonth

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

# lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
# lifestore_products = [id_product, name, price, category, stock]
def incomeByCategory(year):
  # print('hello')
  prodByCategories = productsByCategory()
  sortedCategories = sortByCategoriesSales(prodByCategories, year)
  # sortedCategories = { category: { product_id: sales_qty } }
  incomes = {}
  # print(sortedCategories)
  for product in lifestore_products:
    
    product_category = product[3]
    product_id = product[0]
    product_price = product[2]
    for prod in sortedCategories[product_category]:
      if product_id == prod[0]:
        income = incomes.get(product_category)
        sales_qty = prod[1]
        salesIncome = sales_qty * product_price
        if income == None:
          incomes.setdefault(product_category, salesIncome)
        else:
          extra_income = income + salesIncome
          incomes.update({product_category: extra_income})
  # print('incomes', incomes)
  total = 0
  print('+----------------------------------+')
  print('| {0:^32} |'.format('INGRESOS POR CATEGORÍA'))
  print('+----------------------------------+')
  print('| {0:^17} |  {1:^11} |'.format('Categoría', 'Ingresos'))
  print('+-------------------|--------------+')
  for category in incomes:
    total += incomes[category]
    # ${:0,.2f}
    print('| {0:<17} | $ {1:>10,.2f} |'.format(category, incomes[category]))
  print('+-------------------|--------------+')
  print('| {0:^17} | $ {1:>10,.2f} |'.format('TOTAL', total))
  print('+----------------------------------+')
  

def totalSalesByCategory(year):
  prodByCategories = productsByCategory()
  sortedCategories = sortByCategoriesSales(prodByCategories, year)
  # sortedCategories = { category: { product_id: sales_qty } }
  category_sales = {}
  # print(sortedCategories)
  for category in sortedCategories:
    sales = []
    for product in sortedCategories[category]:
      
      product_sales = product[1]
      sales.append(product_sales)
    totalSales = sum(sales)
    category_sales.setdefault(category, totalSales)
  print("Sales by category")
  print(category_sales)
  sortedCategories = sortByCategoriesMonthlySales(prodByCategories, year)
  print('\n')
  months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
  category_month_sales = {}
  cont = 0
  for month in sortedCategories:
    sortedMonth = month
    category_sales = {}
    print(months[cont].upper())
    for category in sortedMonth:
      sales = []
      # print(category.upper(), '\n')
      for product in sortedMonth[category]:
        # print('prod', product)
        product_sales = product[1]
        sales.append(product_sales)
      totalSales = sum(sales)
      category_sales.setdefault(category, totalSales)
      print(category,':', totalSales)
    category_month_sales.setdefault(months[cont], category_sales)
    cont += 1
    print('\n')
  # print('mon', category_month_sales)
  # category_month_sales = {month:{ categoy: sales_qty} }

  # sortedCategories = [ {category: {product: sales_qty} } ]
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
    
