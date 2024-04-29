def reachable(adj_list, start_node):
    """ Compute the nodes reachable from a start node

    For the above example, reachable([[1, 3], [2], [0], [4], [3], []], 0)) must return {0, 1, 2, 3, 4}
    and reachable([[1, 3], [2], [0], [4], [3], []], 3) must return {3, 4}

    Parameters:
    -----------
    adj_list : the adjacency list of the graph
    start_node: the index of the start node

    Returns:
    --------
    reachable: set(int) the set of nodes reachable from start_node


    """
    # TODO
    if not adj_list or start_node < 0 or start_node >= len(adj_list):
        return set()
    
    stack = [start_node]
    reachables = set()


    while stack:
        node = stack.pop()
        if node not in reachables:
            reachables.add(node)
            stack.extend(adj_list[node])


    return reachables



