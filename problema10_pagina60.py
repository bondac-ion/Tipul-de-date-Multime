"""Elaboraţi un program care afişează pe ecran toate submulţimile mulţimii {1, 2, 3, 4}."""
from itertools import chain, combinations

def boolean(iterable):
    elementele = list(iterable)
    return chain.from_iterable(combinations(elementele, i) for i in range(len(elementele)+1))
print(list(boolean([1,2,3,4])))