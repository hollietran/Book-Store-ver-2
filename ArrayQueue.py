import numpy as np
from Interfaces import Queue

class ArrayQueue(Queue):
    def __init__(self):
        """
        Constructor creates an empty ArrayQueue object.
        """
        self.n = 0  # Number of elements in the queue
        self.j = 0  # Index of the front of the queue
        self.a = np.zeros(1, dtype=object)  # Initialize with size 1

    def resize(self):
        """
        Helper method; creates a new array that maintains the array size invariant
        and copies the old values making sure to maintain FIFO order.
        """
        new_a = np.zeros(self.n * 2, dtype=object)  # Double the size of the array
        # Correctly copy elements from the old array
        for i in range(self.n):
            new_a[i] = self.a[(i + self.j) % len(self.a)]
        self.a = new_a
        self.j = 0  # Reset the front index after resizing

    def add(self, x: object):
        """
        Adds the given element to the tail of the FIFO queue.
        :param x: object type; the element that will be added to the queue.
        :return bool: returns True if the element was successfully added.
        """
        if self.n == len(self.a):
            self.resize()
        # Add to the tail of the queue
        self.a[(self.n + self.j) % len(self.a)] = x
        self.n += 1
        return True

    def remove(self) -> object:
        """
        Removes the element at the head of the FIFO queue.
        :return object: returns the element that was removed or raises IndexError if the queue is empty.
        """
        if self.n <= 0:
            raise IndexError("Remove from empty queue")  # Raise IndexError when trying to remove from an empty queue
        # Remove from the head of the queue
        removed_value = self.a[self.j]
        self.j = (self.j + 1) % len(self.a)  # Move the front index forward
        self.n -= 1
        if self.n == 0:
            # Reset to default capacity when the list becomes empty
            self.a = [0]
            self.j = 0
        elif len(self.a) >= 3 * self.n:
            self.resize() 
        return removed_value

    def size(self):
        """
        Gets the current number of elements in the queue.
        :return: int: the number of elements in the queue.
        """
        return self.n

    def __str__(self):
        s = "["
        for i in range(self.n):
            # Correctly calculate the index for printing
            index = (i + self.j) % len(self.a)
            s += "%r" % self.a[index]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        """
        Makes this ArrayQueue an iterable object.
        """
        self.iterator = 0
        return self

    def __next__(self):
        """
        Returns the next item in the sequence when iterating over the ArrayQueue.
        """
        if self.iterator < self.n:
            x = self.a[(self.iterator + self.j) % len(self.a)]
            self.iterator += 1
        else:
            raise StopIteration()
        return x
