precio_o= float(input("introduce el precio original del producto: "))
descuento= float(input("introduce el porcentaje de descuento: ").replace("%",""))
precio_n= precio_o - (precio_o * (descuento/100))
iva= float(input("introduce el porcentaje de IVA: ").replace("%",""))
precio_iva= (precio_n*iva)/100
precio_total= precio_n + precio_iva
print("El precio original es: ", precio_o)
print("El precio con descuento es: ", precio_n)
print("El IVA es: ", precio_iva)
print("El precio total es: ", precio_total)