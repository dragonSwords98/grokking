"""
Dijkstra's algorithm used for non-negative, acyclical graphs for determining shortest path from start to any node 

Dijkstras is similar to BFS, however also checks paths between neighboring nodes that reduces costs if a shorter path is found.
"""


# TODO: the class struct is wrong, so the code is a bit off from answer

import math

# class Graph:
  
#     def __init__(self, vertices):
#         self.V = vertices  # No. of vertices
#         self.graph = []
  
#     # function to add an edge to graph
#     def addEdge(self, u, v, w):
#         self.graph.append([u, v, w])

class Vertex:
  def __init__(self, value: str, edges: list[Edge]) -> None:
    self.value = value
    self.edges = edges

class Edge:
  def __init__(self, origin, destination: Vertex, cost: int) -> None:
    self.destination = destination
    self.cost = cost

def pickVertexWithMinDistance(graph: list[Vertex], costs: dict) -> Vertex:
  # find vertex with lowest distance not included in visited yet
  sortedCosts = dict(sorted(costs.items(), key=lambda item: item[1]))
  for key in sortedCosts.keys():
    if key in graph:
      return key
  return None

def dijkstras(graph: list[Vertex], start: int) -> dict:
  costs = dict.fromkeys(map(lambda x: x.value, graph), math.inf)
  current = graph[start]
  costs[current.value] = 0

  # all vertices in graph will be visited
  while len(graph) > 0:
    
    # unvisited vertex has been visited
    graph.pop(graph.index(current))

    # explore all edges of this vertex
    for vertex in current.edges:
      # found a shorter path from source to the vertex at this vertex
      if costs[current.value] + vertex.cost < costs[vertex.destination]:
        costs[vertex.destination] = costs[current.value] + vertex.cost
    
    # visit the next unvisited vertex with smallest distance
    current = pickVertexWithMinDistance(graph, costs)
    if not current:
      return costs

  return costs


# To recap, Dijkstra’s algorithm has four steps:
# 1. Find the cheapest vertex. This is the vertex you can get to in the least
# amount of time.
# 2. Check whether there’s a cheaper path to the neighbors of this vertex.
# If so, update their costs.
# 3. Repeat until you’ve done this for every vertex in the graph.
# 4. Calculate the final path. (Coming up in the next section!)


# O( |E| + |V| log |V| )
# because all edges are visited, plus all vertices can be visited and may be revisited again at log rate