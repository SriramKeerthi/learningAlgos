#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
First n powers of 2

@author: sriram
"""

def npow(n, v=2):
    if n > 0:
        return v + npow(n-1, v*2)
    else:
        return 0

def main():
    print(npow(5))
    
if __name__ == "__main__":
    main()