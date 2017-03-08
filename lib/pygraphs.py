""" Pygraphs

Graph library, this file should be splitted when goes bigger.
"""

__author__ = 'Ales Lerch'


import os
import sys


class MaticeSousednosti:

    def __init__(self,pocetVrcholu):
        self.matice = {}
        for poc in range(1,len(pocetVrcholu)+1):
            self.matice[poc] = {}

    def pridejVrchol(self):
        pass

    def oddelejVrchol(self):
        pass

    def vypisMS(self):
        pass

    def vratKlice(self):
        return [x for x in self.matice.keys()]

    def vratHodnoty(self):
        return [x for x in self.matice.values()]

def check():
    print('working neco')
