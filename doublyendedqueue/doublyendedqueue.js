class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}

class DoublyEndedQueue {
    constructor() {
        this.first = null;
        this.last = null;
        this.length = 0;
    }

    push_back(value) {
        var newNode = new Node(value);
        if (!this.first) {
            this.first = newNode;
            this.last = newNode;
        } else {
            this.last.next = newNode;
            newNode.prev = this.last;
            this.last = newNode;
        }
        this.length++;
        return this.last.value;
    }

    pop_back() {
        if (!this.first) return null;

        var poppedNode = this.last;
        if (this.length === 1) {
            this.first = null;
            this.last = null;
        } else {
            this.last = poppedNode.prev;
            this.last.next = null;
            poppedNode.prev = null;
        }
        this.length--;
        return poppedNode;
    }

    pop_front() {
        if (!this.first) return null;
        var shiftedNode = this.first;
        if (this.length === 1) {
            this.first = null;
            this.last = null;
        } else {
            this.first = shiftedNode.next;
            this.first.prev = null;
            shiftedNode.next = null;
        }
        this.length--;
        return shiftedNode;
    }
    push_front(value) {
        var newNode = new Node(value)
        if (!this.first) {
            this.first = newNode;
            this.last = newNode;
        } else {
            this.first.prev = newNode;
            newNode.next = this.first;
            this.first = newNode;
        }
        this.length++;
        return this.last.value;
    }
    get(index) {
        if (index < 0 || index >= this.length) return null;
        if (index <= this.length / 2) {
            console.log("WORKING FROM THE BEGINNING");
            var count = 0;
            var current = this.first;
            while (count !== index) {
                current = current.next;
                count++;
            }
        } else {
            console.log("WORKING FROM THE END");
            var count = this.length - 1;
            var current = this.last;
            while (count !== index) {
                current = current.prev;
                count--;
            }
        }
        return current;
    }

    // // set(index, value){
    // //     var foundNode = this.get(index);
    // //     if (foundNode != null) {
    // //         foundNode.value = value;
    // //         return true;
    // //     }
    // //     return false;
    // }
    // insert(index, value){
    //     if (index < 0 || index > this.length) return null;
    //     if (index === 0 ) return !!this.unshift(value);
    //     if (index === this.length) return !!this.push(value);
    //     var newNode = new Node(value);
    //     var prevNode = this.get(index-1);
    //     var nextNode = prevNode.next;
    //     prevNode.next = newNode;
    //     newNode.prev = prevNode;
    //     newNode.next = nextNode;
    //     nextNode.prev = newNode;
    //     this.length++;
    //     return true;
    // }
    // remove(index){
    //     if (index < 0 || index >= this.length) return null;
    //     if (index === 0) return this.shift();
    //     if (index === this.length) return this.pop();
    //     var removedNode = this.get(index);
    //     removedNode.prev.next = removedNode.next;
    //     removedNode.next.prev = removedNode.prev;
    //     removedNode.next = null;
    //     removedNode.prev = null;
    //     length--;
    //     return removedNode;
    // }
    
}

var obj = new DoublyEndedQueue()

console.log(obj.push_back(10))

module.exports = obj