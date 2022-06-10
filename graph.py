class Graph:
    def __init__(self, vertices, adjacency_list):
        self.adjacency_list = adjacency_list
        self.graph = []
        self.vertices = vertices
        self.transform()

    def add_edge(self, start_vertex, end_vertex, edge_weight):
        self.graph.append([start_vertex, end_vertex, edge_weight])

    def transform(self):
        for start_vertex in self.adjacency_list:
            for end_vertex, edge_weight in self.adjacency_list[start_vertex]:
                self.add_edge(start_vertex, end_vertex, edge_weight)
        return self.graph

    def get_min(self, graph, result_graph):
        current_edge = graph[0]
        for v in result_graph:
            min_adjacent_edge = min(graph,
                                    key=lambda x: x[2] if (x[0] == v or x[1] == v) and
                                                          (x[0] not in result_graph or x[1] not in result_graph)
                                    else float('inf'))
            if current_edge[2] > min_adjacent_edge[2]:
                current_edge = min_adjacent_edge
        return current_edge

    def prims_algorithm(self):
        result_graph = {1}
        mst = []
        self.graph.insert(0, [-1, -1, float('inf')])

        while len(result_graph) < self.vertices:
            r = self.get_min(self.graph, result_graph)
            if r[2] == float('inf'):
                break
            mst.append(r)
            result_graph.add(r[0])
            result_graph.add(r[1])

        self.graph.pop(0)
        return mst
