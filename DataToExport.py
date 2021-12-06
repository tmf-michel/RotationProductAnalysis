from SalesListFunctions import mostSelledProductsRaw, mostSelledProductsMonthlyRaw
from SearchListFunctions import mostSearchedProductsRaw
from SalesCategoryFunctions import lessSelledByCategoryRaw, lessSelledByMonthlyCategoryRaw
from SearchCategoryFunctions import lessSearchedByCategoryRaw
from Reviews import bestReviewsRaw, bestMonthlyReviewsRaw, worstReviewsRaw, worstMonthlyReviewsRaw, reviewsByCategoryRaw, monthlyReviewsByCategoryRaw
from TotalSales import salesPerMonthRaw

def exportData(qtyLow, qtyHigh, year):
  rawData = {}
  mostSelledProducts = mostSelledProductsRaw(qtyLow, year)
  # Por si queremos agregar encabezados a la tabla
  # mostSelledProductsHeader =  [['Producto', 'Cantidad de Ventas']]
  # mostSelledProducts = mostSelledProductsHeader + mostSelledProducts
  rawData.update({'Productos mas vendidos en el año':mostSelledProducts})
  
  mostSelledProductsMonthly = mostSelledProductsMonthlyRaw(qtyLow, year)
  rawData.update({'Productos mas vendidos por mes': mostSelledProductsMonthly})

  mostSearchedProducts = mostSearchedProductsRaw(qtyHigh)
  # Encabezados de tabla
  # mostSearchedProductsHeaders  = [['Productos', 'Cantidad de Búsquedas']]
  # mostSearchedProducts = mostSearchedProductsHeaders + mostSearchedProducts
  rawData.update({'Productos mas buscados':mostSearchedProducts})

  lessSelledByCategory = lessSelledByCategoryRaw(qtyLow, year)
  # print(lessSelledByCategory)
  # Encabezados de tabla
  # lessSearchedByCategory = {'Productos menos vendidos por categoria': lessSearchedByCategory}
  rawData.update({'Productos menos buscados por categoria': lessSelledByCategory})
  
  lessSelledByMonthlyCategory = lessSelledByMonthlyCategoryRaw(qtyLow, year)
  rawData.update({'Productos menos buscados mensualemente por categoria': lessSelledByMonthlyCategory})

  lessSearchedByCategory = lessSearchedByCategoryRaw(qtyHigh)
  # print(lessSearchedByCategory)
  # Encabezados de tabla
  # lessSearchedByCategory = {'Productos menos buscados, por categoria': lessSearchedByCategory}
  rawData.update({'Productos menos buscados por categoria': lessSearchedByCategory})

  bestReviews = bestReviewsRaw(qtyLow, year)
  # Encabezados de tabla
  # bestReviewsHeaders = [['Producto', 'Score Promedio']]
  # bestReviews = bestReviewsHeaders + bestReviews
  rawData.update({'Productos con mejores reseñas':bestReviews})
  
  bestMonthlyReviews = bestMonthlyReviewsRaw(qtyLow, year)
  rawData.update({'Productos con mejores reseñas, por mes': bestMonthlyReviews})

  worstReviews = worstReviewsRaw(qtyLow, year)
  # Encabezados de tabla
  # worstReviewsHeaders = [['Producto', 'Score Promedio']]
  # worstReviews = worstReviewsHeaders + worstReviews
  rawData.update({'Productos con peores reseñas':worstReviews})

  worstMonthlyReviews = worstMonthlyReviewsRaw(qtyLow, year)
  rawData.update({'Productos con peores reseñas, por mes': worstMonthlyReviews})
  
  reviewsByCategory = reviewsByCategoryRaw(year)
  # print(reviewsByCategory)
  # Encabezados de tabla
  # reviewsByCategoryHeader = [['Producto', 'Score']]
  # reviewsByCategory = reviewsByCategoryHeader + reviewsByCategory
  rawData.update({'Reseñas por categoría:': reviewsByCategory})
  
  monthlyReviewsByCategory = monthlyReviewsByCategoryRaw(year)
  rawData.update({'Reseñas mensuales por cateoria: ': monthlyReviewsByCategory})

  salesPerMonth = salesPerMonthRaw(year)
  # Encabezados de tabla
  # salesPerMonthHeaders = [['Fecha', 'Cantidad de Ventas', 'Ingresos']]
  # salesPerMonth = salesPerMonthHeaders + salesPerMonth
  rawData.update({'Ventas promedio mensuales': salesPerMonth})

  for section in rawData:
    print('\n')
    print(section+':', rawData[section])
  print('\n')
  