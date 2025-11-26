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

def crear_flota():
	flota = [
		("Submarino Alfa", SUBMARINO),
		("Buque Beta", BUQUE),
		("Portaaviones Gamma", PORTAAVIONES)
	]

	flota_objetos = []

	for nombre, tipo in flota:
		nuevo_barco = Barco(nombre=nombre, tipo=tipo)
		flota_objetos.append(nuevo_barco)
	return flota_objetos

def obtener_coordenadas(mensaje, max_v):
	while True:
		try:
			valor = input(mensaje)
			if valor.lower() == 's':
				return 's'
			coord = int(valor)
			if 0 <= coord <= max_v:
				return coord
			else:
				print(f"Error: Coordenada fuera de rango")
		except ValueError:
			print("Entrada no valida. Solo numeros")


if __name__ == '__main__':
		print("===== HUNDIR LA FLOTA =====")

		tablero1 = Tablero(tamanho=(8,8))

		barcos_colocados = crear_flota()

		print("CREANDO FLOTA...")
		for barco in barcos_colocados:
			posicion_b = tablero1.barco_aleatorio(barco)

			if not posicion_b:
				print(f"ERROR: No se pudo colocar el barco {barco.nombre}")
				break

		print("===== FASE DE JUEGO =====")
		print(f"Flota: {len(barcos_colocados)} barcos")

		juego_activo = True

		while juego_activo:
			print("\n" + "~" * 40)
			print("--- Turno de Disparo ---")
			print(tablero1)

			contador_barcos_hundidos = 0

			for barco in barcos_colocados:

				if  barco.esta_hundido():
					contador_barcos_hundidos += 1

			if contador_barcos_hundidos == len(barcos_colocados):
				print("GANASTE")
				juego_activo = False
				break
		# Pedimos coordenadas para disparar

			filas = tablero1.filas
			columnas = tablero1.columnas

			fila = obtener_coordenadas(f"Dispara! introduce la fila (0 - {filas - 1}) o s para salir: ", filas)
			if fila == 's':
				juego_activo =  False
				break
			columna = obtener_coordenadas(f"Introduce la columnna (0 - {columnas - 1}) o 's' para salir: ", columnas)
			if columna == 's':
				juego_activo = False
				break

			resultado = tablero1.gestionar_impacto(fila,columna)

			if resultado == "AGUA":
				print("Le diste al agua :c")
			elif resultado == "IMPACTO":
				print("IMPACTO!")
				for barco in barcos_colocados:
					if barco.golpes_r == barco.vida_maxima:
						print(f"HUNDIDO!, destruiste el barco {barco.nombre}")
			elif resultado == "REPETIDO":
				print(f"Le diste a lo mismo, turno perdido")

			print("\n ====== ESTADO ACTUAL ======\n")
			for barco in barcos_colocados:
				estado_a = barco.mostrar_estado()
				print(f" - {barco.nombre} | {estado_a}")



