"""
Dijkstra's Shortest Path Algorithm

Reference:
    Dasgupta, S., Papadimitriou, C., & Vazirani, U. (2006).
    Algorithms. McGraw-Hill Education.
    Chapter 4: Paths in Graphs — Section 4.4: Dijkstra's Algorithm

The algorithm greedily selects the unvisited node with the smallest
known distance, then relaxes all its outgoing edges. A min-heap (priority
queue) is used to efficiently retrieve the next closest node, giving an
overall time complexity of O((V + E) log V). Only works on graphs with
non-negative edge weights.
"""

import heapq


def dijkstra(graph, source):
    # graph: { u: [(v, weight), ...] }
    # initialise all distances to infinity
    dist = {u: float('inf') for u in graph}
    # distance from source to itself is 0
    dist[source] = 0
    # prev[u] stores the node before u on the shortest path
    prev = {u: None for u in graph}
    # min-heap seeded with (distance, source)
    pq = [(0, source)]

    while pq:
        # extract node with smallest tentative distance
        d, u = heapq.heappop(pq)

        # skip stale heap entries
        if d > dist[u]:
            continue

        # relax each outgoing edge (u -> v) with weight w
        for v, w in graph[u]:
            # found a shorter path to v through u
            if dist[u] + w < dist[v]:
                # update shortest known distance to v
                dist[v] = dist[u] + w
                # record u as the predecessor of v on best path
                prev[v] = u
                # push updated distance into heap
                heapq.heappush(pq, (dist[v], v))

    return dist, prev


def get_path(prev, target):
    """Reconstruct shortest path to target."""
    path = []

    while target is not None:
        path.append(target)
        target = prev[target]

    return path[::-1]
