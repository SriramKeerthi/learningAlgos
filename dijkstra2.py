#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dijkstra's

@author: sriram
"""

import random

class Dijkstra():
    def __init__(self, n):
        self.n = n
        self.graph = []
        for i in range(n):
            self.graph.append([None]*n)

    def add(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w
        
    def __str__(self):
        strRep = ""
        for i in range(self.n):
            for j in range(self.n):
                strRep = strRep + str(self.graph[i][j]) + "\t"
            strRep = strRep + "\n"
        return strRep
    
    def shortestPath(self, v):
        spt = set()
        dist = {}
        for u in range(self.n):
            dist[u] = self.graph[u][v]
            if dist[u] is None:
                dist[u] = 9999
        dist[v] = 0
        while len(spt) < self.n:
            u = self.pick(dist, spt)
            spt.add(u)
            for ua in range(self.n):
                if self.graph[u][ua] is not None:
                    dist[ua] = min(dist[ua], dist[u] + self.graph[u][ua])
                            
        return dist
    
    def pick(self, dist, spt):
        mindist = 99999
        minv = -1
        for i in range(self.n):
            if dist[i] < mindist and i not in spt:
                mindist = dist[i]
                minv = i
        return minv

def main():
    n = 9
    d = Dijkstra(n)
    for i in range(n):
        d.add(i, i, 0)
#        for j in range(i + 1, n):
#            d.add(i, j, random.randint(1,10))
    d.add(0, 1, 4)
    d.add(0, 7, 8)
    d.add(1, 7, 11)
    d.add(1, 2, 8)
    d.add(7, 8, 7)
    d.add(7, 6, 1)
    d.add(2, 8, 2)
    d.add(8, 6, 6)
    d.add(2, 5, 4)
    d.add(6, 5, 2)
    d.add(2, 3, 7)
    d.add(3, 5, 14)
    d.add(3, 4, 9)
    d.add(5, 4, 10)
    
    print(d)
    print(d.shortestPath(0))

if __name__ == "__main__":
    main()