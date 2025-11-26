class Barco:
	VIDAS_MAXIMAS = {
		1: 2,
		2: 3,
		4: 5
	}

	def __init__(self, nombre: str, tipo: int ):
		self.nombre = nombre
		self.vida_maxima = self.VIDAS_MAXIMAS.get(tipo, 1)
		self.tipo = tipo
		self.golpes_r = 0

	def recibir_golpe(self):
		if not self.esta_hundido():
			self.golpes_r += 1

	def esta_hundido(self):
		return self.golpes_r >= self.vida_maxima
	def mostrar_estado(self):
		if self.esta_hundido():
			estado = "HUNDIDO"
		elif self.golpes_r > 0:
			dano = (self.golpes_r/self.vida_maxima) * 100
			estado = f"DAÑADO ({dano:.0f}%)"
		else:
			estado = "INTACTO"
		return estado

	def get_info(self, posicion = None):

		info = {
			'nombre': self.nombre,
			'estado': self.mostrar_estado(),
			'tipo': self.tipo,
			'vida maxima': self.vida_maxima

		}
		if posicion:
			info['posicion'] = posicion

		return info



	def __str__(self):
		return f"Barco: {self.nombre} | Tipo: {self.tipo}"


