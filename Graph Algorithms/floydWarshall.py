import sys

def floydWarshall(dist, v):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dist[i][k] != sys.maxsize and dist[k][j] != sys.maxsize:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    printSol(dist, v)


def printSol(dist, v):
    for i in range(v):
        for j in range(v):
            if dist[i][j] == sys.maxsize:
                print("INF", end=' ')
            else:
                print(dist[i][j], end=' ')
        print()


for _ in range(int(input())):
    v = int(input())
    graph = [[]*v for i in range(v)]
    dist = [[]*v for i in range(v)]
    
    for i in range(v):
        for inp in input().split():
            if inp == 'INF':
                graph[i].append(sys.maxsize)
            else:
                graph[i].append(int(inp))
        dist[i] = graph[i][:]
    
    floydWarshall(dist, v)
