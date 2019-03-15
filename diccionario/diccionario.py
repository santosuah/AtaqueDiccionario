
import argparse
import os.path

from generador import Generador

def enteroValido(valor):
	n = int(valor)
	if n <= 0:
		raise argparse.ArgumentTypeError("%s es una longitud no válida" % n)
	return n

def archivoValido(parser, arg):
	if not os.path.exists(arg):
		parser.error("El archivo %s no existe" % arg)
	else:
		return arg

def main():

	try:
		parser = argparse.ArgumentParser()

		parser.add_argument("min",help="Longitud mínima de combinaciones", type=enteroValido)
		parser.add_argument("max", help="Longitud máxima de combinaciones", type=enteroValido)

		parser.add_argument("-p", "--palabras", required=True,
							help="Lista de cadenas de entrada", type=lambda x: archivoValido(parser, x))
		parser.add_argument("-d", "--destino", help="Directorio del diccionario generado", default="diccionario.txt")

		args = parser.parse_args()

		if args.min > args.max:
			raise argparse.ArgumentTypeError("valor mínimo %i y máximo %i no válidos" % (args.min, args.max))

		generador = Generador(args.palabras)
		print("Datos cargados del fichero: " + args.palabras)

		numeroCombinaciones = generador.calcularNumeroCombinaciones(args.min, args.max)
		print("Número de combinaciones: " + str(numeroCombinaciones) + "\n")

		generador.generarDiccionario(args.min, args.max, args.destino)
		print("Diccionario generado: " + args.destino)
	
	except argparse.ArgumentTypeError as ate:
		print(ate)
	
	except Exception as e:
		print(e)


if __name__ == "__main__":
	main()
