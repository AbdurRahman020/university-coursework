"""
Breadth-First Search (BFS) Algorithm

Reference:
    Dasgupta, S., Papadimitriou, C., & Vazirani, U. (2006).
    Algorithms. McGraw-Hill Education.
    Chapter 4: Paths in Graphs — Section 4.1: Distances

The algorithm explores the graph layer by layer using a FIFO queue,
guaranteeing that each node is reached via the shortest path (fewest edges)
from the source. The dist dictionary stores the hop-count distance from
the source to every reachable node.
"""

from collections import deque


def bfs(graph, source):
    # distance to source is 0; also marks it visited
    dist = {source: 0}
    # FIFO queue — start with the source node
    queue = deque([source])

    while queue:
        # dequeue the next node to process
        u = queue.popleft()

        # examine each neighbor of u
        for v in graph[u]:
            # visit only unvisited neighbors
            if v not in dist:
                # neighbor is one hop further
                dist[v] = dist[u] + 1
                # enqueue for later processing
                queue.append(v)

    # dist[v] = shortest hop-count from source to v
    return dist
