// 힙의 특징 : 부모가 항상 자식보다 작거나 같은 트리 기반의 자료 구조
class Node {
  constructor(key, value) {
    this.node = key;
    this.value = value;
  }
}

//주의!! 갖다 쓸 때 key가 필요한지 구별해야됨!

class Heap {
  constructor() {
    this.heap = [];
  }

  push(key, value) {
    const node = new Node(key, value);
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

module.exports = PriorityQueue;
