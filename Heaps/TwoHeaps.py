"""
Given an stream of integers, find the median of the stream.
The median is the middle value in the list of integers.
If the list has an odd number of integers, the median is the middle value.
If the list has an even number of integers, the median is the average of the two middle values.

Solution:
Use two heaps to keep track of the median.
"""

from Heaps.Heap import Heap


class MedianFinder:
    def __init__(self) -> None:
        self.small = Heap()  # Max Heap
        self.large = Heap()  # Min Heap

    def add(self, num) -> None:
        # add the value to the small half aribitrarly
        self.small.push(num)

        """
        Check if both heaps are not empty and also check if the max value in small
        is less than the min value in large
        """
        if self.large.size() > 0 and (self.large.getRoot() * -1) < self.small.getRoot():
            self.large.push(-1 * self.small.pop())

        """
        Check if the abs(len(small) - len(large)) > 1
        Then depending on which value is larger move it to the larger value
        """
        if self.small.size() - self.large.size() > 1:
            self.large.push(-1 * self.small.pop())

        if self.large.size() - self.small.size() > 1:
            self.small.push(-1 * self.large.pop())

    def findMedian(self):
        if self.small.size() == self.large.size():
            return (self.small.getRoot() + (self.large.getRoot() * -1)) / 2
        elif self.small.size() > self.large.size():
            return self.small.getRoot()
        else:
            return self.large.getRoot() * -1
