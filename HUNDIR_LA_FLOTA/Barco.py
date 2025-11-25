class Barco:


	def __init__(self, nombre: str, longitud: int ):
		self.nombre = nombre
		self.longitud = longitud
		self.golpes_recibidos = 0

	def recibir_golpe(self):

		if not self.esta_hundido():
			self.golpes_recibidos += 1

	def esta_hundido(self):

		if self.golpes_recibidos >= self.longitud:

			return True
		else:
			return False

	def mostrar_estado(self):

		if self.esta_hundido():
			estado = "HUNDIDO"

		elif self.golpes_recibidos > 0:
			porcentaje_dano = (self.golpes_recibidos/self.longitud) * 100
			estado = f"DAÑADO ({porcentaje_dano}"
		else:
			estado = "INTACTO"

		print(f"Barco: {self.nombre} | Longitud: {self.longitud} | Estado: {estado}")

		return estado

