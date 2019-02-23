
import argparse
import os.path

from ataqueFuerzaBruta import AtaqueFuerzaBruta

def archivoValido(parser, arg):
    if not os.path.exists(arg):
        parser.error("El archivo %s no existe" % arg)
    else:
        return arg

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--comprimido", required=True,
                        help="archivo comprimido de entrada", type=lambda x: archivoValido(parser, x))
    parser.add_argument("-d", "--diccionario", required=True, type=lambda x: archivoValido(parser, x))
    parser.add_argument("-a", "--archivoDestino", help="directorio del archivo extraido", default=".")

    args = parser.parse_args()

    fuerzaBruta = AtaqueFuerzaBruta(args.comprimido, args.diccionario, args.archivoDestino)
    fuerzaBruta.atacar()

if __name__ == "__main__":
    main()
