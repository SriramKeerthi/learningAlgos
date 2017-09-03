#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GCD

@author: sriram
"""

def gcd(a,b):
    if a == 0 or b == 0:
        return 1
    
    if a == b:
        return a
    
    if a > b:
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)
    

def main():
    print(gcd(12,8))

if __name__ == "__main__":
    main()