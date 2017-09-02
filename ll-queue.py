#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Queues

@author: sriram
"""

class Queue():
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.size = 0
        self.head = None
        self.tail = None
        
    def enqueue(self, n):
        if self.size < self.maxSize:
            self.size = self.size + 1
            node = {}
            node["value"] = n
            node["next"] = None
            if self.head == None:
                self.head = node
                self.tail = node
            else:
                self.tail["next"] = node
                self.tail = node
            return True
        else:
            return False
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head["value"]
    
    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            self.size = self.size - 1
            node = self.head
            self.head = node["next"]
            return node["value"]
    
    def isEmpty(self):
        return self.size == 0
    
def main():
    a = Queue(20)
    for i in range(21):
        print(a.enqueue(i))
        
    for i in range(15):
        print(a.peek(), a.dequeue())

    for i in range(5):
        print(a.enqueue(i))

    for i in range(11):
        print(a.peek(), a.dequeue())
        
if __name__ == "__main__":
    main()