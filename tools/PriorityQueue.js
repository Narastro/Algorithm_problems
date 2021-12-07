class PriorityQueue {
  constructor(comp) {
    this.heap = [];
    this.comp = comp;
    if (comp == undefined) {
      this.comp = (a, b) => {
        return a - b;
      };
    }
  }

  pop() {
    if (this.isEmpty()) {
      return null;
    }
    let min = this.heap[0];
    let last = this.heap.pop();
    if (this.size() != 0) {
      this.heap[0] = last;
      this.downHeap(0);
    }
    return min;
  }

  size() {
    return this.heap.length;
  }

  insert(value) {
    this.heap.push(value);
    this.upHeap(this.size() - 1);
  }

  downHeap(pos) {
    while (this.isInternal(pos)) {
      let s = null;

      //왼쪽과 오른쪽 자식중에 작은 것을 s에 넣는다.
      if (!this.hasRight(pos)) {
        s = this.left(pos);
      } else if (
        this.comp(this.heap[this.left(pos)], this.heap[this.right(pos)]) <= 0
      ) {
        s = this.left(pos);
      } else {
        s = this.right(pos);
      }
      if (this.comp(this.heap[s], this.heap[pos]) < 0) {
        this.swap(pos, s);
        pos = s;
      } else {
        break;
      }
    }
  }
  upHeap(pos) {
    while (!this.isRoot(pos)) {
      let p = this.parent(pos);
      if (this.comp(this.heap[p], this.heap[pos]) <= 0) {
        break;
      }
      this.swap(p, pos);
      pos = p;
    }
  }
  swap(x, y) {
    let tmp = this.heap[x];
    this.heap[x] = this.heap[y];
    this.heap[y] = tmp;
  }
  parent(pos) {
    return parseInt((pos - 1) / 2);
  }
  left(pos) {
    return 2 * pos + 1;
  }
  right(pos) {
    return 2 * pos + 2;
  }

  isInternal(pos) {
    return this.hasLeft(pos);
  }
  isRoot(pos) {
    if (pos == 0) return true;
    return false;
  }
  hasLeft(pos) {
    if (this.left(pos) < this.size()) {
      return true;
    }
    return false;
  }
  hasRight(pos) {
    if (this.right(pos) < this.size()) {
      return true;
    }
    return false;
  }
  isEmpty() {
    return this.heap.length == 0;
  }

  min() {
    return this.heap[0];
  }
}

module.exports = PriorityQueue;
