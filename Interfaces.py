from abc import abstractmethod

'''
    Abstract Data types: It provides the list of interfaces 
    (Stack, Queue, Deque, List, Set)
'''


class Queue:
    """
        Queue: The Queue interface represents a collection of elements to which we can
        add elements and remove the next element.
    """

    @abstractmethod
    def add(self, x: object):
        """
        adds the value x to the Queue
        :param x: Object type; i.e., the new object to be added to the queue
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def remove(self) -> object:
        """
        removes the next value in the queue and returns it
        The Queue’s queueing discipline decides which element
        should be removed.
        :return: object type;
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def size(self) -> int:
        """
        returns the size of the queue
        :return: int type; an integer greater or equal to zero
                 representing the number of elements in the queue
        """
        raise NotImplementedError("Subclasses should implement this!")

    def __len__(self):
        """
        returns the size of the queue when using len, i.e., len(q)
        :return: int type; an integer greater or equal to zero
                 representing the number of elements in the queue
        """
        return self.size()


class Stack:
    """
        Stack: It is a LIFO Queue, the most recently added element
                is the next one removed.
    """

    @abstractmethod
    def push(self, x: object):
        """
        inserts an element in the tail of the stack
        :param x: Object type; i.e., the new object to be added
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def pop(self) -> object:
        """
        removes the last element in the stack
        :return: the object of the tail if it is no empty
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def size(self) -> int:
        """
        returns the size of the stack
        :return: int type; an integer greater or equal to zero representing
                 the number of elements in the stack
        """
        raise NotImplementedError("Subclasses should implement this!")

    def __len__(self):
        """
        returns the size of the queue when using len, i.e., len(s)
        where s is a stack instance
        :return: int type; an integer greater or equal to zero representing
                 the number of elements in the stack
        """
        return self.size()


class Deque:
    """
        Deque: is the abstract datatype of a Deque. The behavior depends on
        the implementation using arrays or linked list
    """

    @abstractmethod
    def add_first(self, x: object):
        """
        inserts an element in the head of the deque
        :param x: Object type; the new object to be added.
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def add_last(self, x: object):
        """
        inserts an element in the tail of the deque
        :param x: Object type; the new object to be added.
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def remove_first(self) -> object:
        """
        removes the element in the head of the deque and returns it
        :return: Object type; the object that was removed from the head of the deque
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def remove_last(self) -> object:
        """
        removes the element in the tail of the deque and returns it
        :return: Object type; the object that was removed from the tail of the deque
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def size(self) -> int:
        """
        returns the size of the deque
        :return: int type; an integer greater or equal to zero representing
                 the number of elements in the deque
        """
        raise NotImplementedError("Subclasses should implement this!")

    def __len__(self):
        """
            __len__: Returns the size of the queue when using len, i.e., len(q) where
            q is an instance of queue.
            Return: an integer greater or equal to zero representing the number
                    of elements in the queue
        """
        return self.size()


class List:
    """
        List: is the abstract datatype of a List. The behavior depends on
        the implementation
    """

    @abstractmethod
    def add(self, i: int, x: object):
        """
        inserts a new element at the given index, shifting all objects
        at indices j >= i to one index greater.
        :param i: int type; the index of insertion.
        :param x: Object type; the new object to be added
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def set(self, i: int, x: object):
        """
        replaces the object at the given index with a new object
        :param i: int type; the index of the value to replace;
                  the integer must obey 0 <= i < n, where n is the
                  number of elements in the list
        :param x: object type; the new object
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def get(self, i: int) -> object:
        """
        returns the object at index i of the list
        :param i: int type; the index of the object to retrieve.
                  the integer i must obey 0 <= i < n, where n is the
                  number of elements in the list
        :return: object type; the object at index i of the list.
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def remove(self, i: int) -> object:
        """
            remove: remove th element i and shift all the elements j > i
            one position to the left and decrease n
            Return: return the value x to be removed.
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def size(self) -> int:
        """
            size: Returns the size of the list
            Return: an integer greater or equal to zero representing the number
                    of elements in the list
        """
        raise NotImplementedError("Subclasses should implement this!")

    def __iter__(self):
        """
            __iter__: Initialize the iterator which is used in the for loops
        """
        raise NotImplementedError("Subclasses should implement this!")

    def __next__(self):
        """
            __next__: Move to the next itme in the iterator. It  is used in the for loops
        """
        raise NotImplementedError("Subclasses should implement this!")

    def __len__(self) -> int:
        """
            __len__: Returns the size of the queue when using len, i.e., len(l)
            where l is a list instance
            Return: an integer greater or equal to zero representing the number
                    of elements in the queue
        """
        return self.size()

    def __getitem__(self, i: int) -> object:
        """
            __getitem__: Returns the item in the position i in array format, i.e., l[i]
            where l is a list instance
            Input:
                i: positive integer less than n
            Return: the item at index i
        """
        return self.get(i)

    def __setitem__(self, i: int, x: object):
        """
            __setitem__: Sets the item x in the index  in array format, i.e., l[i] = x
            where l is a list instance
            Input:
                i: positive integer less than or equal n
                    if i in [0, n) then it sets x at index i
                    if i = n then it adds x at the end
                x: the item to set
        """
        if i == self.size():
            self.add(i, x)
        else:
            self.set(i, x)


