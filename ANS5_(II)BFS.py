#ANS5(II) - Submitted by Tatwamasi Mishra, UCSE20040

#this program implements BFS traversal method in a graph

import collections

#this piece of code implements BFS in a graph
def bfs(graph, source):

    visited = set()
    queue = collections.deque([source])
    visited.add(source)

    while queue:

        #Dequeueing a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        #If not visited, we mark it as visited
        #and add to queue
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

#driver code
if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2, 3], 2: [1], 3: [5], 4: [0, 5], 5: [4]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)