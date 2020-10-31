def bfs(adj, n, color, index):
    # color = [0 for i in range(n+1)]
    q = [index]
    color[index] = 0
    # for i in range(0, n):
    while q:
        u = q.pop(0)
        for v in adj[u]:
            if color[v] == -1:
                # visited[v] = 1
                color[v] = 1-color[u]
                q.append(v)
            else:
                if color[v] == color[u]:
                # print(visited)
                    return 0
    # print(visited)
    return 1



for t in range(int(input())):
    n, m = map(int, input().split())
    adj = [[] for i in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    # print(adj)
    res = 1
    color = [-1 for i in range(n+1)]
    for i in range(1, n+1):
        if color[i] == -1:
            if bfs(adj, n, color, i) == 0:
                res = 0
                break
    print("Scenario #{}:".format(t+1))
    if res:
        print("No Suspicious bugs found!")
    else:
        print("Suspicious bugs found!")

