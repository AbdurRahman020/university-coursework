from dijkstra import *

# %% TEST test_case


def test_dijkstra_basic():
    """Test Dijkstra on the standard example"""

    print("Basic Graph")

    graph = {
        'A': [('B', 4), ('C', 1)],
        'B': [('D', 1)],
        'C': [('B', 2), ('D', 5)],
        'D': []
    }

    dist, prev = dijkstra(graph, 'A')

    print(f"Shortest distances from A: {dist}")
    print(f"Shortest path to D: {get_path(prev, 'D')}")

    assert dist['A'] == 0
    assert dist['B'] == 3   # A->C->B = 1+2
    assert dist['C'] == 1   # A->C
    assert dist['D'] == 4   # A->C->B->D = 1+2+1
    assert get_path(prev, 'D') == ['A', 'C', 'B', 'D']

    print("All assertions passed!\n")


def test_dijkstra_single_node():
    """Test Dijkstra on a single-node graph"""
    print("Single Node")

    graph = {'A': []}
    dist, prev = dijkstra(graph, 'A')

    print(f"Shortest distances from A: {dist}")

    assert dist == {'A': 0}
    assert get_path(prev, 'A') == ['A']

    print("All assertions passed!\n")


def test_dijkstra_linear_chain():
    """Test Dijkstra on a weighted linear chain"""

    print("Linear Chain")

    graph = {
        'A': [('B', 3)],
        'B': [('C', 5)],
        'C': [('D', 2)],
        'D': []
    }
    dist, prev = dijkstra(graph, 'A')

    print(f"Shortest distances from A: {dist}")
    print(f"Shortest path to D: {get_path(prev, 'D')}")

    assert dist['A'] == 0
    assert dist['B'] == 3
    assert dist['C'] == 8
    assert dist['D'] == 10
    assert get_path(prev, 'D') == ['A', 'B', 'C', 'D']

    print("All assertions passed!\n")


def test_dijkstra_chooses_cheaper_path():
    """Test that Dijkstra picks the cheaper path even if it has more hops"""
    print("Cheaper Path Over Fewer Hops")

    # Direct path A->D costs 10; indirect A->B->C->D costs 1+1+1=3
    graph = {
        'A': [('B', 1), ('D', 10)],
        'B': [('C', 1)],
        'C': [('D', 1)],
        'D': []
    }

    dist, prev = dijkstra(graph, 'A')

    print(f"Shortest distances from A: {dist}")
    print(f"Shortest path to D: {get_path(prev, 'D')}")

    assert dist['D'] == 3
    assert get_path(prev, 'D') == ['A', 'B', 'C', 'D']

    print("All assertions passed!\n")


def test_dijkstra_unreachable_node():
    """Test Dijkstra when some nodes are unreachable"""
    print("Unreachable Node")

    graph = {
        'A': [('B', 2)],
        'B': [],
        'C': []   # C is unreachable from A
    }

    dist, prev = dijkstra(graph, 'A')

    print(f"Shortest distances from A: {dist}")

    assert dist['A'] == 0
    assert dist['B'] == 2
    assert dist['C'] == float('inf')

    print("All assertions passed!\n")


def test_dijkstra_equal_weight_paths():
    """Test Dijkstra when multiple paths have equal total weight"""
    print("Equal Weight Paths")

    # A->B->D = 2+3 = 5 and A->C->D = 1+4 = 5 — both cost 5
    graph = {
        'A': [('B', 2), ('C', 1)],
        'B': [('D', 3)],
        'C': [('D', 4)],
        'D': []
    }

    dist, prev = dijkstra(graph, 'A')

    print(f"Shortest distances from A: {dist}")
    print(f"Shortest path to D: {get_path(prev, 'D')}")

    assert dist['D'] == 5
    path = get_path(prev, 'D')
    # either valid path is acceptable
    assert path in [['A', 'B', 'D'], ['A', 'C', 'D']]

    print("All assertions passed!\n")


def run_all_tests():
    print("RUNNING ALL DTESTS")

    test_dijkstra_basic()
    test_dijkstra_single_node()
    test_dijkstra_linear_chain()
    test_dijkstra_chooses_cheaper_path()
    test_dijkstra_unreachable_node()
    test_dijkstra_equal_weight_paths()

    print("ALL TESTS COMPLETED!")


if __name__ == "__main__":
    run_all_tests()
