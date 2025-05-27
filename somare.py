#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 26 23:22:34 2025

@author: guilherme
"""

def soma(arr):
    if arr == []:
        return 0
    else:
        valor = arr[0]
        print(arr[1:])
        return valor+soma(arr[1:])
    
def conta(lista):
    if lista == []:
        return 0
    else:
        return 1 + (conta(lista[1:]))

def maioral(lista):
    if len(lista) == 2:
        return lista[0] if lista[0]>lista[1] else lista[1]
    else:
        maior = lista[0]
        if maior>maioral(lista[1:]):
            return maior
        else:
            return maioral(lista[1:])
    
