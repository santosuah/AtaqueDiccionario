# Ataque de diccionario
![Alt text](./diagramas/flujo.png)

Pequeño script escrito en python, utilizado para comprobar conceptualemte como funcionan este tipos de ataques a groso modo. Esta dirigido a archivos zip comprimidos en ZipCrypto.

Existen dos fases de generación, la creación del diccionario a partir de lista de palabras y una longitud máxima de combinación, para porteriormente comporbar todos las claves del diccionario sobre el archivo comprimido.

## Uso
1. Generar el diccionario, pudiendo indicar además de las cadenas iniciales, la longitud máxima de combinación y el destino del archivo.

```shell
$ python3 diccionario/diccionario.py 1 5 -p datos.txt
Datos cargados del fichero: .\datos.txt
Número de combinaciones: 1508597

Generada claves de longitud (1)
Generada claves de longitud (2)
Generada claves de longitud (3)
Generada claves de longitud (4)
Generada claves de longitud (5)

Tiempo transcurrido: 3.95953s
Diccionario generado: diccionario.txt
```

2. Una vez generado el diccionario, indicamos el archivo comprimido y el diccionario, para comprobar una a una las claves del diccionario.

```shell
$ python3 fuerzaBruta/fuerzaBruta.py -c comprimido.zip -d diccionario.txt

 |■■■■■■■■■■■■■■■■■■■■■■■-----------------| 60% Completado

Tiempo transcurrido: 13.82808s
Clave: rubiopedro
```
## Formato archivo de cadenas
Este se usa como los datos iniciales para generar el diccionario, se trata de un archivo de texto en el cual cada línea contiene una única palabra sin espacios. Ilustramos con el siguiente ejemplo.

```txt
pedro
garcia
rubio
```
## Salida del diccionario
```txt
...
igap
igae
igad
igar
igao
igag
igaa
igac
igai
igau
igab
igcp
...
```

## Ayuda

1. diccionario.py

```shell
$ python3 diccionario/diccionario.py -h
usage: diccionario.py [-h] min max -p PALABRAS [-d DESTINO]

positional arguments:
  min                   Longitud mínima de combinaciones
  max                   Longitud máxima de combinaciones

optional arguments:
  -h, --help            show this help message and exit
  -p PALABRAS, --palabras PALABRAS
                        Lista de cadenas de entrada
  -d DESTINO, --destino DESTINO
                        Directorio del diccionario generado
```

2. fuerzaBruta.py

```shell
$ python3 fuerzaBruta/fuerzaBruta.py -h
usage: fuerzaBruta.py [-h] -c COMPRIMIDO -d DICCIONARIO [-a ARCHIVODESTINO]

optional arguments:
  -h, --help            show this help message and exit
  -c COMPRIMIDO, --comprimido COMPRIMIDO
                        archivo comprimido de entrada
  -d DICCIONARIO, --diccionario DICCIONARIO
  -a ARCHIVODESTINO, --archivoDestino ARCHIVODESTINO
                        directorio del archivo extraido
```

## Algoritmo de generación
Producto cartesiano de vector de caracteres, iniciando con las palabras base; se trata de todas las posibles combinaciones de un juego de caracteres con repetición.

![Alt text](./diagramas/producto.png)

## Producto cartesiano concurrente
El producto cartesiano de dos o mas vectores se peude descomponer, el primero en subpartes, y que a su vez hilos en cada uno calculen resultados parciales para combinarlos todos después.

![Alt text](./diagramas/productoConcurrente.png)

## Modulos utilizados
- itertools
- multiprocessing
- argparse
- time
- zipfile

## Problemas
1. Eficiencia del algoritmo producto cartesiano
2. Eficiencia de descompresion de zipLib
3. ziplib funciona con ZipCrypto y no con AES-256 (compresión en 7zip)
