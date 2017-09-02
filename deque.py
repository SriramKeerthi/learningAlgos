#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deque

@author: sriram
"""

class Deque():
    def __init__(self):
        self.left = None
        self.right = None
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def enqueueFirst(self, v):
        self.size = self.size + 1
        node = {}
        node["value"] = v
        node["left"] = None
        node["right"] = self.left
        if self.right is None:
            self.right = node
        else:
            self.left["left"] = node
        self.left = node
    
    def enqueueLast(self, v):
        self.size = self.size + 1
        node = {}
        node["value"] = v
        node["left"] = self.right
        node["right"] = None
        if self.left is None:
            self.left = node
        else:
            self.right["right"] = node
        self.right = node
        
    def dequeueFirst(self):
        if self.isEmpty():
            return None
        else:
            self.size = self.size - 1
            node = self.left
            self.left = self.left["right"]
            if self.left == None:
                self.right = None
            else:
                self.left["left"] = None
            return node["value"]
    
    def dequeueLast(self):
        if self.isEmpty():
            return None
        else:
            self.size = self.size - 1
            node = self.right
            self.right = self.right["left"]
            if self.right == None:
                self.left = None
            else:
                self.right["right"] = None
            return node["value"]
    
    def peekFirst(self):
        if self.isEmpty():
            return None
        else:
            return self.left["value"]
    
    def peekLast(self):
        if self.isEmpty():
            return None
        else:
            return self.right["value"]
    
def main():
    q = Deque()
    print(q.dequeueFirst())
    print(q.dequeueLast())
    print(q.peekFirst())
    print(q.peekLast())
    for i in range(20):
        q.enqueueFirst(i)
    for i in range(21):
        print(q.peekFirst(), q.dequeueFirst())

    for i in range(20):
        q.enqueueLast(i)
    for i in range(21):
        print(q.peekLast(), q.dequeueLast())

    for i in range(20):
        q.enqueueFirst(i)
    for i in range(21):
        print(q.peekLast(), q.dequeueLast())

    for i in range(20):
        if i % 2 == 0:
            q.enqueueFirst(i)
        else:
            q.enqueueLast(i)
    for i in range(22):
        print(q.peekLast(), q.dequeueLast())

    for i in range(20):
        q.enqueueFirst(i)
    for i in range(22):
        if i % 2 == 0:
            print(q.peekFirst(), q.dequeueFirst())
        else:
            print(q.peekLast(), q.dequeueLast())

if __name__ == "__main__":
    main()