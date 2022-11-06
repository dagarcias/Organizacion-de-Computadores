from operator import itemgetter
from Pruebas import diccionario

lista=[[65, 2], [82, 2], [79, 1], [90, 1], [0, 2], [68, 1], [69, 1], [84, 1], [85, 1], [78, 1]]

def switchL(lista):
    x=(sorted(lista, key=itemgetter(1,0)))
    for i in x:
        buscar=i[0]
        for nombre, numero in diccionario.items():
            if numero == buscar:
                i[0]=nombre
    return x

