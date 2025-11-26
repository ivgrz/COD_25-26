from Tablero import  Tablero
from Barco import Barco



SUBMARINO = 1
BUQUE = 2
PORTAAVIONES = 4
TIPOS_VALIDOS = {
	'1': ('Submarino', SUBMARINO),
	'2': ('Buque', BUQUE),
	'4': ('Portaaviones', PORTAAVIONES)
}
VIDAS_POR_TIPO = {1: 2, 2: 3, 4: 5}

if __name__ == '__main__':

	print(f"======== HUNDIR LA FLOTA ========")

	tablero1 = Tablero(tamanho=(8,8))
	barcos_colocados = []

	while True:
		print(f"Añadir Barcos: \n"
			  f"Tipos disponibles: \n"
			  f"1: Submarino (Vida {VIDAS_POR_TIPO[SUBMARINO]})\n"
			  f"2: Buque (Vida {VIDAS_POR_TIPO[BUQUE]})\n"
			  f"4: Portaaviones (Vida {VIDAS_POR_TIPO[PORTAAVIONES]})")

		nombre_barco = input("Introduce el nombre del barco o 's' para empezar: ").strip()

		if nombre_barco.lower() == 's':
			if not barcos_colocados:
				print(f"ERROR: TIENES QUE INTRODUCIR AL MENOS UN BARCO")
				continue
			break

		tipo_b = input("Introduce el tipo del barco: ").strip()

		if tipo_b not in TIPOS_VALIDOS:
			print("ERROR: DEBES INTRODUCIR UN TIPO VALIDO")
			continue

		tipo_n = TIPOS_VALIDOS[tipo_b][1]

		nuevo_b = Barco(nombre=nombre_barco,tipo=tipo_n)

		posicion_b = tablero1.barco_aleatorio(nuevo_b)

		if posicion_b:
			barcos_colocados.append(nuevo_b)
		else:
			print("Tablero lleno o posicion equivcada :c")
			break

		print(f"====== TABLERO ACTUAL ====\n"
			  f"Total barcos: {len(barcos_colocados)}"
			  f"--- Estado Actual --- \n")

		for barco in barcos_colocados:
			barco.mostrar_estado()

		print(f"\n {tablero1} \n"
			  f"===================\n")