
def menu():
    print(f"---ELIGE UNA OPCION---")

    while True:
        opcion = int(input(f"Elige una opcion"))

        if opcion == 1:
            print(f"Es rojo")
        elif opcion == 2:
            print(f"Es azul")
        elif opcion == 3:
            print(f"Es verde")
        elif opcion == 4:
            print(f"Es amarillo")
        break
menu()