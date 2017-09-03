#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Longest increasing subsequence

@author: sriram
"""

import random

def lis(arr):
    lisList = [[i] for i in arr]
    maxLen = 0
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[j] < arr[i]:
                if len(lisList[j]) + 1 > len(lisList[i]):
                    lisList[i] = list(lisList[j])
                    lisList[i].append(arr[i])
                    if len(lisList[maxLen]) < len(lisList[i]):
                        maxLen = i
    return (len(lisList[maxLen]), lisList[maxLen])

def lisOLogN(arr):
    lisList = [[arr[0]]]
    for i in range(1, len(arr)):
        if lisList[-1][-1] < arr[i]:
            newL = list(lisList[-1])
            newL.append(arr[i])
            lisList.append(newL)
        else:
            for j in range(len(lisList) - 1, -2, -1):
                if j == -1:
                    lisList[0] = [arr[i]]
                else:
                    if lisList[j][-1] < arr[i]:
                        newL = list(lisList[j])
                        newL.append(arr[i])
                        if j == len(lisList) - 1:
                            lisList.append(newL)
                        else:
                            lisList[j + 1] = newL
                        break
    return (len(lisList[-1]),lisList[-1])

def main():
    random.seed(1)
    arr = list(range(20))
    random.shuffle(arr)
    print(arr)
    print(lis(arr[:]))
    print(lisOLogN(arr[:]))

if __name__ == "__main__":
    main()