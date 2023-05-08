

"""

# Contributed by: Bryan Ling
# Original code is from online sources

How is dijkstras different from bellman-ford. BF takes a more 'depth first search' type approach, going through all edges and its vertices for |V| - 1 times at most to determine if the vertices are improving in cost
with each iteration. Because it does not optimize the edges as they're visited right away, rather we move on until we hit all vertices, repeating again and again, it is more DFS like

However, the key takeaway is BF is able to handle negative weights in addition to what dijkstras can do.

"""

import math


class Graph:
  
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []
  
    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])


    def bellmanFord(self, start: int) -> dict:
        costs = dict.fromkeys(map(lambda x: x.value, self.graph), math.inf)
        current = self.graph[start]
        costs[current.value] = 0

        vertices_count = list(map(lambda *x: sum(x), *self.graph.values()))

        while vertices_count > 0:

            


            vertices_count = vertices_count - 1



# time : O ( |V| + |E| )




# Floyd-Warshall is a nested k,j,i 2-D array cost check to find all shortest path from all nodes to all nodes, which is O(|V|^3) of course, since its a check between itself in 3 nested loops of V length