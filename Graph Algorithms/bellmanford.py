from collections import defaultdict
import sys


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, src, dest, weight):
        self.graph.append([src, dest, weight])

    def bellmanford(self, source):
        dist = [sys.maxsize]*(self.vertices)
        dist[source] = 0

        for _ in range(self.vertices - 1):
            for u, v, w in self.graph:
                dist[v] = min(dist[v], dist[u] + w)

        # to check negative cycle
        for u, v, w in self.graph:
            if (dist[u] + w) < dist[v]:
                return 1

        return 0


for _ in range(int(input())):
    v, e = map(int, input().split())
    edges = [int(i) for i in input().split()]

    graph = Graph(v)
    for i in range(0, 3*e, 3):
        graph.add_edge(edges[i], edges[i+1], edges[i+2])

    isNegativeCycle = graph.bellmanford(0)

    print(isNegativeCycle)
