from collections import defaultdict
import sys


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(lambda: [])

        for i in range(1, self.vertices+1):
            if (i+1) <= self.vertices:
                self.add_edge(i, i+1, 1)
            if (3*i) <= self.vertices:
                self.add_edge(i, 3*i, 1)

    def add_edge(self, u, v, weight):
        self.graph[u].append([v, weight])

    def _minDistance(self, visited, dist):
        idx, minn = -1, sys.maxsize
        for i in range(1, self.vertices+1):
            if visited[i] is False and dist[i] < minn:
                minn = dist[i]
                idx = i

        return idx

    def dijkstra(self, src):
        visited = [False]*(self.vertices + 1)
        dist = [sys.maxsize]*(self.vertices + 1)
        dist[1] = 0

        for i in range(1, self.vertices+1):
            vertex = self._minDistance(visited, dist)
            visited[vertex] = True

            for adj in self.graph[vertex]:
                adj_v = adj[0]
                adj_w = adj[1]
                if visited[adj_v] is False:
                    dist[adj_v] = min(dist[adj_v], dist[vertex] + adj_w)    # edge weight is 1
        return dist


for _ in range(int(input())):
    n = int(input())
    graph = Graph(n)

    # result array contains distance of all vertices from 1 (single source)
    result = graph.dijkstra(1)
    print(result[n])
