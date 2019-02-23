## Ataque por diccionario
![Alt text](./Diagramas/flujo.png)

Existen dos fases de generación, la creación del diccionario a partir de lista de palabras y una longitud máxima de combinación, para porteriormente caomporbar todos las claves del diccionario sobre el archivo comprimido.

### Uso
1. Generar el diccionario, pudiendo indicar además de las cadenas iniciales, la longitud máxima de combinación y el destino del archivo.

```shell
$ python3 diccionario/diccionario.py -p datos.txt
Datos cargados del fichero: ./datos.txt

Longitud 1 |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■| 100% Completado
Longitud 2 |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■| 100% Completado
Longitud 3 |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■| 100% Completado
Longitud 4 |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■| 100% Completado
Longitud 5 |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■| 100% Completado

Tiempo transcurrido: 8.74589s
Diccionario generado: diccionario.txt
```

2. Una vez generado el diccionario, indicamos el archivo comprimido y el diccionario, para comprobar una a una las claves del diccionario.

```shell
$ python3 fuerzaBruta/fuerzaBruta.py -c comprimido.zip -d diccionario.txt

 |■■■■■■■■■■■■■■■■■■■■■■■-----------------| 60% Completado

Tiempo transcurrido: 13.82808s
Clave: gato85gomez
```

### Algoritmo de generación
Producto cartesiano de vector de caracteres, iniciando con las palabras base, se trata de todas las posibles combinaciones de un juego de palabreas con repetición.

![Alt text](./Diagramas/algoritmo.png)

### Dependencias
- itertools
- argparse
- time
- zipfile

### Problemas
1. Eficiencia del algoritmo producto cartesiano
2. Uso de hilos
3. Eficiencia de descompresion de zipLib
4. ziplib funciona con CryptoZip y no con AES-256 (compresión en 7zip)
