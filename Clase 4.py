#una linea
"""varias
lineas"""

"""
numerico = 8 numerico
precio = 22.22 flotante
nombre = "Memo" string
flag = true true/false o 0/1 para booleanos
match = switch
"""
producto = input("Captura el nombre del producto: ")
precio = int(input("Agrega el precio del producto: "))

def ventas (producto, precio) :
    iva = 1.15
    total_pagar = precio * iva
    return total_pagar

print("Total a pagar por el producto: ", producto,"", ventas(producto, precio))
total_fin = ventas(producto, precio)