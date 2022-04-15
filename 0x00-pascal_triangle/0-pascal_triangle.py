#!/usr/bin/python3
"""
Pascals triangle
"""


def pascal_triangle(n):
    """
    triangle
    """
    lista = []
    if n > 0:
        for i in range(n):
            lista.append([])
            lista[i].append(1)
            for tmp in range(1, i):
                lista[i].append(lista[i - 1][tmp - 1] + lista[i - 1][tmp])
            if i != 0:
                lista[i].append(1)

    return lista