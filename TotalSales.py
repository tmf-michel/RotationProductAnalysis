from lifestore_file import lifestore_products, lifestore_sales 

# lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 true or 0 false)]
# lifestore_products = [id_product, name, price, category, stock]
# salida = [mes, ingresos, ventas]

# Función para obtener las ventas mensuales y anuales
# Version para datos crudos para exportar
# Recibe como parámetro el año deseado
def salesPerMonthRaw(year):
  monthlySales = {}
  monthlyProducts = {}
  months = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
  # Bucle principal para extraer las fecha y ID de cada venta y separarlos en 2 diccionarios
  # monthlySales = { month : sales_qty} y monthlyProducts = { month : [product_id] }
  # Solo se agregan los meses que tuvieron ventas
  for sale in lifestore_sales:
    # Si el producto no pertenece al año deseado
    # Terminar iteración
    strYear = '/{}'.format(year)
    if strYear not in sale[3]:
      continue
    if sale[4] == 1:
      continue
    monthly_date = sale[3][3:]
    fecha = monthlySales.get(monthly_date)
    # Agregar las ventas y los productos
    if fecha == None:
      monthlySales.setdefault(monthly_date, 1)
      monthlyProducts.setdefault(monthly_date,[sale[1]])
    else:
      monthlySales[monthly_date] = monthlySales[monthly_date]+1
      monthlyProducts[monthly_date].append(sale[1])
  monthIncome = {}
  prices = priceByProduct()
  # Bucle para leer el precio de cada producto  y agregarlo al número de ventas de dicho producto en el mes correspondiente en 
  # monthIncome = {month : Ingresos}
  for month in monthlyProducts:
    sum = 0
    for product in monthlyProducts[month]:
      # print(prices[product])
      sum = sum + prices[product]
      monthIncome.update({month: sum})
  # Bucle para agregar a monthlySales y monthIncome los meses en que no se hicieron ventas
  # monthlySales = { month/year : 0} y monthIncome = { month/year : 0 }
  for month in months:
    isMonth = False
    for month2 in monthIncome:
      new_date = month2.split('/')
      intMonth = int(new_date[0])
      strMonth = months[intMonth-1]
      # Validar si el mes ya existe o no existe
      if month == strMonth:
        isMonth = True
        break
    # Si el mes no existe quiere decir que no se vendió nada en ese mes
    if isMonth == False:
      # Se agrega el mes con ventas = 0 e Ingresos = 0
      monthIncome.update({str(months.index(month)+1)+'/'+year: 0})
      monthlySales.update({str(months.index(month)+1)+'/'+year:0})
  monthIncome = sorted(monthIncome.items())
  monthlySales = sorted(monthlySales.items())
  # print('monthly Income: ', monthIncome)
  # print('\nmonthly sales: ', monthlySales)
  arr = []
  # Calculando las ventas anuales (suma de ventas y suma de ingresos)
  # Se agregan en una sola lista las ventas e ingresos mensuales
  # Se agregan al final de la lista de ventas el total de ingresos y ventas
  ventasAnuales = ["Total",0,0]
  for idx, month in enumerate(monthlySales):
    new_date = month[0].split('/')
    intMonth = int(new_date[0])
    strMonth = months[intMonth-1]
    year = new_date[1]
    monthly_date = strMonth+'/'+year 
    arr.append([monthly_date, month[1], monthIncome[idx][1]])
    ventasAnuales[1] = ventasAnuales[1]+month[1]
    ventasAnuales[2] = ventasAnuales[2]+monthIncome[idx][1]
  # arr = [ 
  #   [mes_01, cant_ventas_01, ingresos_01], 
  #   [...], 
  #   [mes_n, cant_ventas_n, ingresos_n], 
  #   ["Total", ventas_totales, ingresos_totales] 
  # ]
  return arr

# Función para obtener las ventas mensuales
# MES, VENTAS, INGRESOS
# version para mostrar en programa
def salesPerMonth(year):
  # Se obtienen los datos crudos
  arr = salesPerMonthRaw(year)
  # Se mandan a imprimir en formato tabla
  printTable(arr)
  # Se ordena el arreglo usando la función lambda, según las ventas, localizadas en la posición 1 de cada venta, de mayor a menor
  arrSort = sorted(arr, key=lambda l:l[1], reverse=True)
  mostSalesStr = "El mes con más ventas fue {}, con  {} ventas equivalentes a $ {:0,.2f}."
  lessSalesStr = "El mes con menos ventas fue {}, con {} ventas equivalentes a ${:0,.2f}."
  print(mostSalesStr.format(expandedMonth(arrSort[0][0].split('/')[0]), arrSort[0][1], arrSort[0][2]))
  print('\n')
  # La última posición de arreglo arrSort[*] es la que tuvo menos ventas
  print(lessSalesStr.format(expandedMonth(arrSort[len(arrSort)-1][0].split('/')[0]), arrSort[len(arrSort)-1][1], arrSort[len(arrSort)-1][2] ))



def priceByProduct():
  prices = {}
  for product in lifestore_products:
    product_id = product[0]
    prices.update({product_id: product[2]})
    
  # products = {product_id: price}
  return prices

def printTable(arr):
  Tabla = """\
+---------------------------------------+
      Ingresos y Ventas Mensuales      
+---------------------------------------+
| MES          VENTAS          INGRESOS |
|---------------------------------------|
{}
+---------------------------------------+\
"""
  Tabla = (Tabla.format('\n'.join(" {:<8}       {:>3}        $ {:>12,.2f} ".format(*fila)
    for fila in arr)))
  print (Tabla)
  print('\n')

def expandedMonth(month):
  months = {
    "Ene": "Enero", "Feb":"Febrero", "Mar":"Marzo", "Abr":"Abril", "May":"Mayo", "Jun":"Junio", "Jul":"Julio", "Ago":"Agosto", "Sep":"Septiembre", "Oct":"Octubre", "Nov":"Noviembre", "Dic":"Diciembre"
  }
  return months[month]
  