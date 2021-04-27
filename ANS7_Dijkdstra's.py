#ANS7 - Submitted by Tatwamasi Mishra, UCSE20040

#this program implements Dijkstra's shortest path algorithm
#with the help of the adjacency matrix of the graph
#to find and display the shortest paths from the source node to
#all other nodes

import sys
 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex distance from source node to")
        for node in range(self.V):
            print(node, ": ", dist[node])
 
    #function to find vertex with minimum distance value from unadded vertices
    def minDistance(self, dist, sptSet):
 
        #intializing min distance for next node
        min = sys.maxsize
 
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 
    #function to implement dijkstra's algorithm
    def dijkstra(self, src):
 
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            #u = min distance vertex from vertices not yet visited
            #sptSet = shortest path tree set
            u = self.minDistance(dist, sptSet)
 
            #putting the shortest distance vertext in the tree set
            sptSet[u] = True
 
            #updating distance values of adjacent vertices if
            #current distance is greater than new distance
            #&& the adjacent vertex is not in sptSet
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]) :
                    dist[v] = dist[u] + self.graph[u][v]
 
        self.printSolution(dist)
 
 
#driver code
g = Graph(9)
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
print("Nodes in the graph are: ")
for node in range(9) :
  print(node, end = " ")
src = int(input("\nEnter source node: ")) 
g.dijkstra(src)