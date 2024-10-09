import numpy as np
from Interfaces import Stack


class ArrayStack(Stack):
    def __init__(self):
        """
        Constructor creates an empty ArrayStack object.
        """
        self.n = 0
        self.a = np.zeros(1, dtype=object)  # Initialize with size 1

    def resize(self):
        """
        Helper method; creates a new array that maintains the
        array size invariant and copies the old values.
        """
        new_a = np.zeros(max(1, self.n * 2), dtype=object)  # Double the size of the array, but at least size 1
        for i in range(self.n):
            new_a[i] = self.a[i]  # Simple copy for stack, no circular buffer
        self.a = new_a

    def push(self, x: object):
        """
        Adds the given element to the top of the stack.
        :param x: object type; the element that will be added to the stack.
        :return bool: returns True if the element was successfully added.
        """
        if self.n == len(self.a):
            self.resize()
        self.a[self.n] = x
        self.n += 1
        return True

    def pop(self) -> object:
        """
        Removes the element at the top of the stack.
        :return object: returns the element that was removed.
        Raises IndexError if the stack is empty.
        """
        if self.n == 0:
            raise IndexError("Remove from empty stack")  # Raise IndexError when trying to remove from an empty stack
        self.n -= 1
        removed_element = self.a[self.n]
        if self.n == 0:
            # Reset to default capacity when the list becomes empty
            self.a = [0]
            self.j = 0
        elif len(self.a) >= 3 * self.n:
            self.resize() 
        return removed_element

    def size(self):
        """
        Gets the current number of elements in the stack.
        :return: int: the number of elements in the stack.
        """
        return self.n

    def __str__(self):
        s = "["
        for i in range(self.n):
            s += "%r" % self.a[i]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        """
        Makes this ArrayStack an iterable object.
        """
        self.iterator = 0
        return self

    def __next__(self):
        """
        Returns the next item in the sequence when iterating over the ArrayStack.
        """
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator += 1
        else:
            raise StopIteration()
        return x

    def add(self, i: int, x: object):
        """
        Inserts a new element x at the given index i.
        This will shift elements to the right to make space.
        :param i: int type; index of the position where new element will be inserted
        :param x: object type; i.e., any object
        :raise IndexError: raises IndexError if i is negative or greater than or
        equal to the number of existing elements
        """
        if i < 0 or i > self.n:
            raise IndexError("Index out of bounds")
        if self.n == len(self.a):
            self.resize()
        # Shift elements to the right to make space
        for j in range(self.n, i, -1):
            self.a[j] = self.a[j - 1]
        self.a[i] = x  # Insert the new element
        self.n += 1

    def remove(self, i: int) -> object:
        """
        Removes the element at index i by shifting elements
        left to fill the gap.
        :param i: int type; the index of the element to be removed
        :return: Object type; the element at index i
        :raise IndexError: raises IndexError if i is negative or greater than or
        equal to the number of existing elements
        """
        if i < 0 or i >= self.n:
            raise IndexError("Index out of bounds")
        removed_value = self.a[i]
        # Shift elements to the left to fill the gap
        for j in range(i, self.n - 1):
            self.a[j] = self.a[j + 1]
        self.n -= 1
        if self.n == 0:
            # Reset to default capacity when the list becomes empty
            self.a = [0]
            self.j = 0
        elif len(self.a) >= 3 * self.n:
            self.resize() 
        return removed_value