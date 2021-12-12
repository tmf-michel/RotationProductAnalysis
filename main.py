# Created by: Jorge Chavarín
# Date: 04/12/2021

# Archivos y ibrerías importados
from src.Login import userAccess
from src.SalesListFunctions import mostSelledProducts, mostSelledProductsMonthly, monthlyRefundByProduct
from src.SearchListFunctions import mostSearchedProducts
from src.SalesCategoryFunctions import lessSelledByCategory, lessSelledByMonthlyCategory, totalSalesByCategory, incomeByCategory
from src.SearchCategoryFunctions import lessSearchedByCategory, categoriesSearched
from src.Reviews import bestReviews, bestMonthlyReviews, worstReviews, worstMonthlyReviews, reviewsByCategory, monthlyReviewsByCategory
from src.TotalSales import salesPerMonth
from src.DataToExport import exportData
from src.CommonFunctions import clear


#inicializacion de procesos

# Bucle infinito para ejecutar el programa indefinidamente
while(True):  
  # Función para limpiar la consola 
  clear()
  
  # Función de login, pregunta por usuario y contraseña previamente registrados
  access = userAccess()

  # Si el usuario y contraseña son correctas, se ejecuta el resto del programa
  if access == True:
    year = input('¿De qué año deseas el reporte? Ejemplo: 2020\nAño: ')
    # year = '2020'
    # Menú para que el usuario conozca las opciones
    print("\nANÁLISIS DE ROTACIÓN DE PRODUCTOS\n")
    menu= """\
  1) Los 5 productos más vendidos
  2) Los 10 productos más buscados
  3) Los 5 productos menos vendidos por categoría
  4) Los 10 productos menos buscados por categoría
  5) Los 5 productos con las mejores reseñas
  6) Los 5 productos con las peores reseñas
  7) Reseñas, Búsquedas e Ingresos por categoría
  8) Total de ingresos y ventas promedio Mensuales
  9) Ventas mensuales por categoría y devoluciones por mes
  10) Datos crudos para exportar
  0) Salir
  """
    # Variables usadas para la cantidad de datos en los reportes
    qtyLow = 5 
    qtyHigh = 10
    # Bucle para repetir el menú indefinidamente, hasta que el usuario desee salir
    while(access):
      print("Selecciona una opción:\n")
      try:
        # try para que la aplicación no se rompa si el usuario escribe algo diferente a un número en opc
        opc = int(input(menu))                  #Impresión del menú
        # Serie de if y elif según lo que  seleccionó el usuario

        if opc == 1:
          # Función para mostrar los productos más vendidos
          mostSelledProducts(qtyLow, year)              # 5 Productos con mayores ventas
          # Función para mostrar los productos más vendidos por mes
          mostSelledProductsMonthly(qtyLow, year)
          
        elif opc == 2:
          # Función para mostrar los productos más buscados
          mostSearchedProducts(qtyHigh)           # 10 productos con mayores búsquedas
        elif opc == 3:
          # Función para mostrar los productos menos vendidos por categoría
          lessSelledByCategory(qtyLow, year)            # 5 productos con menores ventas por categoría
          # Función para mostrar los productos menos vendidos por categoría por mes
          lessSelledByMonthlyCategory(qtyLow, year)
        elif opc == 4:
          # Función para mostrar los productos menos buscados por categoría
          lessSearchedByCategory(qtyHigh)         # 10 productos con menores búsquedas por categoría
        elif opc == 5:
          # Función para mostrar los productos con las mejores reseñas / scores
          bestReviews(qtyLow, year)                          # 5 productos con mejores reseñas / scores
          # Función para mostrar los productos con las mejores reseñas / scores por mes
          bestMonthlyReviews(qtyLow, year)
        elif opc == 6:
          # Función para mostrar los productos con las peores reseñas / scores
          worstReviews(qtyLow, year)                        # 5 productos con peores reseñas / scores
          # Función para mostrar los productos con las peores reseñas / scores por mes
          worstMonthlyReviews(qtyLow, year)
        elif opc == 7:
          # Función para mostrar el promedio de reseñas por categoría por mes
          monthlyReviewsByCategory(year)
          # Función para mostrar el promedio de reseñas por categoría
          reviewsByCategory(year) 
          categoriesSearched()                  # Promedio de reseñas de cada categoría
          incomeByCategory(year)                # Ganancias en pesos por categoría
        elif opc == 8:
          # Función para mostrar las ventas e ingresos de cada mes y el anual
          salesPerMonth(year)                       # Cantidad de ventas e ingresos por mes ordenados cronológicamente
        elif opc == 9:
          # Función para mostrar los ingresos y ventas de cada categoría al mes
          totalSalesByCategory(year)
          # Función para mostrar la cantidad de productos devueltos por mes
          monthlyRefundByProduct(year)
        elif opc == 10:
          # Función para mostrar todas las opciones del menú en versión para exportar o copiar/pegar
          exportData(qtyLow, qtyHigh, year)           #Listas sin formato de tabla para imprimir
        # El Usuario desea salir
        elif opc == 0: 
          print("Hasta luego...")
          # Se cambia el estado de acces a False para salir del bucle
          access = False
          break
        # Else para cuando el usuario teclee un número que no está en el menú
        else:
          print("Esta opción es inválida. Vuelve a intentarlo.\n")
        print('\n\n')
    # Except para cuando el usuario teclee algo que no sea un número
      except Exception as e:
        print('\nEsta opción es inválida. Vuelve a intentarlo.\n')
        # print(e)
  # El usuario introdujo más de 3 veces la contraseña, por lo tanto 'access' vale False
  else:
    print("\n\n ERROR! Ha excedido el número máximo de intentos.\n")