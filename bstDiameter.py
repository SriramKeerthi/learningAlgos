#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BST Diameter

@author: sriram
"""

import random

def add(root, node):
    if root is None:
        return node
    else:
        if root["value"] > node["value"]:
            root["left"] = add(root["left"], node)
        else:
            root["right"] = add(root["right"], node)
        return root

def printInOrder(root):
    if root is not None:
        printInOrder(root["left"])
        print(root["value"],end=".")
        printInOrder(root["right"])
    else:
        print("",end=".")

def height(root):
    if root is None:
        return 0
    else:
        return 1 + max(height(root["left"]), height(root["right"]))

def diameter(root):
    if root is None:
        return 0
    else:
        return max(1 + height(root["left"]) + height(root["right"]), max(diameter(root["left"]), diameter(root["right"])))

def main():
    root = None
    vals = list(range(7))
    random.seed(0)
    random.shuffle(vals)
    for v in vals:
        print(v)
        node = {}
        node["left"] = None
        node["right"] = None
        node["value"] = v
        root = add(root, node)
    printInOrder(root)
    print()
    print(height(root))
    print(diameter(root))
    
if __name__ == "__main__":
    main()
    