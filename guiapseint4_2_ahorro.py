"""
Ejercicio 2: Cálculo de Ahorros para una Compra Especial
Problema:
Tienes una meta de ahorro para comprar una nueva consola de videojuegos que cuesta
$300. Diseña un programa que te ayude a calcular cuánto dinero necesitas ahorrar cada
mes para alcanzar tu meta en un año. Además, si ahorras más de $100 al mes, recibirás un
bono adicional del 5% sobre el total ahorrado al final del año. Imprime el total ahorrado,
incluyendo el bono, al final del año.
"""
meta = 300
bono = 0
ahorro_mensual = int(input("Ingrese ahorro mensual: "))
print(f"La meta es de ${meta}")
print(f"El ahorro anual fue ${ahorro_mensual*12:,}")
if ahorro_mensual >= 100:
    bono = round(ahorro_mensual * 0.05)
print(f"El bono por ahorrar sobre $100 mensual fue ${bono:,} ")
print(f"El total ahorrado fue de ${ahorro_mensual*12+bono:,}")