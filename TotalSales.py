from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches 
# from datetime import date
# dd/mm/aaaa
# lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 true or 0 false)]
# lifestore_products = [id_product, name, price, category, stock]
# salida = [mes, ingresos, ventas]
def salesPerMonthRaw(year):
  monthlySales = {}
  monthlyProducts = {}
  months = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
  for sale in lifestore_sales:
    # Si el producto no pertenece al año deseado
    # Terminar iteración
    strYear = '/{}'.format(year)
    if strYear not in sale[3]:
      continue

    if sale[4] == 1:
      continue
    # new_date = sale[3].split('/')
    # intMonth = int(new_date[1])
    # strMonth = months[intMonth-1]
    # year = new_date[2]
    # monthly_date = strMonth+'/'+year  
    monthly_date = sale[3][3:]
    fecha = monthlySales.get(monthly_date)
    if fecha == None:
      monthlySales.setdefault(monthly_date, 1)
      monthlyProducts.setdefault(monthly_date,[sale[1]])
    else:
      monthlySales[monthly_date] = monthlySales[monthly_date]+1
      monthlyProducts[monthly_date].append(sale[1])
  monthIncome = {}
  prices = priceByProduct()
  
  for month in monthlyProducts:
    print(month)
    sum = 0
    for product in monthlyProducts[month]:
      # print(prices[product])
      sum = sum + prices[product]
      monthIncome.update({month: sum})
  for month in months:
    isMonth = False
    for month2 in monthIncome:
      new_date = month2.split('/')
      intMonth = int(new_date[0])
      strMonth = months[intMonth-1]
      if month == strMonth:
        isMonth = True
        break
    if isMonth == False:
      monthIncome.update({str(months.index(month)+1)+'/'+year: 0})
      monthlySales.update({str(months.index(month)+1)+'/'+year:0})
  monthIncome = sorted(monthIncome.items())
  monthlySales = sorted(monthlySales.items())
  # print('monthly Income: ', monthIncome)
  # print('\nmonthly sales: ', monthlySales)
  arr = []
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
  # arr.append(ventasAnuales)
  # print(arr)
  
  return arr
  # printTable(arr)

  # SORT POR AÑO Y POR MES
  # VENTAS ANUALES
def salesPerMonth(year):
  arr = salesPerMonthRaw(year)
  printTable(arr)
  arrSort = sorted(arr, key=lambda l:l[1], reverse=True)
  mostSalesStr = "El mes con más ventas fue {}, con {} ventas equivalentes a $ {:0,.2f}."
  lessSalesStr = "El mes con menos ventas fue {}, con {} ventas equivalentes a ${:0,.2f}."
  print(mostSalesStr.format(expandedMonth(arrSort[0][0].split('/')[0]), arrSort[0][1], arrSort[0][2]))
  print('\n')
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
  