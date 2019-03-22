
from itertools import product
from multiprocessing import Pool
from time import time

class Generador(object):

	def __init__(self, nombreArchivo):
		self.__datos = self.__eliminarRepetidos(self.__cargarArchivo(nombreArchivo))
		self.__L = len(self.__datos)

	def __cargarArchivo(self, nombreArchivo):
		
		datos = ""
		archivo = open(nombreArchivo, "r")

		for palabra in archivo:
			datos += palabra.replace("\n", "")

		archivo.close()
		return datos

	def __eliminarRepetidos(self, cadena):

		cadenaSinRep = ""
		for caracter in cadena:
			if caracter not in cadenaSinRep:
				cadenaSinRep += caracter

		return cadenaSinRep

	def calcularNumeroCombinaciones(self, min, max):
		combinaciones = 0
		for long in range(min, max+1):
			combinaciones += self.__L ** long

		return combinaciones

	def __calcularCombinaciones(self, particion, repeticiones, archivo):
		# como argumento en la función product, pasamos n repeticiones-1 los datos
		for combinacion in product(particion, *((self.__datos,)*(repeticiones-1))):
			archivo.write("".join(combinacion)+ "\n")

	def generarDiccionario(self, longitudMinima, longitudMaxima, nombreArchivo):

		try:
			inicio = time()
			poolHilos = Pool()
			diccionario = open(nombreArchivo, "w")

			numeroParticiones = 5
			longitudParticion = self.__L // numeroParticiones

			for longitudClave in range(longitudMinima, longitudMaxima+1):

				for numeroParticion in range(numeroParticiones):

					if numeroParticion == numeroParticiones - 1:
						particionDatos = self.__datos[longitudParticion*numeroParticion:]
					else:
						particionDatos = self.__datos[longitudParticion*numeroParticion:longitudParticion*(numeroParticion+1)]

					poolHilos.apply_async(self.__calcularCombinaciones(particionDatos, longitudClave, diccionario))

				print("Generada claves de longitud (" + str(longitudClave) + ")")

			poolHilos.close()
			poolHilos.join()
			
			diccionario.close()
			fin = time()
			print("\nTiempo transcurrido:", str(round(fin-inicio, 5))+"s")

		except KeyboardInterrupt:
			poolHilos.close()
			poolHilos.join()
			diccionario.close()
