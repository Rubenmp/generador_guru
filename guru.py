#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Programa para completar el juego Palabras Gurú """

import enchant
import copy
from sets import Set


class Arbol:
    def __init__(self, diccionario, letras):
        'Constructor'
        self.diccionario = diccionario
        self.letras = letras
        self._letras_usadas = [False]*len(letras)
        self._palabras_cod = [] # Palabras codificadas
        self._palabra_actual = []
        
    def busqueda_profundidad(self):
        'Busca las palabras del diccionario español que se generan con determinadas letras'
        self._palabras_cod = []
        self._busqueda_profundidad_rec()
        palabras = []
        for palabra in self._palabras_cod:
            palabras.append(self._palabra2string(palabra))

        return eliminar_repetidas(palabras)


    def _busqueda_profundidad_rec(self):
        self._comprobar_palabra(self._palabra_actual)

        # Hacemos copia profunda de las variables
        c_letras_usadas  = copy.deepcopy(self._letras_usadas)
        c_palabra_actual = copy.deepcopy(self._palabra_actual)
        
        ramas = self._generar_hijos() # Genera los números de las letras libres
        for hijo in ramas:
            self._letras_usadas[hijo] = True
            self._palabra_actual.append(hijo)
            
            self._busqueda_profundidad_rec()
            
            self._letras_usadas[hijo] = False
            self._palabra_actual = self._palabra_actual[:-1] # Quitamos la última letra

            
    def _generar_hijos(self):
        'Permite la búsqueda en el árbol'
        hijos = []
        for index, val in enumerate(self._letras_usadas):
            if (val == False):
                hijos.append(index)
                
        return hijos

    
    def _comprobar_palabra(self, palabra):
        'Comprueba si la palabra existe en el diccionario'
        if (len(palabra) != 0):
            if (self.diccionario.check(self._palabra2string(palabra))):
                self._palabras_cod.append(copy.deepcopy(palabra))

                
    def _palabra2string(self, palabra):
        'Convierte una secuencia de números en el string correspondiente'
        #print(palabra)
        ret = ""
        for i in palabra: # Palabra es un vector de números
            ret += self.letras[i]
            
        return ret

    
def eliminar_repetidas(palabras):
    'Elimina palabras repetidas'
    conjunto = Set()
    for i in palabras:
        conjunto.add(i)
        
    return list(conjunto)


def imprimir(palabras):
    'Cálculo palabra más larga'
    max = 0
    for i in palabras:
        if (len(i) > max):
            max = len(i)
            
    palabras_ordenadas = [None]*(max+1)        
    for i in range(len(palabras_ordenadas)):
        palabras_ordenadas[i] = []
    
    for i in palabras:
        palabras_ordenadas[len(i)].append(i)
    
    for index, val in enumerate(palabras_ordenadas):
        if (index != 0):
            print("Palabras de longitud {}: ".format(index))
            print(val)


def main():
    dic =  enchant.Dict("es_ES")
    while (True):
        letras = raw_input('Letras que aparecen (incluye tildes): ')
        arbol = Arbol(dic, letras)
        palabras = arbol.busqueda_profundidad()
        imprimir(palabras)
        print(" ")

    
if __name__ == "__main__":
    main()
