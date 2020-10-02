class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        # self.graph = defaultdict(lambda: [])
        self.graph = []

    def add_edge(self, src, dest, weight):
        self.graph.append([src, dest, weight])

    def initialise(self, arr, size):
        for i in range(self.vertices):
            arr[i] = i
            size[i] = 1

    def find(self, i, arr):
        while i != arr[i]:
            arr[i] = arr[arr[i]]
            i = arr[i]

        return i

    def union(self, x, y, arr, size):
        if size[x] < size[y]:
            arr[x] = arr[y]
            size[y] += size[x]
        else:
            arr[y] = arr[x]
            size[x] += size[y]

    def kruskal(self):
        # graph = sorted(self.graph.items, key=lambda kv: (kv[1][1], kv[0]))
        self.graph = sorted(self.graph, key=lambda i: i[2])

        arr = [0]*(self.vertices+1)
        size = [0]*(self.vertices+1)
        self.initialise(arr, size)

        edges = 0
        i = 0
        result = []

        while edges < self.vertices - 1:
            s, d, w = self.graph[i]
            i += 1
            x = self.find(s, arr)
            y = self.find(d, arr)

            if x != y:
                edges += 1
                result.append([s, d, w])
                self.union(x, y, arr, size)

        return result


for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = Graph(v)
    Gedges = [int(i) for i in input().split()]
    i = 0

    while i < 3*e:
        s, d, w = Gedges[i], Gedges[i+1], Gedges[i+2]
        graph.add_edge(s, d, w)
        i+=3

    print(graph.kruskal())
