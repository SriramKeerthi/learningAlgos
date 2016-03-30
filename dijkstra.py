import sys
import random
from collections import OrderedDict
from queue import PriorityQueue

class Graph():
    def __init__(self):
        self._graph = OrderedDict()
        self._vertices = set()

    def __str__(self):
        return ", ".join([v + " -> (" + ", ".join([w for w in self._graph[v]]) + ")" for v in self._graph])

    def addEdge(self, v1, v2, w = 1):
        self._vertices.add(v1)
        self._vertices.add(v2)

        if v1 not in self._graph:
            self._graph[v1] = OrderedDict()
        self._graph[v1][v2] = w

    def dijkstra(self, source):
        dist = {}
        prev = {}
        dist[source] = 0
        pq = PriorityQueue()
        for v in self._vertices:
            pq.put((sys.maxsize, v))

        while not pq.empty():
            u = pq.get()[1]
            if u in self._graph and u in dist:
                for v in self._graph[u]:
                    newDist = self._graph[u][v] + dist[u]
                    if v not in dist or newDist < dist[v]:
                        dist[v] = newDist
                        prev[v] = u
                        pq.put((newDist, v))

        return dist, prev

    def getPath(prev, v):
        path = " -> " + v
        while v in prev:
            v = prev[v]
            path = " -> " + v + path
        return "*" + path

def main():
    random.seed(2)
    g = Graph()
    vertexCount = 10
    vertices = [chr(65 + i) for i in range(0, vertexCount)]
    for i in range(0, vertexCount * 2):
        v1 = chr(65 + random.randint(0, vertexCount - 1))
        v2 = chr(65 + random.randint(0, vertexCount - 1))
        if v1 != v2:
            g.addEdge(v1, v2)
    print(g)

    source = vertices[0]
    dist, prev = g.dijkstra(source)
    
    for v in [v for v in vertices if v in dist]:
        print("Vertex: {}, Shortest Distance: {}, Shortest Path: {}".format(v, dist[v], Graph.getPath(prev, v)))

if __name__ == "__main__":
    main()