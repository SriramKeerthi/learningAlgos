#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quickselect

@author: sriram
"""
import random

def _partition(arr, startIndex, stopIndex):
    pivot = arr[(startIndex + stopIndex)//2]
    while True:
        while arr[startIndex] < pivot:
            startIndex = startIndex + 1
        while arr[stopIndex] > pivot:
            stopIndex = stopIndex - 1
        if startIndex >= stopIndex:
            return stopIndex
        arr[startIndex],arr[stopIndex] = arr[stopIndex],arr[startIndex]
        startIndex = startIndex + 1
        stopIndex = stopIndex - 1

def _quickSelect(arr, startIndex, stopIndex, k):
    if startIndex == stopIndex:
#        print("Index bs")
        return arr[startIndex]

    pivotIndex = _partition(arr, startIndex, stopIndex)
#    if pivotIndex == k:
#        return arr[k]
    if k <= pivotIndex:
#        print(k, arr[pivotIndex], arr, arr[startIndex:pivotIndex + 1])
        return _quickSelect(arr, startIndex, pivotIndex, k)
    else:
#        print(k, arr[pivotIndex], arr, arr[pivotIndex + 1:stopIndex + 1])
        return _quickSelect(arr, pivotIndex + 1, stopIndex, k)

def quickSelect(arr, k):
    arrCopy = list(arr)
    qs = _quickSelect(arrCopy, 0, len(arr) - 1, k)
#    print(arrCopy)
    return qs

def main():
#    random.seed(1)
    arr = list(range(20))
    random.shuffle(arr)
    print(arr)
    for i in range(20):
        qs = quickSelect(arr, i)
        print(i, qs, i == qs)
    
if __name__ == "__main__":
    main()