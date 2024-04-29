from q1 import mat_to_list
from q2 import reachable


def main():
    adj_mat =  [[0, 1, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0]]
    
    print("Expected output: [[1, 3], [2], [0], [4], [3], []]")
    print(mat_to_list(adj_mat))
    
    print()
    print()


    
    empty_mat = []
    print("Expected output: []")
    print(mat_to_list(empty_mat))
    print()
    print()

    single_node_mat = [[0]]
    print("Expected output: [[]]")
    print(mat_to_list(single_node_mat))
    print()
    print()

    fully_connected_mat = [[0, 1, 1],
                           [1, 0, 1],
                           [1, 1, 0]]
    print("Expected output: [[1, 2], [0, 2], [0, 1]]")
    print(mat_to_list(fully_connected_mat))
    print()
    print()

    disconnected_mat = [[0, 1, 0],
                        [1, 0, 0],
                        [0, 0, 0]]
    print("Expected output: [[1], [0], []]")
    print(mat_to_list(disconnected_mat))
    print()
    print()





    adj_list = [[1, 3], [2], [0], [4], [3], []]
    print("Expected output: {0, 1, 2, 3, 4}")
    print(reachable(adj_list, 0))
    print()
    print()


    print("Expected output: {3, 4}")
    print(reachable(adj_list, 3))
    print()
    print()


if __name__ == "__main__":
    main()