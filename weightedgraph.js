const graph = {
    vertices: ["A", "B", "C", "D", "E"],
    edges: [
        { vertex1: "A", vertex2: "C", weight: -3 },
        { vertex1: "A", vertex2: "B", weight: 5 },
        { vertex1: "B", vertex2: "C", weight: 3 },
        { vertex1: "A", vertex2: "E", weight: -2 },
        { vertex1: "C", vertex2: "D", weight: -10 },
        { vertex1: "D", vertex2: "E", weight: 1 },
        { vertex1: "C", vertex2: "E", weight: 1 },
        { vertex1: "E", vertex2: "A", weight: 2 }
    ]
};

function bellmanFord(vertices, edges, start_point) {
    let distance = {};
    let predecessor = {};

    vertices.map(vertex2 => {
        distance[vertex2] = Infinity;
        predecessor[vertex2] = null;
    });

    distance[start_point] = 0;

    for (let i = 1; i < vertices.length; i++) {
        for (let { vertex1, vertex2, weight } of edges) {
            if (distance[vertex1] + weight < distance[vertex2]) {
                distance[vertex2] = distance[vertex1] + weight;
                predecessor[vertex2] = vertex1;
            }
        }
    }

    for (let { vertex1, vertex2, weight } of edges) {
        if (distance[vertex1] + weight < distance[vertex2]) {
            throw("Graph contains a negative-weight cycle");
        }
    }

    return { distance, predecessor };
}

console.log(bellmanFord(graph.vertices, graph.edges, "С"))