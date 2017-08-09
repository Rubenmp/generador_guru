#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Programa para completar el juego Palabras Gurú """

import copy
from sets import Set


class Guru:
    def __init__ (self, letras):
        self.letras = unicode2lista(letras)
        
    def compatible(self, palabra):
        """ Comprueba si la palabra se puede formar con las letras indicadas
        Sin repetición
        """
        valida = True
        if (len(palabra) <= len(self.letras)):
            letras = copy.deepcopy(self.letras)
            for index_i, i in enumerate(palabra):
                encontrado = False
                for index_j, j in enumerate(letras):
                    if (i == j and not encontrado):
                        letras[index_j] = None
                        encontrado = True
                if (not encontrado):
                    valida = False
        else:
            valida = False

        return valida
    
        
def unicode2lista(palabra):
    """ Convierte una palabra utf-8 en una secuencia de letras
    Sirve para separar caracteres especiales (á, ñ, ...)
    """
    ret = []
    for letra in unicode(palabra,"utf-8"):
        ret.append(letra)

    return ret


def eliminar_repetidas(palabras):
    'Elimina palabras repetidas'
    conjunto = Set()
    for i in palabras:
        conjunto.add(i)
        
    return list(conjunto)

        
def imprimir(p_palabras):
    'Imprime las palabras ordenadas por tamaño'
    if (len(p_palabras) != 0):
        max = 0 # Cálculo palabra más larga
        for i in p_palabras:
            if (len(unicode2lista(i)) > max):
                max = len(unicode2lista(i))

        palabras_ordenadas = [None]*(max+1)        
        for i in range(len(palabras_ordenadas)):
            palabras_ordenadas[i] = []
    
        for i in p_palabras:
            palabras_ordenadas[len(unicode2lista(i))].append(i)
    
        for index, val in enumerate(palabras_ordenadas):
            if (index != 0 and len(val) != 0):
                print("Palabras de longitud {}: ".format(index)),
                linea = eliminar_repetidas(val)
                for i in linea:
                    print(i),
                print("")
    else:
        print("Ningún resultado")
                    

def main():
    letras = raw_input('Letras que aparecen (incluye tildes): ')
    guru = Guru(letras)
    palabras = []

    with open("./dic/es_ES.txt", "r") as ins:
        for linea in ins:
            palabra = unicode2lista(linea.rstrip())
            if (guru.compatible(palabra)):
                palabras.append(linea.rstrip())  

    imprimir(palabras)
    
    
if __name__ == "__main__":
    main()
