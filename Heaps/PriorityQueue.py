class PriorityQueue:
    def __init__(self):
        self.heap = [None]
        self.pMap = {}

    @classmethod
    def mapToHeap(cls, priorityMap):
        heap = cls()
        heap.pMap = priorityMap
        heap.heap = heap.heap + list(heap.pMap.keys())
        print(heap.heap)
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
            print(" " * 4 + f"Current node ({curr}): {self.heap[curr]}")
            print(" " * 4 + f"Right child ({hasRight}): {rightChild}")
            print(" " * 4 + f"Left child ({hasLeft}): {leftChild}")
            if hasLeft and hasRight:  # has left and right child
                if self._greaterThan(
                    leftChild, rightChild, equal=True
                ) and self._greaterThan(
                    leftChild, curr
                ):  # left child the correct root of subtree
                    print(" " * 4 + f"* Swapping {curr} and {leftChild}")
                    self.heap[curr], self.heap[leftChild] = (
                        self.heap[leftChild],
                        self.heap[curr],
                    )
                    curr = leftChild
                elif self._greaterThan(rightChild, leftChild) and self._greaterThan(
                    rightChild, curr
                ):  # right child the correct root of subtree
                    print(" " * 4 + f"* Swapping {curr} and {rightChild}")
                    self.heap[curr], self.heap[rightChild] = (
                        self.heap[rightChild],
                        self.heap[curr],
                    )
                    curr = rightChild
                else:
                    break

            elif hasLeft and self._greaterThan(leftChild, curr):
                print(" " * 4 + f"* Swapping {curr} and {leftChild}")
                self.heap[curr], self.heap[leftChild] = (
                    self.heap[leftChild],
                    self.heap[curr],
                )
                curr = leftChild

            elif hasRight and self._greaterThan(rightChild, curr):
                print(" " * 4 + f"* Swapping {curr} and {rightChild}")
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
        print("---" * 10)
        while curr > 0:
            print(f"-> Percolating down called with heap[{curr}] = {self.heap[curr]}")
            self._percolateDown(curr)
            curr -= 1
        print("---" * 10)

    def _lessThan(
        self, nodeOne, nodeTwo, equal=False
    ):  # nodeOne < nodeTwo or nodeOne <= nodeTwo
        print(
            " " * 4
            + f"_lessThan called with heap[{nodeOne}] = {self.heap[nodeOne]} with priority = {self.pMap[self.heap[nodeOne]]}, "
            + f"heap[{nodeTwo}] = {self.heap[nodeTwo]} with priority = {self.pMap[self.heap[nodeTwo]]}, equal = {equal}"
        )
        if equal:
            result = self.pMap[self.heap[nodeOne]] <= self.pMap[self.heap[nodeTwo]]
            print(
                " " * 5
                + f"* Returning {self.pMap[self.heap[nodeOne]]} <= {self.pMap[self.heap[nodeTwo]]} = {result}"
            )
            return result
        else:
            result = self.pMap[self.heap[nodeOne]] < self.pMap[self.heap[nodeTwo]]
            print(
                " " * 5
                + f"* Returning {self.pMap[self.heap[nodeOne]]} < {self.pMap[self.heap[nodeTwo]]} = {result}"
            )
            return result

    def _greaterThan(
        self, nodeOne, nodeTwo, equal=False
    ):  # nodeOne > nodeTwo or nodeOne >= nodeTwo
        print(
            " " * 4
            + f"_greaterThan called with heap[{nodeOne}] = {self.heap[nodeOne]} with priority = {self.pMap[self.heap[nodeOne]]}, "
            + f"heap[{nodeTwo}] = {self.heap[nodeTwo]} with priority = {self.pMap[self.heap[nodeTwo]]}, equal = {equal}"
        )
        if equal:
            result = self.pMap[self.heap[nodeOne]] >= self.pMap[self.heap[nodeTwo]]
            print(
                " " * 5
                + f"* Returning {self.pMap[self.heap[nodeOne]]} >= {self.pMap[self.heap[nodeTwo]]} = {result}"
            )
            return result
        else:
            result = self.pMap[self.heap[nodeOne]] > self.pMap[self.heap[nodeTwo]]
            print(
                " " * 5
                + f"* Returning {self.pMap[self.heap[nodeOne]]} > {self.pMap[self.heap[nodeTwo]]} = {result}"
            )
            return result

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


if __name__ == "__main__":
    priorityMap = {
        5: 5,
        1: 4,
        -1: 10,
        -8: 6,
        -7: 4,
        8: 6,
        -5: 7,
        0: 6,
        10: 4,
        -4: 3,
        3: 2,
        4: 12,
        -3: 5,
        
        2: 8,
        -2: 4,
        -9: 5,
        6: 5,
        7: 2,
        9: 1,
        -6: 1,
    }
    print(priorityMap)
    print("---" * 20)
    pq = PriorityQueue.mapToHeap(priorityMap)
    print(pq.heap)
