class Dijkstra:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)]
                      for _ in range(vertices)]

    def print_solution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    def min_distance(self, dist, sptSet):
        min_index = 0
        min = 1e7

        for v in range(self.V):
            if dist[v] < min and not sptSet[v]:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):

        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            u = self.min_distance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                        not sptSet[v] and
                        dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_solution(dist)


class Floyd:
    V = 4

    INF = 99999
    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0, 1],
             [INF, INF, INF, 0]
             ]

    def floydWarshall(self):
        dist = list(map(lambda i: list(map(lambda j: j, i)), self.graph))
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    dist[i][j] = min(dist[i][j],
                                     dist[i][k] + dist[k][j]
                                     )
        self.printSolution(dist)

    def printSolution(self, dist):
        print("Following matrix shows the shortest distances between every pair of vertices")
        for i in range(self.V):
            for j in range(self.V):
                if dist[i][j] == self.INF:
                    print("%7s" % "INF", end=" ")
                else:
                    print("%7d" % (dist[i][j]), end=' ')
                if j == self.V - 1:
                    print()


Floyd().floydWarshall()

g = Dijkstra(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0)
