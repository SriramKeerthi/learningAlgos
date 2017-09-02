#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stacks using Linked Lists

@author: sriram
"""

class Stack():
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.size = 0
        self.root = None
        
    def push(self, n):
        if self.size < self.maxSize:
            self.size = self.size + 1
            node = {}
            node["value"] = n
            node["next"] = self.root
            self.root = node
            return True
        else:
            return False
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.root["value"]
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            self.size = self.size - 1
            node = self.root
            self.root = node["next"]
            return node["value"]
    
    def isEmpty(self):
        return self.size == 0
    
def main():
    a = Stack(10)
    for i in range(20):
        print(a.push(i))
        
    for i in range(21):
        print(a.peek(), a.pop())
        
if __name__ == "__main__":
    main()