from Tablero import  Tablero
from Barco import Barco


SUBMARINO = 1
BUQUE = 2
PORTAAVIONES = 4


if __name__ == '__main__':

	print(f"======== HUNDIR LA FLOTA ========")

	tablero1 = Tablero(tamanho=(8,8))
	tablero1.mostrar_tablero()

	barco1 = Barco(nombre="Submarino_1", longitud=3)
	barco1.mostrar_estado()

	tablero1.mostrar_tablero()

	barco1.recibir_golpe()
	barco1.mostrar_estado()
	barco1.recibir_golpe()
	barco1.recibir_golpe()
	barco1.mostrar_estado()
