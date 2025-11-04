

def temperaturas_():
    """
    Almacena en una lista la temperatura de cada dia de la semana

    No recibe parametros (No-Param)

    :returns: Una lista de enteros con las temperaturas ingresadas
    :rtype: list[int]
    """
    temperatura = []
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]

    for i in dias:
        temp = int(input(f"Escribe la temperatura del dia {i}: "))
        temperatura.append(temp)

        print(f"En el dia {i} la temperatura es de {temp}")
        print(temperatura)

temperaturas_()


def media_temperaturas(temperatura):

    valor_medio = sum(temperatura)/len(temperatura)

    print(f"SEGUNDA FUNCION")
    print("La lista pasada es: ", temperatura)
    print(f"El valor medio de los grados de temperatura de esta semana es {valor_medio}")



media_temperaturas(temperatura=[20,15,18,30,25])