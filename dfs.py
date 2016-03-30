import random

class Graph():
    def __init__(self):
        self._graph = {}

    def __str__(self):
        return str(self._graph)

    def addEdge(self, v1, v2, w = 1):
        if v1 not in self._graph:
            self._graph[v1] = {}
        self._graph[v1][v2] = w

    def dfs(self, v):
        return self._dfs(v, set())

    def _dfs(self, v, visited):
        visited.add(v)
        if v in self._graph:
            for w in self._graph[v]:
                if w not in visited:
                    self._dfs(w, visited)
        return visited

def main():
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
        print("Vertex: {}, Visited: {}".format(v,g.dfs(v)))

if __name__ == "__main__":
    main()