class WeightedGraph {
    constructor() {
        //pass
    }

    bellmanFord(vertices, edges, start_point) {
        let distance = {};
        let predecessor = {};

        vertices.map(vertex => {
            distance[vertex] = Infinity;
            predecessor[vertex] = null;
        });

        distance[start_point] = 0;
        let containsNegative = false;

        for (let i = 1; i < vertices.length; i++) {
            for (let { vertex1, vertex2, weight } of edges) {
                if (distance[vertex1] + weight < distance[vertex2]) {
                    distance[vertex2] = distance[vertex1] + weight;
                    predecessor[vertex2] = vertex1;
                }
                if ((weight < 0) && (!containsNegative)) {
                    console.log("Graph contains a negative-weight cycle");
                    containsNegative = true;
                }
            }
        }
        return { distance, predecessor };
    }
}

const graph = {
    vertices: ["A", "B", "C", "D", "E"],
    edges: [
        { vertex1: "A", vertex2: "B", weight: -20 },
        { vertex1: "B", vertex2: "D", weight: 2 },
        { vertex1: "A", vertex2: "C", weight: 2 },
        { vertex1: "B", vertex2: "C", weight: 3 },
        { vertex1: "C", vertex2: "D", weight: 1 },
        { vertex1: "B", vertex2: "E", weight: 4 },
        { vertex1: "C", vertex2: "D", weight: 3 },
        { vertex1: "E", vertex2: "D", weight: 3 },
        { vertex1: "C", vertex2: "E", weight: 5 },
    ]
};

obj = new WeightedGraph()
console.log(obj.bellmanFord(graph.vertices, graph.edges, "A"))

// console.log(bellmanFord(graph.vertices, graph.edges, "A"))

module.exports = obj;