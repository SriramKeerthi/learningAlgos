#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Knapsack problem

@author: sriram
"""

#import random

def _knapsack(wv, n, target, kmap):
    if n == 0 or target == 0:
        return 0
    else:
        (weight, value) = wv[n - 1]
        if n not in kmap:
            kmap[n] = {}
        if target not in kmap[n]:
            if target >= weight:
                kmap[n][target] = max(value + _knapsack(wv, n-1, target - weight, kmap), 
                                _knapsack(wv, n-1, target, kmap))
            else:
                kmap[n][target] = _knapsack(wv, n-1, target, kmap)
        return kmap[n][target]
        
def knapsack(wv, target):
    return _knapsack(wv, len(wv), target, {})
    
def main():
    wv=[(10,60),(20,100),(30,120)]
    print(knapsack(wv, 40))

if __name__ == "__main__":
    main()