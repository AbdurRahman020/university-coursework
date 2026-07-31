from bfs import bfs

# %% test cases


def test_bfs_basic():
    """Test BFS on a simple directed graph"""
    print("TEST BFS: Basic Graph")

    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }

    dist = bfs(graph, 'A')
    print(f"Distances from A: {dist}")

    assert dist['A'] == 0
    assert dist['B'] == 1
    assert dist['C'] == 1
    assert dist['D'] == 2

    print("All assertions passed!\n")


def test_bfs_single_node():
    """Test BFS on a single-node graph"""
    print("TEST BFS: Single Node")

    graph = {'A': []}

    dist = bfs(graph, 'A')
    print(f"Distances from A: {dist}")

    assert dist == {'A': 0}

    print("All assertions passed!\n")


def test_bfs_linear_chain():
    """Test BFS on a linear chain"""
    print("TEST BFS: Linear Chain")

    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['D'],
        'D': []
    }

    dist = bfs(graph, 'A')
    print(f"Distances from A: {dist}")

    assert dist['A'] == 0
    assert dist['B'] == 1
    assert dist['C'] == 2
    assert dist['D'] == 3

    print("All assertions passed!\n")


def test_bfs_unreachable_nodes():
    """Test BFS where some nodes are unreachable from source"""
    print("TEST BFS: Unreachable Nodes")

    graph = {
        'A': ['B'],
        'B': [],
        'C': ['D'],   # C and D are unreachable from A
        'D': []
    }

    dist = bfs(graph, 'A')
    print(f"Distances from A: {dist}")

    assert dist['A'] == 0
    assert dist['B'] == 1
    # C and D should not appear in dist since they're unreachable
    assert 'C' not in dist
    assert 'D' not in dist

    print("All assertions passed!\n")


def test_bfs_shortest_path_over_longer():
    """Test that BFS finds the shortest path, not just any path"""

    print("TEST BFS: Shortest Path Selection")

    # two paths from A to D: A->B->D (length 2) and A->C->D (length 2)
    # and a longer path A->B->C->D (length 3) — BFS must give distance 2
    graph = {
        'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D'],
        'D': []
    }

    dist = bfs(graph, 'A')
    print(f"Distances from A: {dist}")

    assert dist['A'] == 0
    assert dist['B'] == 1
    assert dist['C'] == 1   # via A->C directly, not A->B->C
    assert dist['D'] == 2   # via A->B->D or A->C->D

    print("All assertions passed!\n")


def test_bfs_star_graph():
    """Test BFS on a star graph (one hub connected to all leaves)"""
    print("TEST BFS: Star Graph")

    graph = {
        'hub': ['a', 'b', 'c', 'd'],
        'a': [],
        'b': [],
        'c': [],
        'd': []
    }

    dist = bfs(graph, 'hub')
    print(f"Distances from hub: {dist}")

    assert dist['hub'] == 0

    for leaf in ['a', 'b', 'c', 'd']:
        assert dist[leaf] == 1, f"Distance to {leaf} should be 1"

    print("All assertions passed!\n")


def run_all_tests():
    print("RUNNING ALL TESTS\n")

    test_bfs_basic()
    test_bfs_single_node()
    test_bfs_linear_chain()
    test_bfs_unreachable_nodes()
    test_bfs_shortest_path_over_longer()
    test_bfs_star_graph()

    print("ALL TESTS COMPLETED!")


if __name__ == "__main__":
    run_all_tests()
