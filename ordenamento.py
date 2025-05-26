#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 25 21:46:52 2025

@author: guilherme
"""

def busca_menor(array):
    menor = array[0]
    menor_indice = 0
    for i in range(1,len(array)):
        if array[i] <= menor:
            menor_indice = i
            menor = array[menor_indice]
    return menor_indice

def ordenacao_por_selecao(arr):
    lista_ord = []
    for n in range(len(arr)):
        menor = busca_menor(arr)
        lista_ord.append(arr.pop(menor))
        
    return lista_ord

lista = [3,4,5,2,321,13,12,20,1,0,2,4,3,7,5,139,-1]
print(ordenacao_por_selecao()