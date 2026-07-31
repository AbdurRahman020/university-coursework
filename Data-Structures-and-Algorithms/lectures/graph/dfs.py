"""
Depth-First Search (DFS) Algorithm

Reference:
    Dasgupta, S., Papadimitriou, C., & Vazirani, U. (2006).
    Algorithms. McGraw-Hill Education.
    Chapter 3: Decompositions of Graphs — Section 3.2: DFS in Directed Graphs

The algorithm maintains a global clock and records pre/post visit times
for each node, which are essential for topological sort, SCC detection,
and cycle detection.
"""


def dfs(graph):
    visited = set()
    pre = {}
    post = {}
    clock = [0]  # mutable list used as a counter (avoids nonlocal)

    def explore(u):
        visited.add(u)          # mark node as visited
        clock[0] += 1           # tick clock on entry
        pre[u] = clock[0]       # record pre-visit time

        for v in graph[u]:      # visit each neighbor
            if v not in visited:
                explore(v)      # recurse only on unvisited neighbors

        clock[0] += 1           # tick clock on exit
        post[u] = clock[0]      # record post-visit time

    for u in graph:             # outer loop handles disconnected graphs
        if u not in visited:
            explore(u)

    return pre, post


def get_path(prev, target):
    """Reconstruct shortest path to target."""
    path = []

    while target is not None:
        path.append(target)
        target = prev[target]

    return path[::-1]
