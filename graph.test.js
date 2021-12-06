const obj = require('./weightedgraph.js');
// import { bellmanFord } from './weightedgraph.js';

describe("WeightedGraph", () => {

    test('test :))', () => {
        graphTest = {
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
        result = obj.bellmanFord(graphTest.vertices, graphTest.edges, "A")
        expect(result).toStrictEqual({"distance": {"A": 0, "B": -20, "C": -17, "D": -18, "E": -16}, "predecessor": {"A": null, "B": "A", "C": "B", "D": "B", "E": "B"}});
    });
});