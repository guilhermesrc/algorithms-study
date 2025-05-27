#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 25 12:29:16 2025

@author: guilherme


lista = [1,5,6,7,8,9]
item = 7
3
"""
def pesquisa_binaria(lista,item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        medio= (baixo+alto)//2
        chute = lista[medio]
        if chute == item:
            return medio
        if chute > item:
            alto = medio-1
        else:
            baixo = medio+1
    return None

def pesquisa_normal(lista,item):
    c=0
    i = lista[c]
    while i != item:
        i = lista[c]
        c+=1
        if i==item:
            return c-1
    return None

lista = [1,5,6,7,8,9]
item = 8
print(pesquisa_binaria(lista, item))
print(pesquisa_normal(lista, item))
