def mat_to_list(adj_mat):
    """ Convert adjacency matrix to an adjacency list representation

    Parameters:
    -----------
    adj_mat : (a square 0-1 matrix)
        Adjacency matrix (n x n) of the graph (of n nodes)


    Returns:
    --------
     adj_list: `list[list[int]]`
        The adjacency list of the graph

    """
    # TODO

    adj_list = []

    dimension = len(adj_mat)

    for i in range(dimension):
        adj_list.append([])
        for j in range(dimension):
            if adj_mat[i][j] == 1:
                adj_list[i].append(j)

    return adj_list