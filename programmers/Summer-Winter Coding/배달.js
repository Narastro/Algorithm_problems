/* 2021.12.20. Summer/Winter Coding(~2018)
 * 배달
 */

class Node {
  constructor(key, value) {
    this.node = key;
    this.value = value;
  }
}

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

const dijistra = (map, start, K) => {
  const heap = new PriorityQueue();
  const dist = new Map();
  let cnt = 0;
  heap.push(start.node, start.len);
  while (!heap.isEmpty()) {
    const v = heap.pop();
    if (!dist.has(v.node) && v.value <= K) {
      cnt += 1;
      dist.set(v.node, v.value);
      if (map.has(v.node))
        map.get(v.node).forEach(({ node, len }) => {
          heap.push(node, v.value + len);
        });
    }
  }
  return cnt;
};

const solution = (N, road, K) => {
  const map = new Map();
  road.forEach(([from, to, len]) => {
    const node1 = { node: from, len };
    const node2 = { node: to, len };
    map.set(from, map.has(from) ? [...map.get(from), node2] : [node2]);
    map.set(to, map.has(to) ? [...map.get(to), node1] : [node1]);
  });
  return dijistra(map, { node: 1, len: 0 }, K);
};

console.log(
  solution(
    5,
    [
      [1, 2, 1],
      [2, 3, 3],
      [5, 2, 2],
      [1, 4, 2],
      [5, 3, 1],
      [5, 4, 2],
    ],
    3
  )
);
