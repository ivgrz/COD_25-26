

def obtener_temperaturas():
    """
    Almacena en una lista la temperatura de cada dia de la semana

    No recibe parametros (No-Param)

    :returns: Una lista de enteros con las temperaturas ingresadas
    :rtype: list[int]
    """
    temperatura = []
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]

    for dia in dias:
        temperatura_dia = int(input(f"Escribe la temperatura del dia {dia}: "))
        temperatura.append(temperatura_dia)

        print(f"En el dia {dia} la temperatura es de {temperatura_dia}")
        print(temperatura)
    return temperatura
obtener_temperaturas()


def media_temperaturas(temperatura: list[int]) -> float :
    """

    :param temperatura: Lista de temperaturas de cada dia de una semana
    :type temperatura: List[int]
    :returns:El valor medio de las temperaturas
    :rtype: float
    """
    valor_medio = sum(temperatura)/len(temperatura)

    print(f"SEGUNDA FUNCION")
    print("La lista pasada es: ", temperatura)
    print(f"El valor medio de los grados de temperatura de esta semana es {valor_medio}")

    return valor_medio

media_temperaturas(temperatura=[20,15,18,30,25])