#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Programa para completar el juego Palabras Gurú """

import enchant


def buscar_palabras(letras, diccionario, longitud=0):
    palabras = [None]
    if (longitud ==  0):
        for i in range(len(letras)):
            'Genera las palabras de cada longitud y las añade a palabras'
            nuevas_palabras = buscar_palabras(letras, diccionario, i+1)
            palabras.append(nuevas_palabras)
        palabras[0] = []
    else:
        palabras = []
        palabra  = [0]*longitud
        while (siguiente_palabra(palabra, len(letras)) != None):
            palabra_original = palabra2string(palabra, letras)
            if (diccionario.check(palabra_original)):
                palabras.append(palabra_original)

    return palabras
        
def siguiente_palabra(actual, num_letras):
    'Genera el árbol sin repetir letras'
    siguiente = actual
    iterar = True
    nivel = len(actual)-1

    while(iterar):
        if (actual[nivel] < (num_letras-1)):
            siguiente[nivel] += 1
            iterar = False
        else:
            siguiente[nivel] = 0
            nivel -= 1
            if (nivel < 0):
                siguiente = None
                iterar = False

    if (siguiente != None and letra_repetida(siguiente, num_letras)):
        siguiente = siguiente_palabra(siguiente, num_letras)
    
    return siguiente

def letra_repetida(palabra, num_letras):
    'Palabra será una lista de números que representarán una posición'
    rep = False
    letras = [False]*num_letras
    for i in range(len(palabra)):
        if (letras[palabra[i]] == False):
            letras[palabra[i]] = True
        else:
            rep = True

    return rep

def palabra2string(palabra, letras):
    ret = ""
    for i in palabra:
        ret += letras[i]

    return ret

def imprimir(palabras):
    for i in range(len(palabras)):
        if (i != 0):
            print("Palabras de longitud {}: ".format(i))
            print(palabras[i])

            
            
if __name__ == '__main__':
    letras = raw_input('Letras que aparecen (incluye tildes): ')
    dic =  enchant.Dict("es_ES")
    palabras = buscar_palabras(letras, dic)
    imprimir(palabras)

