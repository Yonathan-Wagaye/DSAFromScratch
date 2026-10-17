class Heap:
    def __init__(self):
        self.heap = [None]

    @classmethod
    def listToHeap(cls, values):
        heap = cls()
        heap.heap = heap.heap + list(values)
        heap._heapify()
        return heap

    def _percolateDown(self, nodeIndex):
        curr = nodeIndex
        n = len(self.heap) - 1

        while curr < n:
            children = self._getChildren(curr)
            hasLeft, hasRight, leftChild, rightChild = (
                children[0][0],
                children[0][1],
                children[1][0],
                children[1][1],
            )
            if hasLeft and hasRight:  # has left and right child
                if self._greaterThan(
                    leftChild, rightChild, equal=True
                ) and self._greaterThan(
                    leftChild, curr
                ):  # left child the correct root of subtree
                    self.heap[curr], self.heap[leftChild] = (
                        self.heap[leftChild],
                        self.heap[curr],
                    )
                    curr = leftChild
                elif self._greaterThan(rightChild, leftChild) and self._greaterThan(
                    rightChild, curr
                ):  # right child the correct root of subtree
                    self.heap[curr], self.heap[rightChild] = (
                        self.heap[rightChild],
                        self.heap[curr],
                    )
                    curr = rightChild
                else:
                    break

            elif hasLeft and self._greaterThan(leftChild, curr):
                self.heap[curr], self.heap[leftChild] = (
                    self.heap[leftChild],
                    self.heap[curr],
                )
                curr = leftChild

            elif hasRight and self._greaterThan(rightChild, curr):
                self.heap[curr], self.heap[rightChild] = (
                    self.heap[rightChild],
                    self.heap[curr],
                )
                curr = rightChild
            else:
                break

    def _heapify(self):
        n = len(self.heap) - 1
        curr = n // 2
        while curr > 0:
            self._percolateDown(curr)
            curr -= 1

    def _lessThan(
        self, nodeOne, nodeTwo, equal=False
    ):  # nodeOne < nodeTwo or nodeOne <= nodeTwo
        if equal:
            return self.heap[nodeOne] <= self.heap[nodeTwo]
        else:
            return self.heap[nodeOne] < self.heap[nodeTwo]

    def _greaterThan(
        self, nodeOne, nodeTwo, equal=False
    ):  # nodeOne > nodeTwo or nodeOne >= nodeTwo
        if equal:
            return self.heap[nodeOne] >= self.heap[nodeTwo]
        else:
            return self.heap[nodeOne] > self.heap[nodeTwo]

    def _getChildren(self, nodeIndex):
        leftChild = 2 * nodeIndex
        rightChild = leftChild + 1
        n = len(self.heap)
        children = [[False, False], [leftChild, rightChild]]
        if 0 < leftChild < n:
            children[0][0] = True
        if 0 < rightChild < n:
            children[0][1] = True
        return children

    def pop(self):
        if len(self.heap) == 1:
            return None
        root = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self._percolateDown(1)
        return root

    def _percolateUp(self, nodeIndex):
        curr = nodeIndex
        while curr > 1:
            parent = curr // 2
            if self._greaterThan(curr, parent):
                self.heap[curr], self.heap[parent] = self.heap[parent], self.heap[curr]
                curr = parent
            else:
                break

    def push(self, value):
        self.heap.append(value)
        self._percolateUp(len(self.heap) - 1)

    def getRoot(self):
        if not self.heap:
            return None
        return self.heap[1]

    def size(self):
        return len(self.heap) - 1


if __name__ == "__main__":
    values = [5, 1, -1, -8, -7, 8, -5, 0, 10, -4, 3, 4, -3, 2, -2, -9, 6, 7, 9, -6]
    print(values)
    print("---" * 20)
    heap = Heap.listToHeap(values)
    print(heap.heap)
