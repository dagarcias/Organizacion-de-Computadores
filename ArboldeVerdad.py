import ArbolDeHuffman
from Pruebas2 import switchL

class node:

    def __init__(self, frecuencia, enumeracion):
        self.izq = None
        self.der = None
        self.frecuencia = frecuencia
        self.simbolos = None
        self.enumeracion = enumeracion

    def get_enumeracion(self):
        return self.enumeracion

    def get_frecuencia(self):
        return self.frecuencia

    def set_izq(self, hijoizq):
        self.izq = hijoizq

    def set_der(self, hijoder):
        self.der = hijoder

    def get_izq(self):
        return self.izq

    def get_der(self):
        return self.der

    def set_simbolo(self, simbolo):
        self.simbolos = simbolo

    def get_simbolo(self):
        return self.simbolos


class arbol:
    def __init__(self, raiz):
        self.raiz = raiz


lista = ArbolDeHuffman.main()
listaFrecuencia = ArbolDeHuffman.returnFrecuencias()
lista.reverse()
n = 107

resta = 1
nodoUsado = [1]

def crearArbol():
    global resta
    raiz = node(lista[0][2], 2*n-resta)
    resta += 1   
    raiz.set_izq(node(lista[0][0], 2*n-resta))
    resta += 1
    raiz.set_der(node(lista[0][1], 2*n-resta))
    
    for x in range(0,len(lista)-1):
        nodoUsado.append(0)  
    
    crearNodos(raiz.get_izq(), lista[0][0])  
    crearNodos(raiz.get_der(), lista[0][1])
    return raiz


def crearNodos(nodo, valor):
    global resta
    indiceItem = 0
    for item in lista:
        if item[2] == valor and nodoUsado[indiceItem] == 0:
            nodoUsado[indiceItem] = 1
            resta +=1
            nodo.set_izq(node(item[0], 2*n-resta))
            crearNodos(nodo.get_izq(), item[0])
            
            resta += 1
            nodo.set_der(node(item[1], 2*n-resta))
            crearNodos(nodo.get_der(), item[1])
            break
        indiceItem += 1
    

nodosHojas = []
def hallarHojas(nodo): 
    if nodo.get_izq() == None and nodo.get_der() == None:
        nodosHojas.append(nodo)
    else:
        hallarHojas(nodo.get_izq())
        hallarHojas(nodo.get_der())
    return nodosHojas
        
def infijo(nodo):
    if nodo != None:
        infijo(nodo.get_izq())
        print("")
        print("")
        print(
            f"[{nodo.get_simbolo(), nodo.get_frecuencia(), nodo.get_enumeracion()}]")
        infijo(nodo.get_der())

raiz = crearArbol()
listaHojas = hallarHojas(raiz)

def añadirSimbolos(listaHojas, listaOrden):
    hojasUsadas = []
    for x in listaOrden:
        hojasUsadas.append(0)
    
    for hoja in listaHojas:
        final = False
        indice = 0
        while not final:
            if listaOrden[indice][1] == hoja.get_frecuencia():
                hoja.set_simbolo(listaOrden[indice][0])
                listaOrden.pop(indice)
                final = True
            indice += 1

listaOrden = switchL(listaFrecuencia)
añadirSimbolos(listaHojas, listaOrden)
infijo(raiz)

datosHojas = []
for i in listaHojas:
    datosHojas.append(i.get_frecuencia())
    
print(f"HOJAS: {datosHojas}")


input('enter para salir: ')
