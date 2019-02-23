
from itertools import product
from time import time
from barraProgreso import BarraProgreso

class Generador(object):

	def __init__(self, nombreArchivo):
		self.__datos = self.__cargarArchivo(nombreArchivo)
		self.__L = len(self.__datos)
		self.__progreso = BarraProgreso()

	def __cargarArchivo(self, nombreArchivo):
		
		datos = []
		archivo = open(nombreArchivo, "r")

		for palabra in archivo: 
			datos.append(palabra.replace("\n",""))

		archivo.close()
		return datos

	def generarDiccionario(self, longitudMaximaClave, nombreArchivo):

		inicio = time()
		diccionario = open(nombreArchivo, "w")

		for longitudClave in range(1, longitudMaximaClave+1):

			tamaño = self.__L**longitudClave
			n = 1
			for combinacion in product(self.__datos, repeat=longitudClave):
				
				diccionario.write("".join(combinacion) + "\n")

				self.__progreso.printProgressBar(
					n,
					tamaño,
					prefix = "Longitud "+ str(longitudClave)
				)
			
				n += 1
		
		diccionario.close()
		fin = time()
		print("\nTiempo transcurrido:", str(round(fin-inicio, 5))+"s")
