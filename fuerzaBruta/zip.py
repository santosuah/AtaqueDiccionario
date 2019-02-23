
from zipfile import ZipFile

class Zip(object):

	def __init__(self, ruta, destino):
		self.__archivo = ZipFile(ruta)
		self.__destino = destino

	def extraer(self, constraseña):
		try:
			self.__archivo.extractall(path=self.__destino, pwd=bytes(constraseña, 'utf-8'))
			return True
		except:
			return False
