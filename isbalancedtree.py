#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Balanced Binary Tree

@author: sriram
"""

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
    node["left"] = None
    node["right"] = None
    node["value"] = v
    return _add(root, node)

def maxDepth(root):
    if root is None:
        return 0
    else:
        return 1 + max(maxDepth(root["left"]), maxDepth(root["right"]))

def minDepth(root):
    if root is None:
        return 0
    else:
        return 1 + min(minDepth(root["left"]), minDepth(root["right"]))


def isBalanced(root):
    return (maxDepth(root) - minDepth(root)) <= 1

def main():
    root = add(None, 6)
    root = add(root, 3)
    root = add(root, 9)
    root = add(root, 1)
    root = add(root, 5)
    root = add(root, 7)
    root = add(root, 11)
    root = add(root, 12)
    root = add(root, 10)
    
    print(root)
    print(isBalanced(root))

if __name__ == "__main__":
    main()