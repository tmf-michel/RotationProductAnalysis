from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches


cantidad_de_productos = len(lifestore_products)
print(f'En Inventario existen {cantidad_de_productos} productos distintos.')

num = int(input('Cuántos Productos Quieres Obtener?\n > '))
productos = lifestore_products[:num]

print('\nEscogiste los siguientes productos:')
for producto in productos:
    print(producto)

print('\nSus nombres son los siguientes:')
nombres = []
for producto in productos:
    nombre = producto[1]
    nombres.append(nombre)
print(nombres)

print('\n Aún podemos mostrarlos de mejor manera:')
for nombre in nombres:
    # Solamente quiero mostrar las primeras 14 letras del nombre
    print(f'* {nombre[:14]}')
