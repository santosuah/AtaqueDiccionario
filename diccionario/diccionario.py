
import argparse
import os.path

from generador import Generador

def archivoValido(parser, arg):
	if not os.path.exists(arg):
		parser.error("El archivo %s no existe" % arg)
	else:
		return arg

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("-p", "--palabras", required=True,
						help="Lista de cadenas de entrada", type=lambda x: archivoValido(parser, x))
	parser.add_argument("-l", "--longitud", help="Longitud máxima de las combinaciones", type=int, default=5)
	parser.add_argument("-d", "--destino", help="Directorio del diccionario generado", default="diccionario.txt")

	args = parser.parse_args()

	gen = Generador(args.palabras)
	print("Datos cargados del fichero: " + args.palabras + "\n")

	gen.generarDiccionario(args.longitud, args.destino)
	print("Diccionario generado: " + args.destino)


if __name__ == "__main__":
	main()
