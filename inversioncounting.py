#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inversion counting

@author: sriram
"""

import random

def _merge(arr, startIndex, midIndex, stopIndex):
    count = 0
    li = []
    i = startIndex
    j = midIndex
    while i < midIndex and j < stopIndex:
        while i < midIndex and arr[i] < arr[j]:
            li.append(arr[i])
            i = i + 1
        while j < stopIndex and arr[j] < arr[i]:
            li.append(arr[j])
            j = j + 1
            count = count + (midIndex - i)
    while i < midIndex:
        li.append(arr[i])
        i = i + 1
    while j < stopIndex:
        li.append(arr[j])
        j = j + 1
    for i in range(startIndex, stopIndex):
        arr[i] = li[i - startIndex]
    return count

            

def _mergeSort(arr, startIndex, stopIndex):
    count = 0
    if startIndex < stopIndex - 1:
        midIndex = (startIndex + stopIndex) // 2
        count = count + _mergeSort(arr, startIndex, midIndex)
        count = count + _mergeSort(arr, midIndex, stopIndex)
        count = count + _merge(arr, startIndex, midIndex, stopIndex)
    return count

def countInversion(arr):
    arrCopy = list(arr)
    count = _mergeSort(arrCopy, 0, len(arrCopy))
    print(arrCopy)
    return count

def main():
    arr = list(range(0,5))
    random.shuffle(arr)
    
    arr = [12,11,13,5,6,7]
    print(arr)
    print(countInversion(arr))


if __name__ == "__main__":
    main()