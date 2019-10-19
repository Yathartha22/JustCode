from collections import defaultdict, deque

class Graph:
    """
    Graph object.

    This object serves to either explore the nodes of a graph
    or to calculate the distance between different paths

    """

    def __init__(self):
        # initialize graph as a dictionary
        self.graph = defaultdict(list)
    
    def add_edge(self, source, edge):
        # add edges to a source in the graph
        self.graph[source].append(edge)


    def bfs(self, source):
        # initialize the visited nodes to False
        # and the queue where we will put nodes related to the source
        visited = [False] * (len(self.graph))
        queue = []

        # start by queueing the source
        queue.append(source)

        # mark that node as visited
        visited[source] = True

        # as long as we have nodes that we haven't covered, let's search
        while queue:
            # we remove the source from the queue as we're about to explore it
            source = queue.pop(0)
            print (source) 

            # loop through neighbors to visit them
            for i in self.graph[source]:
                # if node is not visited,we append it to the queue to explore 
                # its neighbors and mark it as visited
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def bfs_with_distance(self, source):
        # we start by initializing our queue
        queue = deque([source])
        # we initialize the level dict that will contain the distance
        level = {source: 0}
        # we also log the parent of each node 
        # (we replaced the visited dict with parent and level)
        parent = {source: None}
        i = 1
        while queue:
            v = queue.popleft()
            for n in self.graph[v]:
                if n not in level:            
                    queue.append(n)
                    level[n] = i
                    parent[n] = v
            i += 1
        return level, parent



if __name__ == '__main__':
    g = Graph()

    g.add_edge(0, 1) 
    g.add_edge(0, 2) 
    g.add_edge(1, 2) 
    g.add_edge(2, 0) 
    g.add_edge(2, 3) 
    g.add_edge(3, 3)

    print(g.bfs_with_distance(2))