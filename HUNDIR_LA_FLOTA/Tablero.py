"""
Representamos el tablero de juego
"""
import random


class Tablero:

	AGUA = 0
	SUBMARINO = 1
	BUQUE = 2
	PORTAAVIONES = 4
	FALLO = 5
	IMPACTO = 6



	def __init__(self, tamanho: tuple):
		self.filas, self.columnas = tamanho

		self.casillas = []

		for f in range(self.filas):
			fila_actual = []

			for c in range(self.columnas):
				fila_actual.append(self.AGUA)
			self.casillas.append(fila_actual)

		self.barcos = []



	def _verificar_posicion(self, fila: int, columna: int ):
		if not (0 <= fila < self.filas and 0 <= columna < self.columnas):
			return False
		return self.casillas[fila][columna] == self.AGUA

	def colocar_barco(self, barco, fila: int, columna: int):
		self.casillas[fila][columna] = barco.tipo

		self.barcos.append({
			'barco': barco,
			'posicion': (fila,columna)
		})
	def barco_aleatorio(self,barco):
		MAX_INTENTOS = 100

		for _ in range(MAX_INTENTOS):
			fila_inicio = random.randrange(self.filas)
			columna_inicio = random.randrange(self.columnas)

			if self._verificar_posicion(fila_inicio,columna_inicio):
				self.colocar_barco(barco,fila_inicio,columna_inicio)
				print(f"Colocado: {barco.nombre} | Tipo: {barco.tipo} | Coordenada:  ({fila_inicio} , {columna_inicio}) ")
				return fila_inicio,columna_inicio
			print(f"ERROR: No se pudo colocar el barco {barco.nombre} aleatoriamente")

		return None

	def gestionar_impacto(self, fila: int, columna: int):
		if not (0 <= fila < self.filas and 0 <= columna < self.columnas):
				return "FUERA"
		valor_casilla = self.casillas[fila][columna]
		posicion_disparo = (fila,columna)

		if valor_casilla == self.AGUA:
			self.casillas[fila][columna] = self.FALLO
		elif valor_casilla in [self.SUBMARINO,self.BUQUE,self.PORTAAVIONES]:
			self.casillas[fila][columna] = self.IMPACTO

			for barco_entrada in self.barcos:
				if barco_entrada['posicion'] == (fila,columna):
					barco_entrada['barco'].recibir_golpe()
					return "IMPACTO"
			return "IMPACTO"
		elif valor_casilla == self.IMPACTO:

			for barco_entrada in self.barcos:
				if barco_entrada['posicion'] == posicion_disparo:
					barco = barco_entrada['barco']

					if not barco.esta_hundido():
						barco.recibir_golpe()
						return "IMPACTO"
					else:
						return "REPETIDO"
			return "ERROR"

		elif valor_casilla == self.FALLO:
			return "REPETIDO"

		return "ERROR"


	def __str__(self):
		lineas_salida = []

		mapa_simbolos = {
			self.AGUA: '🌊',
			self.SUBMARINO: '⛵',
			self.BUQUE:'🚢',
			self.PORTAAVIONES:'✈️',
			self.FALLO: '❌',
			self.IMPACTO: '💥',
			7 : '💀'

		}

		lineas_salida.append(
			f"====== TABLERO ======="
		)
		lineas_salida.append("    " + " ".join(f"{c:^2}" for c in range(self.columnas))) #Muestra los indices de la columna alineados a los espacios
		lineas_salida.append("  " + "---" * (self.columnas + 1))

		for i, fila in enumerate(self.casillas):
			linea_imprimir = f"{i:<2}|"
			for j, valor in enumerate(fila):

				if valor in [self.SUBMARINO, self.BUQUE, self.PORTAAVIONES]:
					simbolo = mapa_simbolos.get(self.AGUA)
				elif valor == self.IMPACTO:
					barco_r_hundido = False
					for barco_entrada in self.barcos:
						if barco_entrada['posicion'] == (i,j):
							if barco_entrada['barco'].esta_hundido():
								barco_r_hundido = True
								break
					if barco_r_hundido:
						simbolo = mapa_simbolos.get(7)
					else:
						simbolo = mapa_simbolos.get(self.IMPACTO)
				else:
					simbolo = mapa_simbolos.get(valor, str(valor))
				linea_imprimir += f" {simbolo} |"

			lineas_salida.append(linea_imprimir)
			lineas_salida.append("  " + "---" * (self.columnas + 1))

		lineas_salida.append(f"============")

		return "\n".join(lineas_salida)