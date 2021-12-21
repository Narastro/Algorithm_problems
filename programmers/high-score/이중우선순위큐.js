/* 2021.12.21. 프로그래머스 고득점 Kit - 힙(heap)
 * 이중 우선순위 큐
 */

class Node {
  constructor(value) {
    this.value = value;
  }
}

class Heap {
  constructor() {
    this.heap = [];
  }

  push(value) {
    const node = new Node(value);
    this.heap.push(node);
    this.heapifyUp();
  }

  pop() {
    const count = this.heap.length;
    const rootNode = this.heap[0];

    if (count <= 0) return undefined;
    if (count === 1) this.heap = [];
    else {
      this.heap[0] = this.heap.pop();
      this.heapifyDown();
    }
    return rootNode;
  }

  heapifyUp() {
    let index = this.heap.length - 1;
    const lastInsertedNode = this.heap[index];

    while (index > 0) {
      const parentIndex = this.getParentIndex(index);
      if (this.heap[parentIndex].value > lastInsertedNode.value) {
        this.heap[index] = this.heap[parentIndex];
        index = parentIndex;
      } else break;
    }

    this.heap[index] = lastInsertedNode;
  }

  heapifyDown() {
    let index = 0;
    const count = this.heap.length;
    const rootNode = this.heap[index];

    while (this.getLeftChildIndex(index) < count) {
      const leftChildIndex = this.getLeftChildIndex(index);
      const rightChildIndex = this.getRightChildIndex(index);
      const smallerChildIndex =
        rightChildIndex < count &&
        this.heap[rightChildIndex].value < this.heap[leftChildIndex].value
          ? rightChildIndex
          : leftChildIndex;

      if (this.heap[smallerChildIndex].value <= rootNode.value) {
        this.heap[index] = this.heap[smallerChildIndex];
        index = smallerChildIndex;
      } else break;
    }

    this.heap[index] = rootNode;
  }

  getLeftChildIndex(parentIndex) {
    return parentIndex * 2 + 1;
  }
  getRightChildIndex(parentIndex) {
    return parentIndex * 2 + 2;
  }
  getParentIndex(childIndex) {
    return Math.floor((childIndex - 1) / 2);
  }

  peek() {
    return this.heap[0];
  }
}

class PriorityQueue extends Heap {
  constructor() {
    super();
  }

  isEmpty() {
    return this.heap.length <= 0;
  }
}

const solution = (operations) => {
  const minHeap = new PriorityQueue();
  const maxHeap = new PriorityQueue();
  let heapLength = 0;
  operations.forEach((oper) => {
    const command = oper.split(" ")[0];
    const number = Number(oper.split(" ")[1]);
    if (command === "I") {
      minHeap.push(number);
      maxHeap.push(-number);
      heapLength += 1;
    } else if (heapLength !== 0) {
      heapLength -= 1;
      if (number === 1) {
        console.log(maxHeap.peek());
        maxHeap.pop();
      } else {
        console.log(minHeap.peek());
        minHeap.pop();
      }
    }
    if (heapLength === 0) {
      minHeap.heap = [];
      maxHeap.heap = [];
    }
  });
  if (heapLength === 0) {
    return [0, 0];
  } else {
    return [-maxHeap.peek().value, minHeap.peek().value];
  }
};

console.log(
  solution([
    "I 4",
    "I 3",
    "I 2",
    "I 1",
    "D 1",
    "D 1",
    "D -1",
    "D -1",
    "I 5",
    "I 6",
  ])
);
