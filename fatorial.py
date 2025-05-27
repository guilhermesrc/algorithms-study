#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 26 23:14:14 2025

@author: guilherme
"""

def fat(n):
    if n==1:
        return n
    else:
        return n* fat(n-1)
    