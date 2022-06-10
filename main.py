from graph import Graph


if __name__ == '__main__':
    graph = {
        1: [[2, 13], [3, 18], [4, 17], [5, 14], [6, 22]],
        2: [[3, 26], [5, 19]],
        3: [[4, 30]],
        4: [[6, 22]]
    }
    g = Graph(6, graph)
    print(g.prims_algorithm())
