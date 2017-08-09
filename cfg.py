#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def main():
    prin("Descargando diccionario español")
    os.system('wget -O ./dic/es_ES.aff "https://raw.githubusercontent.com/sbosio/rla-es/master/source-code/hispalabras-0.1/hispalabras/es_ES.aff"')
    os.system('wget -O ./dic/es_ES.dic "https://raw.githubusercontent.com/sbosio/rla-es/master/source-code/hispalabras-0.1/hispalabras/es_ES.dic"')

    print("Descargando programa unmunch para generar el diccionario completo a partir de los archivos .dic y .aff")
    os.system('wget -O ./dic/unmunch.cxx "https://raw.githubusercontent.com/hunspell/hunspell/master/src/tools/unmunch.cxx"')
    os.system('wget -O ./dic/unmunch.h "https://raw.githubusercontent.com/hunspell/hunspell/master/src/tools/unmunch.h"')
    os.system('g++ -o ./dic/unmunch ./dic/unmunch.cxx')

    print("Generando diccionario")
    os.system('./dic/unmunch ./dic/es_ES.dic ./dic/es_ES.aff 2> /dev/null > ./dic/es_ES.txt.bk')
    os.system('sort ./dic/es_ES.txt.bk > ./dic/es_ES.txt')
    os.system('rm -f ./dic/es_ES.txt.bk')


if __name__ == "__main__":
    main()
