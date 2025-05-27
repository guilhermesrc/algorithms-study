#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 27 09:02:49 2025

@author: guilherme
"""

def pesquisa_binaria_rec(lista,item,inicio,fim):
    if len(lista) == 1:
        if item == lista[0]:
            return 0
        else:
            return None
    else:
        if inicio<=fim:
            medio= (inicio+fim)//2
            chute = lista[medio]
            if chute == item:
                return medio
            elif chute > item:
                fim = medio-1
                return pesquisa_binaria_rec(lista,item,inicio,fim)

            else:
                inicio = medio+1
                return pesquisa_binaria_rec(lista,item,inicio,fim)
    return None

lista = [2,3,4,5]
print(pesquisa_binaria_rec(lista,3,0,len(lista)-1))