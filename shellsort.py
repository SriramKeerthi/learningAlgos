# -*- coding: utf-8 -*-
"""
Shell sort

@author: Sriram
"""

import random

def _shellSort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j = j - gap
            arr[j] = temp
        gap = gap // 2
    return arr

def shellSort(arr):
    return _shellSort(list(arr))

def main():
    arr = list(range(20))
    random.shuffle(arr)
    print(arr)
    print(shellSort(arr))
    
if __name__ == "__main__":
    main()