class Set:
    """
        Set: It is the abstract datatype of a set. The behavior depends on
        the implementation
    """

    @abstractmethod
    def add(self, key: object, value: object):
        """
            add: inserts the tuple(key, value) in the set
            Inputs:
                key: The key of the tuple
                value: the value to store
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def find(self, key: object) -> object:
        """
            find: find the key in the set
            Inputs:
                key: The key of the tuple
            Return:
                the value that corresponds to the key if exists, otherwise returns None
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def remove(self, key: object):
        """
            remove: remove the tuple (key, value) in the set if it exists
            Inputs:
                key: The key of the tuple

        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def size(self) -> int:
        """
            size: Returns the size of the set
            Return: an integer greater or equal to zero representing the number
                    of elements in the set
        """
        raise NotImplementedError("Subclasses should implement this!")

    def __len__(self) -> int:
        """
            __len__: Returns the size of the queue when using len, i.e., len(q)
            Return: an integer greater or equal to zero representing the number
                    of elements in the queue
        """
        return self.size()

    def __missing__(self, key: object) -> bool:
        """
            __missing__: return true if the key exists __getitem__ uses it
            Input:
                key: key of the tuple
        """
        return self.find(key) == None

    def __getitem__(self, key: object) -> object:
        """
            __getitem__: return the value of tuple (key,value) in the set using format, i.e., x = l[i]
            where l is a set instance
            Input:
                key: key of the tuple
        """
        return self.find(key)

    def __setitem__(self, key: object, value: object):
        """
            __setitem__: Add the tuple (key,value) in the set using format, i.e., l[i] = x
            where l is a set instance
            Input:
                key: key of the tuple
                value: the value of the tuple
        """
        self.add(key, value)


class Tree:
  @abstractmethod
  def depth(self, u) -> int:
    """
    computes the depth of node u
    :return: int type; an integer greater or equal to zero representing the number
            of edges in the path from node u to the root
    """
    raise NotImplementedError("Subclasses should implement this!")

  @abstractmethod
  def height(self):
    """
    computes the height of the tree
    """
    raise NotImplementedError("Subclasses should implement this!")

  @abstractmethod
  def size(self):
    """
    returns the number of nodes in the tree
    """
    raise NotImplementedError("Subclasses should implement this!")

  @abstractmethod
  def bf_order(self):
    """
    returns the list of nodes in the tree as they are traversed using breadth-first order traversal
    """
    raise NotImplementedError("Subclasses should implement this!")

  @abstractmethod
  def in_order(self):
    """
    returns the list of nodes in the tree as they are traversed using in-order traversal
    """
    raise NotImplementedError("Subclasses should implement this!")

  @abstractmethod
  def post_order(self):
    """
    returns the list of nodes in the tree as they are traversed using post-order traversal
    """
    raise NotImplementedError("Subclasses should implement this!")

  @abstractmethod
  def pre_order(self):
    """
    returns the list of nodes in the tree as they are traversed using pre-order traversal
    """
    raise NotImplementedError("Subclasses should implement this!")


class Graph:
    """
        Graph: Abstract datatype of a graph.
    """

    @abstractmethod
    def add_edge(self, i: int, j: int):
        """
        adds an edge from source node i to target node j
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def remove_edge(self, i: int, j: int):
        """
        removes the edge (i, j) from the graph
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def has_edge(self, i: int, j: int) -> bool:
        """
        determines whether the edge (i, j) exists in this graph
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def out_edges(self, i: int) -> List:
        """
        returns a list of all nodes incident to node i, where i
        is the source node
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def in_edges(self, j: int) -> List:
        """
        returns a list of all nodes incident to node j, where j is
        the target node
        """
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def size(self) -> int:
        """
        returns the number of nodes in the graph
        """
        raise NotImplementedError("Subclasses should implement this!")
