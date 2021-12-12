"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""
from src.lifestore_file import lifestore_products, lifestore_sales
from src.CommonFunctions import changeIdToName, sort, sortInverse, numberToMonth
from src.SalesCategoryFunctions import productsByCategory

# lifestore_sales = [id_sale, id_product, score, date, refund]
def reviewsByProduct(year):
  dic = lifestore_sales
  sales = {}
  scores = {}
  for product in dic:
    product_id = product[1]
    score = product[2]
    prod_qty = sales.get(product_id)
    strYear = '/{}'.format(year)
    # Si no esta el año deseado
    # ]Terminar iteración
    if strYear not in product[3]:
      continue
    #No se ha pasado el producto
    if prod_qty == None:
      # Agregar el producto ID y cantidad de 1
      sales.setdefault(product_id,1)
      scores.setdefault(product_id, score)
    else:
      sales[product_id] = prod_qty+1
      scores[product_id] = scores[product_id]+score
  reviews = {}
  # print('sales', sales)
  # print('\nscores', scores)
  # print('\n')
  for product in sales:
    prodScore = scores[product]
    prodSale = sales[product]
    reviews.update({product: round(prodScore / prodSale, 1)})
  
  notScoredProducts = {} 

  for seq in range(len(lifestore_products)):
    if lifestore_products[seq][0] not in sales:
      notScoredProducts.update({lifestore_products[seq][0]:0})
  # products = {product_id: sales_qty}
  return reviews

def bestReviewsRaw(qty, year):
  reviews = sort(changeIdToName(reviewsByProduct(year)), 5)
  arr = []
  for item in reviews:
    arr.append([item[0], item[1]])
  return arr

def bestReviews(qty, year):
  arr = bestReviewsRaw(qty, year)
  Tabla = """\
+------------------------------------------------------------------------+
|                 TOP 5 de Productos con mejores reseñas                 |
+------------------------------------------------------------------------+
| Producto                                                       Reseñas |
|------------------------------------------------------------------------|
{}
+------------------------------------------------------------------------+\
"""
  Tabla = (Tabla.format('\n'.join("| {:<65} {:>4} |".format(*fila)
    for fila in arr)))
  print (Tabla)

def worstReviewsRaw(qty, year):
  reviews = sortInverse(changeIdToName(reviewsByProduct(year)), qty)
  arr = []
  for item in reviews:
    arr.append([item[0], item[1]])
  arr.reverse()
  return arr

def worstReviews(qty, year):
  arr = worstReviewsRaw(qty, year)
  Tabla = """\
+------------------------------------------------------------------------+
|                 Los 5 de Productos con peores reseñas                  |
+------------------------------------------------------------------------+
| Producto                                                       Reseñas |
|------------------------------------------------------------------------|
{}
+------------------------------------------------------------------------+\
"""
  Tabla = (Tabla.format('\n'.join("| {:<65} {:>4} |".format(*fila)
    for fila in arr)))
  print (Tabla)

def reviewsByCategoryRaw(year):
  productsByCategories = productsByCategory()
  # print(productsByCategories)
  reviewsByProd = reviewsByProduct(year)
  # print('\nReviews', reviewsByProd)
  scores = []
  for category in productsByCategories:
    lst = []
    for product in productsByCategories[category]:
      if product in reviewsByProd:
        lst.append(reviewsByProd[product])
    avScore = round(Average(lst),1)
    scores.append([category, avScore])
  # print('\nScores', scores)
  return scores

def Average(lst):
  return sum(lst) /len(lst)

def reviewsByCategory(year):
  scores = reviewsByCategoryRaw(year)
  Tabla = """\
+---------------------------+
|      Reseñas promedio     |
+---------------------------+
| Categoría         Reseñas |
|---------------------------|
{}
+---------------------------+\
"""
  Tabla = (Tabla.format('\n'.join("| {:<20} {:>4} |".format(*fila)
    for fila in scores)))
  print (Tabla)

def monthlyReviewsByCategoryRaw(year):
  productsByCategories = productsByCategory()
  # print(productsByCategories)
  reviewsByProd = monthlyReviewsByProduct(year)
  # monthlyReviews = [ {product_id: scoreAverage} ]
  monthlyReviews = []
  for i in range(len(reviewsByProd)):
    scores = []
    for category in productsByCategories:
      lst = []
      for product in productsByCategories[category]:
        if product in reviewsByProd[i]:
          lst.append(reviewsByProd[i][product])
      if len(lst) == 0:
        avScore = 'NA'
      else:
        avScore = round(Average(lst),1)
      scores.append([category, avScore])
    monthlyReviews.append(scores)
  # monthlyReviews = [ [ [category, score] ] ]
  return monthlyReviews

