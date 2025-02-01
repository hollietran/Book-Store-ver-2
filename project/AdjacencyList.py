from Interfaces import Graph, List
import numpy as np
from ArrayList import ArrayList
from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n: int, dtype=ArrayList):
        self.n = n
        self.dtype = dtype
        self.adj = np.zeros(n, dtype=self.dtype)
        for i in range(self.n):
            self.adj[i] = self.dtype()

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
        if self.has_edge(i,j):
            return False
        self.adj[i].append(j)
        return True

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
        for k in range(self.adj[i].size()):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return True
        return False

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
        for k in range(self.adj[i].size()):
            if self.adj[i].get(k) == j:
                return True
        return False

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
        return self.adj[i]
        '''l = self.dtype() #uhh it says d something
        for j in range(self.n):
            if self.has_edge(i, j):
                l.append(j)
        return l'''

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
        sources = self.dtype()
        for i in range(self.n):
            if self.has_edge(i, j):
                sources.append(i)
        return sources

    def bfs(self, r: int):
        """
        returns a List of the node indices of the graph as they are
        traversed using Breadth-First Search Traversal beginning at
        the node at index r
        :param r: int type; the index of the source node
        :returns: List subclass type; ArrayList or DLList as specified by
                the attribute 'dtype'
        """
        # FIXME
        if r < 0 or r >= self.n:
            raise IndexError("Index out of bounds.")
        l = self.dtype()
        visited = np.zeros(self.n)
        q = ArrayQueue()
        q.add(r)
        visited[r] = True
        while q.size() > 0:  # Replace `is_empty()` with `size() > 0` or `len(q) > 0`
            s = q.remove()
            l.append(s)
            for i in self.out_edges(s):
                if not visited[i]:
                    q.add(i)
                    visited[i] = True
        return l

    def dfs(self, r: int):
        """
        returns a List of the node indices of the graph as they are
        traversed using Depth-First Search Traversal beginning at
        the node at index r
        :param r: int type; the index of the source node
        :returns: List subclass type; ArrayList or DLList as specified by
                the attribute 'dtype'
        """
        # FIXME
        if r < 0 or r >= self.n:
            raise IndexError("Index out of bounds.")
        l = self.dtype()
        visited = np.zeros(self.n)
        s = ArrayStack()
        s.push(r)
        while s.size() > 0:
            p = s.pop()
            if not visited[p]:
                l.append(p)
                visited[p] = True
                # Process neighbors in reverse order to match expected traversal
                neighbors = self.out_edges(p)
                for i in range(neighbors.size() - 1, -1, -1):
                    s.push(neighbors.get(i))
        return l

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