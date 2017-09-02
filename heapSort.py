#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Heap Sort in Python

@author: sriram
"""
import random

def heapify(arr, n, i):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2
    
    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)

def _heapSort(arr):
    n = len(arr)
    
    # Build the heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Do the sorting
    for i in range(n - 1, 0, -1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr, i, 0)
        
def heapSort(li):
    liCopy = list(li)
    _heapSort(liCopy)
    return liCopy

def main():
    li = list(range(0,30))
    random.shuffle(li)
    print(li)
    print(heapSort(li))
    
if __name__ == "__main__":
    main()

