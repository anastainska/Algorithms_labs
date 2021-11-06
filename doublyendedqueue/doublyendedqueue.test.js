// import DoublyEndedQueue from './doublyendedqueue'

const doublyendedqueue = require('./doublyendedqueue');

describe("DoublyEndedQueue", () => {

    

    test('pushes back a number', () => {
        expect(doublyendedqueue.push_back(30)).toBe(30);
    });

    test('pushes front a number', () => {
        expect(doublyendedqueue.push_front(30)).toBe(30);
    });

    test('popped last number', () => {
        expect(doublyendedqueue.pop_back(30)).toEqual({"next": null, "prev": null, "value": 30});
    });

    test('popped first number', () => {
        expect(doublyendedqueue.pop_front(30)).toEqual({"next": null, "prev": null, "value": 30});
    });
});