def monthlyReviewsByCategory(year):
  monthlyScores = monthlyReviewsByCategoryRaw(year)

  for i in range(len(monthlyScores)):
    month = numberToMonth(i+1)
    scores = monthlyScores[i]
    print('\n',month.upper())
    Tabla = """\
+---------------------------+
|      Reseñas promedio     |
+---------------------------+
| Categoría         Reseñas |
|---------------------------|
{}
+---------------------------+\
"""
    Tabla = (Tabla.format('\n'.join("| {:<20} {:>4} |".format(*fila)
      for fila in scores)))
    print (Tabla)

def monthlyReviewsByProduct(year):
  lst = lifestore_sales 
  sales = [ {},{},{},{},{},{},{},{},{},{},{},{} ]
  scores = [ {},{},{},{},{},{},{},{},{},{},{},{} ]
  for sale in lst:
    strYear = '/{}'.format(year)
    # Si no esta el año deseado
    # ]Terminar iteración
    if strYear not in sale[3]:
      continue
    # Obtener el mes de la venta y convertirlo en entero
    # Ej. 27/06/2020 el mes es '06' y se convierte a 6
    month = int(sale[3].split('/')[1])
    product_id = sale[1]
    score = sale[2]
    prod_qty = sales[month-1].get(product_id)
    #No se ha pasado el producto
    if prod_qty == None:
      # Agregar el producto ID y cantidad de 1
      sales[month-1].setdefault(product_id,1)
      scores[month-1].setdefault(product_id, score)
    else:
      sales[month-1][product_id] = prod_qty+1
      scores[month-1][product_id] = scores[month-1][product_id]+score
  monthlyReviews = []
  # print('sales', sales)
  # print('\nscores', scores)
  # print('\n')
  for i in range(len(sales)):
    reviews = {}
    for product in sales[i]:
      prodScore = scores[i][product]
      prodSale = sales[i][product]
      reviews.update({product: round(prodScore / prodSale, 1)})
    monthlyReviews.append(reviews)

    #######################################################################
    # notScoredProducts = {} 

    # for seq in range(len(lifestore_products)):
    #   if lifestore_products[seq][0] not in sales:
    #     notScoredProducts.update({lifestore_products[seq][0]:0})
    # # products = {product_id: sales_qty}
    #######################################################################
  # monthlyReviews = [ {product_id: scoreAverage} ]
  return monthlyReviews

def worstMonthlyReviewsRaw(qty, year):
  lst = monthlyReviewsByProduct(year)
  monthlyReviews = {}
  # Por cada mes...
  for i in range(len(lst)):
    # Recuperar el mes en cuestión
    month = numberToMonth(i+1)
    reviews = sortInverse(changeIdToName(lst[i]), qty)
    arr = []
    for item in reviews:
      arr.append([item[0], item[1]])
    arr.reverse()
    monthlyReviews.update({month:arr})
  return monthlyReviews

def worstMonthlyReviews(qty, year):
  monthlyReviews = worstMonthlyReviewsRaw(qty, year)
  
  for month in monthlyReviews:
    arr = monthlyReviews[month]
    if len(arr) <= 0:
      arr.append(['NA', 'NA'])
    print('\n{:^80}'.format(month.upper()))
    Tabla = """\
+------------------------------------------------------------------------+
|                 Los 5 de Productos con peores reseñas                  |
+------------------------------------------------------------------------+
| Producto                                                       Reseñas |
|------------------------------------------------------------------------|
{}
+------------------------------------------------------------------------+\
"""
    Tabla = (Tabla.format('\n'.join("| {:<65} {:>4} |".format(*fila)
      for fila in arr)))
    print (Tabla)

def bestMonthlyReviewsRaw(qty, year):
  lst = monthlyReviewsByProduct(year)
  monthlyReviews = {}
  # Por cada mes...
  for i in range(len(lst)):
    # Recuperar el mes en cuestión
    month = numberToMonth(i+1)
    reviews = sort(changeIdToName(lst[i]), qty)
    arr = []
    for item in reviews:
      arr.append([item[0], item[1]])
    monthlyReviews.update({month:arr})
  return monthlyReviews

def bestMonthlyReviews(qty, year):
  monthlyReviews = bestMonthlyReviewsRaw(qty, year)
  
  for month in monthlyReviews:
    arr = monthlyReviews[month]
    if len(arr) <= 0:
      arr.append(['NA', 'NA'])
    print('\n{:^80}'.format(month.upper()))
    Tabla = """\
+------------------------------------------------------------------------+
|                Los 5 de Productos con mejores reseñas                  |
+------------------------------------------------------------------------+
| Producto                                                       Reseñas |
|------------------------------------------------------------------------|
{}
+------------------------------------------------------------------------+\
"""
    Tabla = (Tabla.format('\n'.join("| {:<65} {:>4} |".format(*fila)
      for fila in arr)))
    print (Tabla)