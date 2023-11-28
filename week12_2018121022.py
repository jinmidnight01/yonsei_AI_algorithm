# Name: Jinhyo Park
# Student ID: 2018121022
# Assignment: Week 12

class WeightedGraph:
  def __init__(self, n):
    self.adj = [[] for _ in range(n)]
    self.n = n

  def add_edge(self, u, v, w):
    self.adj[u].append((v, w))
    self.adj[v].append((u, w))

  def get_weight(self, u, v):
    for i in range(len(self.adj[u])):
      if self.adj[u][i][0] == v:
        return self.adj[u][i][1]
    return None

def find_smallest_weight(graph, S):
    min_weight = float("inf")
    min_edge = (-1, -1)

    for u in S:
        for v, w in enumerate(graph.adj):
            if v not in S:
                weight = graph.get_weight(u, v)
                if weight is not None and weight < min_weight:
                    min_weight = weight
                    min_edge = (u, v)
    return min_edge

first_line = input().split()
n = int(first_line[0])
m = int(first_line[1])
l = int(first_line[2])

g = WeightedGraph(n)
for i in range(m):
    line = input().split()
    u = int(line[0])
    v = int(line[1])
    w = int(line[2])
    g.add_edge(u, v, w)

s = []
for i in range(l):
    vertex = int(input())
    s.append(vertex)

v1, v2 = find_smallest_weight(g, s)
print(v1)
print(v2)
