from dfs import dfs

# %% test cases


def test_dfs_basic():
    """Test DFS on a simple directed graph"""
    print("Basic Graph")

    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }

    pre, post = dfs(graph)

    print(f"Pre-visit times:  {pre}")
    print(f"Post-visit times: {post}")

    # all nodes must be visited
    assert set(pre.keys()) == {'A', 'B', 'C', 'D'}
    assert set(post.keys()) == {'A', 'B', 'C', 'D'}
    # pre times must all be unique
    assert len(set(pre.values())) == 4
    # post times must all be unique
    assert len(set(post.values())) == 4
    # pre[u] < post[u] for every node

    for u in graph:
        assert pre[u] < post[u], f"pre[{u}] should be < post[{u}]"

    print("All assertions passed!\n")


def test_dfs_single_node():
    """Test DFS on a graph with a single node"""
    print("Single Node")

    graph = {'A': []}
    pre, post = dfs(graph)

    print(f"Pre-visit times:  {pre}")
    print(f"Post-visit times: {post}")

    assert pre == {'A': 1}
    assert post == {'A': 2}

    print("All assertions passed!\n")


def test_dfs_disconnected_graph():
    """Test DFS on a disconnected graph (two components)"""
    print("Disconnected Graph")

    graph = {
        'A': ['B'],
        'B': [],
        'C': ['D'],
        'D': []
    }

    pre, post = dfs(graph)
    print(f"Pre-visit times:  {pre}")
    print(f"Post-visit times: {post}")
    # all 4 nodes must be visited despite disconnection

    assert set(pre.keys()) == {'A', 'B', 'C', 'D'}
    assert set(post.keys()) == {'A', 'B', 'C', 'D'}

    for u in graph:
        assert pre[u] < post[u]
    print("All assertions passed!\n")


def test_dfs_linear_chain():
    """Test DFS on a linear chain A -> B -> C -> D"""
    print("Linear Chain")

    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['D'],
        'D': []
    }

    pre, post = dfs(graph)
    print(f"Pre-visit times:  {pre}")
    print(f"Post-visit times: {post}")
    # in a chain, A is entered first so has the smallest pre time
    assert pre['A'] < pre['B'] < pre['C'] < pre['D']
    # and D finishes first (deepest node)
    assert post['D'] < post['C'] < post['B'] < post['A']
    print("All assertions passed!\n")


def test_dfs_pre_post_ordering():
    """Test that pre/post times form valid parenthesization"""
    print("Pre/Post Parenthesization Property")

    graph = {
        1: [2, 3],
        2: [4],
        3: [],
        4: []
    }

    pre, post = dfs(graph)

    print(f"Pre-visit times:  {pre}")
    print(f"Post-visit times: {post}")
    # node 2 is a descendant of 1: intervals must be nested

    assert pre[1] < pre[2] and post[2] < post[1]
    # node 4 is a descendant of 2: intervals must be nested
    assert pre[2] < pre[4] and post[4] < post[2]
    # all clock values are unique (2*n values total)
    all_times = list(pre.values()) + list(post.values())
    assert len(set(all_times)) == len(all_times)

    print("All assertions passed!\n")


def test_dfs_clock_values():
    """Test that clock values run from 1 to 2n"""
    print("Clock Values Range")

    graph = {
        'X': ['Y', 'Z'],
        'Y': [],
        'Z': []
    }

    pre, post = dfs(graph)

    print(f"Pre-visit times:  {pre}")
    print(f"Post-visit times: {post}")

    n = len(graph)
    all_times = sorted(list(pre.values()) + list(post.values()))
    # clock should produce values 1 through 2n with no gaps
    assert all_times == list(range(1, 2 * n + 1))
    print("All assertions passed!\n")


def run_all_tests():
    print("RUNNING ALL TESTS\n")

    test_dfs_basic()
    test_dfs_single_node()
    test_dfs_disconnected_graph()
    test_dfs_linear_chain()
    test_dfs_pre_post_ordering()
    test_dfs_clock_values()

    print("ALL TESTS COMPLETED!")


if __name__ == "__main__":
    run_all_tests()
