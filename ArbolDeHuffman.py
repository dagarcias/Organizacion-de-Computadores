import Pruebas

txt = input("Introduce el texto: ")
x = list(txt)

ValoresDelArbol = [[0, 0, 0]]
listaValorxFrecuencia = Pruebas.GetData(x)

def lista():
    listainterna=[]
    for i in listaValorxFrecuencia:
        listainterna.append(i[1])
    return listainterna



lista=lista() 






minimo = 0
minimos = []

def valmins():
    cont2 = 0
    ws = len(lista)

    for i in range(0, ws+1):
        if cont2 < 2:
            minimo = min(lista)
            minimos.append(minimo)
            lista.remove(minimo)
            cont2 = cont2+1
    return minimos


def summin():
    h = len(minimos)
    suma = 0
    x = minimos[0]
    if h >= 2:
        y = minimos[1]
        suma = x+y
        lista.append(suma)
    else:
        suma = x
        lista.append(suma)
    return suma


def main():
    x = 0
    l = 0
    cont1 = 0
    while len(lista) != 1:
        l = valmins()
        x = summin()
        ValoresDelArbol.append([l[0], l[1], x])
        minimos.pop()
        minimos.pop()
        cont1 = cont1+1

    ValoresDelArbol.pop(0)
    return ValoresDelArbol

def returnFrecuencias():
    return listaValorxFrecuencia
