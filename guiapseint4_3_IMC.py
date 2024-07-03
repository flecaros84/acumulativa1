"""
Ejercicio 3: Calculadora de Índice de Masa Corporal (IMC) y Evaluación de Salud
Problema:
Como parte de un proyecto de salud en la escuela, se te pide que diseñes un programa que
ayude a calcular el Índice de Masa Corporal (IMC) de una persona y evalúe su estado de
salud. El IMC se calcula utilizando la fórmula:
De acuerdo con los valores de IMC, se puede evaluar el estado de salud de la siguiente
manera:
IMC < 18.5: Bajo peso
18.5 <= IMC < 25: Peso normal
25 <= IMC < 30: Sobrepeso
IMC >= 30: Obesidad
El programa debe solicitar al usuario que ingrese su peso (en kilogramos) y su altura (en
metros), calcular su IMC y determinar su estado de salud según los criterios mencionados
anteriormente. Imprime el IMC calculado y la evaluación del estado de salud.
"""
#Calcular el IMC = peso / altura**2
#Entrada / proceso / salida
#Que datos debe ingresar el user: altura y peso
#Solicitar la altura en tipo de dato float
altura = float(input("Ingresa la altura en formato 1.65: "))
peso = float(input("Ingresa el peso en kilos formato 80: "))
imc = peso/altura**2
#imprimir el resultado con f de formato para agregar variables al print,
#(imc:.2f) especificamos que la variable de tipo flotante se imprima
#despúes del punto .2 con dos decimales y la f final es para especificar
#que es un dato de tipo flotante
print(f"El IMC es de: {imc:.2f}")
if (imc < 18.5):
    print("Bajo peso")
elif (imc >= 18.5 and imc < 25):
    print("Peso normal")
elif (imc >=25 and imc < 30):
    print("Sobrepeso")
elif (imc >=30):
    print ("Obesidad")
