"""
Representamos el tablero de juego
"""

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

	def mostrar_tablero(self):

		print(f"====== TABLERO =====")
		print("  | " + " | ".join(str(i) for i in range(self.columnas)))
		print("--+" + "---"*self.columnas)
		for i, fila in enumerate(self.casillas): # Enumerate se usa para obtener el indice y valor

			linea_imprimir = f"{i:<2}|"


			for valor in fila:

				valor_str = f"{valor:^1}"
				linea_imprimir += f" {valor_str} |"

			print(linea_imprimir)
		print(f"====================")

