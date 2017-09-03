#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lowest Common Ancestor

@author: sriram
"""

import random

def lca(root, a, b):
    if root is None:
        return None
    if a < root["value"] and b < root["value"]:
        return lca(root["left"], a, b)
    elif a > root["value"] and b > root["value"]:
        return lca(root["right"], a, b)
    else:
        return root
    
def _add(root, node):
    if root is None:
        return node
    else:
        if root["value"] < node["value"]:
            root["right"] = _add(root["right"], node)
        else:
            root["left"] = _add(root["left"], node)
    return root

def add(root, v):
    node = {}
    node["value"] = v
    node["left"] = None
    node["right"] = None
    return _add(root, node)

def main():
    arr = list(range(20))
    random.seed(1)
    random.shuffle(arr)
    arr = [30, 15, 45, 7, 22, 37, 52]
    root = None
    for i in arr:
        root = add(root, i)
    print(root)
    a = 15
    b = 22
    print(a, b, lca(root, a, b)["value"])

if __name__ == "__main__":
    main()