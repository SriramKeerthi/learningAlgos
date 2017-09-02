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
        
def main():
    random.seed(1)
    g = Graph()
    for v in ['A', 'B', 'C', 'D', 'E']:
        for u in ['A', 'B', 'C', 'D', 'E']:
            if v != u:
                if random.randint(0, 1) == 0:
                    g.addEdge(v, u)
    
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
    
    print(g.graph)
    print(g.stronglyConnected())
    print(g.traverseDFS('D'))
if __name__ == "__main__":
    main()