"""
Ejercicio 1: Conversor de Dólar a Peso con Descuento
Problema:
Tus amigos están planeando un viaje a un país extranjero y necesitan convertir sus dólares
a la moneda local. Diseña un programa que les ayude a convertir sus dólares a pesos,
considerando el valor actual del dólar. Además, si la cantidad a convertir supera los
$10,000, se aplicará un descuento del 10%; si supera los $50,000, se aplicará un descuento
del 25%. Imprime el subtotal, el descuento aplicado y el total después del descuento.
"""
clp_dolar = float(850)
print("Ingrese dolares a cambiar:")
dolares = float(input())
subtotal = float()
descuento = float()
total = float()
subtotal = clp_dolar*dolares
if dolares>50000:
 descuento = clp_dolar*dolares*0.25
elif dolares>10000:
 subtotal = clp_dolar*dolares
 descuento = clp_dolar*dolares*0.1
total = subtotal+descuento
print("subtotal pesos = " +str(subtotal))
print("bonificación =" +str(descuento))
print("total pesos=" +str(total))