#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DFS, BFS and Strongly Connected Components

@author: sriram
"""

import random
from collections import OrderedDict

class Graph():
    def __init__(self):
        self.graph = OrderedDict()
        
    def addEdge(self, v1, v2, w = 1):
        if v1 not in self.graph:
            self.graph[v1] = []
        edgeList = self.graph[v1]
        edgeList.append((v2, w))

    def addUnorderedEdge(self, v1, v2, w = 1):
        if v1 not in self.graph:
            self.graph[v1] = []
        edgeList = self.graph[v1]
        edgeList.append((v2, w))
        if v2 not in self.graph:
            self.graph[v2] = []
        edgeList = self.graph[v2]
        edgeList.append((v1, w))
        
    def traverseDFS(self, v):
        visited = OrderedDict()
        visited[v] = (f"* -> {v}", 0)
        self._traverseDFS(self.graph, v, visited)
        return visited
    
    def _traverseDFS(self, graph, v, visited, completion = None):
        if completion is None:
            completion = []
        if v in graph:
            edgeList = graph[v]
            for (u, w) in edgeList:
                if u not in visited:
                    visited[u] = (f"{v} -> {u}", w)
                    self._traverseDFS(graph, u, visited, completion)
        completion.append(v)
        
    def traverseBFS(self, v):
        visited = OrderedDict()
        visited[v] = (f"* -> {v}", 0)
        self._traverseBFS(v, visited)
        return visited
    
    def _traverseBFS(self, v, visited):
        if v in self.graph:
            edgeList = self.graph[v]
            toTraverse = []
            for (u, w) in edgeList:
                if u not in visited:
                    visited[u] = (f"{v} -> {u}", w)
                    toTraverse.append(u)
            for u in toTraverse:
                self._traverseBFS(u, visited)

    def stronglyConnected(self):
        graph = self.graph
        keys = graph.keys()
        visited = OrderedDict()
        completion = []
        for key in keys:
            if key not in visited:
                visited[key] = (f"* -> {key}", 0)
                self._traverseDFS(graph, key, visited, completion)
        
        reverseGraph = self.reverseGraph(graph)
        
        revVisited = OrderedDict()
        stronglyConnectedComponents = []
        completion.reverse()
        print(completion)
        for key in completion:
            if key not in revVisited:
                existingKeys = set(revVisited.keys())
                revVisited[key] = (f"* -> {key}", 0)
                self._traverseDFS(reverseGraph, key, revVisited)
                
                cc = set()
                stronglyConnectedComponents.append(cc)
                for nk in revVisited.keys():
                    if nk not in existingKeys:
                        cc.add(nk)
        return stronglyConnectedComponents
    
    def reverseGraph(self, graph):
        reverse = OrderedDict()
        for key in graph.keys():
            for (v,w) in graph[key]:
                if v not in reverse:
                    reverse[v] = []
                edgeList = reverse[v]
                edgeList.append((key, w))
        return reverse
                
    def _minKey(self, mstSet, keyValue):
        minkey = None
        minweight = None
        for key,weight in keyValue.items():
            if key not in mstSet and (minweight is None or minweight > weight):
                minweight = weight
                minkey = key
        return minkey
        
    def primMst(self):
        mstSet = set()
        keys = list(self.graph.keys())
        keyValue = OrderedDict()
        keyValue[keys[0]] = 0
        path = {}
        while len(mstSet) != len(keys):
            u = self._minKey(mstSet, keyValue)
            mstSet.add(u)
            if u in self.graph:
                for (v,w) in self.graph[u]:
                    if v not in mstSet:
                        if v not in keyValue or keyValue[v] > w:
                            keyValue[v] = w
                            path[v] = (u,v,w)
                    
        return list(path.values())
            
def main():
    random.seed(1)
    g = Graph()
#    for v in ['A', 'B', 'C', 'D', 'E']:
#        for u in ['A', 'B', 'C', 'D', 'E']:
#            if v != u:
#                if random.randint(0, 1) == 0:
#                    g.addEdge(v, u, random.randint(1,3))
    
#    g.addEdge('A', 'B')
#    g.addEdge('B', 'C')
#    g.addEdge('C', 'A')
#    g.addEdge('B', 'D')
#    g.addEdge('D', 'E')
#    g.addEdge('E', 'F')
#    g.addEdge('F', 'D')
#    g.addEdge('G', 'F')
#    g.addEdge('G', 'H')
#    g.addEdge('H', 'I')
#    g.addEdge('I', 'J')
#    g.addEdge('J', 'G')
#    g.addEdge('J', 'K')
#    
    g.addUnorderedEdge("0", "1", 4)
    g.addUnorderedEdge("0", "7", 8)
    g.addUnorderedEdge("1", "7", 11)
    g.addUnorderedEdge("1", "2", 8)
    g.addUnorderedEdge("7", "8", 7)
    g.addUnorderedEdge("6", "7", 1)
    g.addUnorderedEdge("2", "8", 2)
    g.addUnorderedEdge("6", "8", 6)
    g.addUnorderedEdge("2", "3", 7)
    g.addUnorderedEdge("2", "5", 4)
    g.addUnorderedEdge("5", "6", 2)
    g.addUnorderedEdge("3", "5", 14)
    g.addUnorderedEdge("3", "4", 9)
    g.addUnorderedEdge("4", "5", 10)
    
#    g.addUnorderedEdge(0, 1, 2)
#    g.addUnorderedEdge(0, 3, 6)
#    g.addUnorderedEdge(1, 2, 3)
#    g.addUnorderedEdge(1, 4, 5)
#    g.addUnorderedEdge(1, 3, 8)
#    g.addUnorderedEdge(2, 4, 7)
#    g.addUnorderedEdge(3, 4, 9)
    
    
    
    print(g.graph)
#    print(g.stronglyConnected())
#    print(g.traverseDFS('D'))
    print(g.primMst())
    
if __name__ == "__main__":
    main()