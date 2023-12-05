# Name: Jinhyo Park
# Student ID: 2018121022
# Assignment: Week 13

class WeightedDirectedGraph:
    def __init__(self, n):
        self.adj = [{} for _ in range(n)]
        self.n = n

    def add_edge(self, u, v, w):
        self.adj[u][v] = w

    def get_weight(self, u, v):
        return self.adj[u].get(v)

    def shortest_path_weight(self, start, end):
        if start == end:
            return 0
        
        distance = [float('inf')] * self.n
        distance[start] = 0
        prev = [-1] * self.n
        visited = [False] * self.n

        for _ in range(self.n - 1):
            u = self.min_distance(distance, visited)
            visited[u] = True

            for v in range(self.n):
                if not visited[v] and self.adj[u].get(v) is not None:
                    if distance[u] + self.adj[u][v] < distance[v]:
                        distance[v] = distance[u] + self.adj[u][v]
                        prev[v] = u

        path_weight = self.calculate_path_weight(prev, start, end)
        return path_weight if path_weight is not None else 'x'

    def min_distance(self, distance, visited):
        min_dist = float('inf')
        min_index = -1

        for v in range(self.n):
            if distance[v] < min_dist and not visited[v]:
                min_dist = distance[v]
                min_index = v

        return min_index

    def calculate_path_weight(self, prev, start, end):
        if prev[end] == -1:
            return None

        path_weight = 0
        at = end
        while at != -1:
            if prev[at] != -1:
                path_weight += self.adj[prev[at]][at]
            at = prev[at]

        return path_weight

first_line = input().split()
n = int(first_line[0])
m = int(first_line[1])

g = WeightedDirectedGraph(n)
for i in range(m):
    line = input().split()
    u = int(line[0])
    v = int(line[1])
    w = int(line[2])
    g.add_edge(u, v, w)

for i in range(n):
  for j in range(n):
    print(g.shortest_path_weight(i,j))