#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Subset sum

@author: sriram
"""
import random

def subsum(arr):
    maxval = max(arr)
    mat = []
    for i in range(len(arr)):
        mat.append([None] * (maxval**2 + 1))
    for target in range(maxval**2 + 1):
        for row,num in enumerate(arr):
            if target == 0:
                mat[row][target] = True
            elif row == 0:
                mat[row][num] = True
            else:
                mat[row][target] = mat[row - 1][target] or mat[row - 1][target - num]
            
    return mat

def printMat(mat):
    strVal = ""
    for arr in mat:
        for i in arr:
            strVal = strVal + str(i) + "\t"
        strVal = strVal + "\n"
    print(strVal)
    
def main():
    random.seed(0)
#    arr = [i for i in range(10) if random.randint(0,1) == 0]
    arr = [3, 3, 3]
    mat = subsum(arr)
    print(arr)
    printMat(mat)
    print(mat[-1][9])
    

if __name__ == "__main__":
    main()