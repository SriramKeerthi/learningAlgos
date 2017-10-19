#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Almost Palindrome

@author: sriram
"""

def isPalindrome(line):
    print(line)
    for i in range(len(line) // 2):
        if line[i] != line[-(i+1)]:
            return False
    return True

def almostPalindrome(line):
    lineLen = len(line)
    for i in range(lineLen//2):
        if line[i] == line[-(i+1)]:
            continue
        else:
            if lineLen % 2 == 0 and i == lineLen // 2:
                return i
            else:
                if isPalindrome(line[i+1:-i]):
                    return i
                elif isPalindrome(line[i:-(i+1)]):
                    return lineLen - i - 1
                else:
                    return -1
    return -1

def main():
    print(almostPalindrome("abcd"))

if __name__ == "__main__":
    main()