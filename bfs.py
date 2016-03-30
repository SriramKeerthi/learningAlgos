import random
from collections import OrderedDict

class Graph():
    def __init__(self):
        self._graph = OrderedDict()

    def __str__(self):
        return ", ".join([v + " -> (" + ", ".join([w for w in self._graph[v]]) + ")" for v in self._graph])

    def addEdge(self, v1, v2, w = 1):
        if v1 not in self._graph:
            self._graph[v1] = OrderedDict()
        self._graph[v1][v2] = w

    def bfs(self, v):
        return self._bfs(v, OrderedDict({v: "* -> " + v}))

    def _bfs(self, v, visited):
        if v in self._graph:
            toVisit = set()
            for w in self._graph[v]:
                if w not in visited:
                    visited[w] = v + " -> " + w
                    toVisit.add(w)
            for w in toVisit:
                self._bfs(w, visited)
        return visited

def main():
    random.seed(1)
    g = Graph()
    vertexCount = 5
    vertices = [chr(65 + i) for i in range(0, vertexCount)]
    for i in range(0, vertexCount * 2):
        v1 = chr(65 + random.randint(0, vertexCount - 1))
        v2 = chr(65 + random.randint(0, vertexCount - 1))
        if v1 != v2:
            g.addEdge(v1, v2)
    print(g)
    for v in vertices:
        print("Vertex: {}, Visited: {}".format(v,g.bfs(v)))

if __name__ == "__main__":
    main()