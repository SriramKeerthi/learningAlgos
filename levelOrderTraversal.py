#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Level-order traversal

@author: sriram
"""
from queue import Queue

def _add(root, m, node):
    if root["value"] == m:
        if root["left"] is None:
            root["left"] = node
            return True
        else:
            root["right"] = node
            return True
    else:
        if root["left"] is not None or root["right"] is not None:
            if root["left"] is not None:
                if _add(root["left"], m, node):
                    return True
            if root["right"] is not None:
                return _add(root["right"], m, node)
        return False
        
def add(root, m, n):
    if root is None:
        root = {}
        root["value"] = m
        root["left"] = None
        root["right"] = None
    node = {}
    node["value"] = n
    node["left"] = None
    node["right"] = None
    _add(root, m, node)
    return root

def levelOrderTraversal(root):
    q = Queue()
    q.put((root, 0))
    prev_lv = 0
    while not q.empty():
        (node, lv) = q.get()
        if prev_lv != lv:
            prev_lv = lv
            print()
        print(node["value"], end=" ")
        if node["left"] is not None:
            q.put((node["left"], lv+1))
        if node["right"] is not None:
            q.put((node["right"], lv+1))
    
def main():
    root = None
    root = add(root, "Jon", "Mark")
    root = add(root, "Jon", "David")
    root = add(root, "Mark", "Paul")
    root = add(root, "Paul", "Lee")
    root = add(root, "Paul", "Steve")
    
    levelOrderTraversal(root)

if __name__ == "__main__":
    main()