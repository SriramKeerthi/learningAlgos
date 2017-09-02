#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HeapQ

@author: sriram
"""
import random

class HeapQ():
    def __init__(self):
        self.data = []
        self.size = 0
    
    def _heapify(self, arr, i, n):
        largest = i
        left = i*2 + 1
        right = i*2 + 2
        
        if left < n and arr[left][0] < arr[largest][0]:
            largest = left
        if right < n and arr[right][0] < arr[largest][0]:
            largest = right
        
        if largest != i:
            arr[largest],arr[i] = arr[i],arr[largest]
            self._heapify(arr, largest, n)

    def enqueue(self, priority, value):
        if self.size == len(self.data):
            self.data.append((priority,value))
        else:
            self.data[self.size] = (priority,value)
        self.size = self.size + 1
        self._rebalance(self.size - 1)
        
    def _rebalance(self, pos):
        if pos > 0:
            parent = (pos - 1)//2
            if self.data[parent][0] > self.data[pos][0]:
                self.data[parent],self.data[pos] = self.data[pos],self.data[parent]
                self._rebalance(parent)

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            v = self.data[0]
            self.data[0],self.data[self.size - 1] = self.data[self.size - 1],self.data[0]
            self.size = self.size - 1
            self._heapify(self.data, 0, self.size)
            return v

    def isEmpty(self):
        return self.size == 0
    
    
def main():
    size = 20
    q = HeapQ()
    li = list(range(size + 1))
    random.shuffle(li)
    for i in li:
        q.enqueue(i, size - i)
    for i in range(size + 2):
        print(q.dequeue())
        
if __name__ == "__main__":
    main()