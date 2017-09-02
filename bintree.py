#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Binary Search Tree

@author: sriram
"""

class Bintree():
    def __init__(self):
        self.root = None

    def _insert(self, root, node):
        if root is None:
            return node
        else:
            if root["value"] > node["value"]:
                root["left"] = self._insert(root["left"], node)
            else:
                root["right"] = self._insert(root["right"], node)
            return root
    
    def insert(self, n):
        node = {}
        node["left"] = None
        node["right"] = None
        node["value"] = n
        self.root = self._insert(self.root, node)
    
    def printInOrder(self):
        self._printInOrder(self.root)
    
    def _printInOrder(self, root):
        if root is not None:
            self._printInOrder(root["left"])
            print(root["value"], end=',')
            self._printInOrder(root["right"])

def main():
    a = Bintree()
    a.insert(5)
    a.insert(2)
    a.insert(7)
    a.insert(4)
    a.insert(10)
    a.insert(8)
    a.printInOrder()

if __name__ == "__main__":
    main()
    