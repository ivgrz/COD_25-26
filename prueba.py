print(f"HOLA MUNDO")

def potencia():
# Programa que calcule la potencia de dos numeros
 print ("Calcular la potencia de dos numeros")
 n1 = float(input("ingrese un numero entero: "))
 n2 = float(input("ingrese otro numero entero: "))
 # Verificar si n2 es un entero
 if n2. is_integer():
     resultado = 1
     for i in range(int(n2)):
        resultado *= n1
     print(f"La potencia de {n1} elevado a {n2} es: {resultado}")
 else:
     resultado = n1 ** n2
     print(f"La potencia de {n1} elevado a {n2} es: {resultado}")
 print("Es todo por ahora")


potencia()