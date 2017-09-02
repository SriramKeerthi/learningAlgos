#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sieve of Eratosthenes

@author: sriram
"""

def printNPrimes(n):
    flag = [True] * n
    flag[0] = False
    flag[1] = False
    for i in range(2,n):
        if flag[i]:
            for j in range(i*2,n,i):
                flag[j] = False
    print([i for i in range(0,n) if flag[i]])

def main():
    n = 100
    printNPrimes(n)

if __name__ == "__main__":
    main()
