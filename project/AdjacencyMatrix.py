from Interfaces import Graph, List
from ArrayList import ArrayList
from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack
import numpy as np


class AdjacencyMatrix(Graph):

    def __init__(self, n: int, dtype=ArrayList):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)
        self.dtype = dtype

    def add_edge(self, i: int, j: int):
        """
        adds a directed edge from node i to node j
        :param i: int type; index of node i
        :param j: int type; index of node j
        :raises: IndexError if i < 0 or j < 0
                 or i >= number of nodes or j >= number of nodes
        """
        # FIXME
        if i < 0 or j < 0 or i >= self.n or j >= self.n:
            raise IndexError("Index out of bounds.")
        self.adj[i][j] = True
        return self.adj[i][j]

    def remove_edge(self, i: int, j: int):
        """
        removes the directed edge from node i to node j,
        if it exists in the graph.  Returns true if
        edge was removed, false otherwise
        :param i: int type; index of node i
        :param j: int type; index of node j
        :raises: IndexError if i < 0 or j < 0
                 or i >= number of nodes or j >= number of nodes
        :returns: bool type; true if the edge (i, j) was removed, false otherwise.
        """
        # FIXME
        if i < 0 or j < 0 or i >= self.n or j >= self.n:
            raise IndexError("Index out of bounds.")
        
        if self.adj[i][j] == 1:  # Check if the edge exists
            self.adj[i][j] = 0   # Remove the edge
            return True          # Indicate success
        else:
            return False         # Indicate failure (edge did not exist)
    

    def has_edge(self, i: int, j: int) -> bool:
        """
        determines if the directed edge from node i to node j
        exists in the graph.  Returns true if edge (i, j) exists,
        false otherwise.
        :param i: int type; index of node i
        :param j: int type; index of node j
        :raises: IndexError if i < 0 or j < 0
                 or i >= number of nodes or j >= number of nodes
        :returns: bool type; true if the edge (i, j) exists, false otherwise.
        """
        # FIXME
        if i < 0 or j < 0 or i >= self.n or j >= self.n:
            raise IndexError("Index out of bounds.")
        return self.adj[i][j]

    def out_edges(self, i) -> List:
        """
        returns a List of node indices that are targets
        of the node at index i, i.e., a List of all nodes j
        such that (i, j) is an edge in the graph
        :param i: int type; index of source node
        :raises: IndexError if i < 0 or i >= number of nodes
        :returns: List subclass type; either an ArrayList or DLList
                  as specified by the attribute 'dtype'
        """
        # FIXME
        if i < 0 or i >= self.n:
            raise IndexError("Index out of bounds.")
        out_edges = self.dtype()
        for j in range(self.n):
            if self.has_edge(i, j):
                out_edges.append(j)
        return out_edges

    def in_edges(self, j) -> List:
        """
        returns a List of node indices that are sources
        of the node at index j, i.e., a List of all nodes i
        such that (i, j) is an edge in the graph
        :param j: int type; index of targe node
        :raises: IndexError if i < 0 or i >= number of nodes
        :returns: List subclass type; either an ArrayList or DLList
                  as specified by the attribute 'dtype'
        """
        # FIXME
        if j < 0 or j >= self.n:
            raise IndexError("Index out of bounds.")
        in_edges = self.dtype()
        for i in range(self.n):
            if self.has_edge(i, j):
                in_edges.append(i)
        return in_edges

    def bfs(self, r: int):
        """
        returns a List of the node indices of the graph as they are
        traversed using Breadth-First Search Traversal beginning at
        the node at index r
        :param r: int type; the index of the source node
        :returns: List subclass type; ArrayList or DLList as specified by
                the attribute 'dtype'
        """
        if r < 0 or r >= self.n:
            raise IndexError("Index out of bounds.")
        visited = np.zeros(self.n, dtype=bool)
        queue = ArrayQueue()
        queue.add(r)  # Use 'add' instead of 'enqueue'
        visited[r] = True
        bfs_list = self.dtype()
        while queue.size() > 0:  # Check size instead of using 'is_empty'
            u = queue.remove()  # Use 'remove' to dequeue
            bfs_list.append(u)
            for v in self.out_edges(u):
                if not visited[v]:
                    queue.add(v)  # Use 'add' instead of 'enqueue'
                    visited[v] = True
        return bfs_list


    def dfs(self, r: int):
        """
        returns a List of the node indices of the graph as they are
        traversed using Depth-First Search Traversal beginning at
        the node at index r
        :param r: int type; the index of the source node
        :returns: List subclass type; ArrayList or DLList as specified by
                the attribute 'dtype'
        """
        if r < 0 or r >= self.n:
            raise IndexError("Index out of bounds.")
        visited = np.zeros(self.n, dtype=bool)
        stack = ArrayStack()
        stack.push(r)  # Push the starting node
        dfs_list = self.dtype()
        while stack.size() > 0:  # Replace 'is_empty' with 'size() > 0'
            u = stack.pop()  # Pop the top element
            if not visited[u]:
                dfs_list.append(u)
                visited[u] = True
                for v in reversed(self.out_edges(u)):  # Reverse order to match expected traversal
                    if not visited[v]:
                        stack.push(v)
        return dfs_list


    def size(self):
        """
        returns the number of nodes in the graph
        :returns: int type;
        """
        return self.n

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += f"{i}:  {self.adj[i]}\n"
        return s

