# -*- coding: utf-8 -*-
"""
Max sublist product

@author: SriramKeerthi
"""
import random

def max_subproduct(arr):
    if len(arr) == 0:
        return 0
    
    max_i = arr[0]
    min_i = arr[0]
    max_v = arr[0]
    
    for i in range(1,len(arr)):
        prev_max,prev_min = max_i,min_i
        max_i = max(arr[i], arr[i]*prev_min, arr[i]*prev_max)
        min_i = min(arr[i], arr[i]*prev_min, arr[i]*prev_max)
        max_v = max(max_v, max_i)
    
    return max_v

def main():
    arr = list(range(-5,20))
    random.shuffle(arr)
    arr = [60, 2, -0.0001, 999]
    print(arr)
    print(max_subproduct(arr))

if __name__ == "__main__":
    main()