# Name: Jinhyo Park
# Student ID: 2018121022
# Assignment: Week 11

class Node:
  def __init__(self, v: int):
    self.v = v
    self.next = None

class Graph:
  def __init__(self, n: int):
    self.n = n
    self.adjlist = [None for _ in range(n)]

  def addEdge(self, u: int, v: int):
    e = Node(v)
    e.next = self.adjlist[u]
    self.adjlist[u] = e

    e = Node(u)
    e.next = self.adjlist[v]
    self.adjlist[v] = e

  def dfs(self, v: int, visited: list):
    visited[v] = True
    current = self.adjlist[v]
    while current:
      if not visited[current.v]:
        self.dfs(current.v, visited)
      current = current.next

  def solve(self) -> int:
    visited = [False] * self.n
    connected_components = 0
    for i in range(self.n):
      if not visited[i]:
        connected_components += 1
        self.dfs(i, visited)
    return connected_components

n,m = map(int,input().split(' '))
graph = Graph(n)
for _ in range(m):
  u,v = map(int,input().split(' '))
  graph.addEdge(u,v)
print(graph.solve())