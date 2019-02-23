
from time import time

from zip import Zip
from barraProgreso import BarraProgreso

class AtaqueFuerzaBruta(object):

	def __init__(self, rutaArchivo, rutaDiccionario, destino):
		self.__datos = self.__cargarArchivo(rutaDiccionario)
		self.__L = len(self.__datos)
		self.__archivo = Zip(rutaArchivo, destino)
		self.__progreso = BarraProgreso()

	def __cargarArchivo(self, nombreArchivo):
		
		datos = []
		archivo = open(nombreArchivo, "r")

		for palabra in archivo: 
			datos.append(palabra.replace("\n",""))

		archivo.close()
		return datos

	def __coincide(self, clave):
		return self.__archivo.extraer(clave)

	def atacar(self):
		print()

		inicio = time()
		n = 1
		for candidata in self.__datos:

			if self.__coincide(candidata):
				print()
				fin = time()
				print("\nTiempo transcurrido:", str(round(fin-inicio, 5))+"s")
				print("Clave:", candidata)
				return candidata
					
			self.__progreso.printProgressBar(
				n,
				self.__L
			)
				
			n += 1
	
		fin = time()
		print("\nTiempo transcurrido:", str(round(fin-inicio, 5))+"s")
		print("Clave no encontrada")
		return ""
