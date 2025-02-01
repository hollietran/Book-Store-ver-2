import sys
import traceback
import time

import AdjacencyList
import AdjacencyMatrix
import algorithms
import ArrayList
import DLList
import ChainedHashTable
from exceptions import InvalidStateException
import BinaryHeap
import BinarySearchTree
import BinaryTree
from Book import Book
import MaxQueue
from SortableBook import SortableBook


class BookStore:
    """
    Simulates a book system such as Amazon. It allows  searching,
    removing and adding to a shopping cart.  New items can be added to the
    catalog.  Existing items can be removed from the catalog
    """

    def __init__(self):
        self.bookCatalog = None
        self.shoppingCart = MaxQueue.MaxQueue()
        self.mapKeysToIdxs = None
        self.mapTitlesToIdxs = None
        self.booksByRank = None
        self.catalogIsSorted = None
        self.similarityGraph = None
        self.dtype = None

    """ --------- METHODS RELATED TO THE CATALOG --------- """

    def load_catalog(self, fileName: str, catalog_ds: str, graph_ds: str, sort_by: str):
        """
        reads the text file at the given directory and creates a list with all books.
        Each book record contains a key, title, group, rank (number of copies sold) and
        a list of keys of similar books
        :param fileName: str type; the name of the text file containing the book catalog
        :param catalog_ds: str type; the option of list data structure to use 1 - ArrayList, 2 - DLList
        :param sort_by: str type; the option of sorting algorithm to use:
                        1 - Quick-sort w/ random pivot, 2 - Quick-sort w/ first element pivot
                        If invalid option is given, catalog is not sorted
        """
        self.mapTitlesToIdxs = BinarySearchTree.BinarySearchTree()
        self.catalogIsSorted = False
        msg = ""
        try:
            if catalog_ds == '1':
                self.dtype = ArrayList.ArrayList
                msg += "- ArrayList catalog selected.  "
            elif catalog_ds == '2':
                self.dtype = DLList.DLList
                msg += "- DLList catalog selected.  "
            else:
                raise ValueError(f"'{catalog_ds}' is not a valid catalog data structure option.")

            self.bookCatalog = self.dtype()
            self.mapKeysToIdxs = ChainedHashTable.ChainedHashTable(self.dtype)

            # begin loading catalog
            start_time = time.time()

            with open(fileName, encoding="utf8") as f:
                for line in f:
                    (key, title, group, rank, similar) = line.split("^")
                    s = SortableBook(key, title.strip(), group, rank, similar)
                    self.bookCatalog.append(s)


            # sorting catalog
            if sort_by == '1':
                algorithms.quick_sort(self.bookCatalog)
                self.catalogIsSorted = True
                msg += "\n- Catalog was sorted with quick-sort, random pivot.  "
            elif sort_by == '2':
                algorithms.quick_sort(self.bookCatalog, False)
                self.catalogIsSorted = True
                msg += "\n- Catalog was sorted with quick_sort, first-element pivot.  "
            else:
                msg += "\n- Invalid sorting algorithm selected. Catalog was not sorted."

            elapsed_time = time.time() - start_time

            # loading dictionaries
            for i in range(self.bookCatalog.size()):
                book = self.bookCatalog.get(i)
                self.mapKeysToIdxs.add(book.key, i)  # chained-hash table maps (book key, catalog idx)
                self.mapTitlesToIdxs.add(book.title.lower(), i)  # binary search tree maps (book title, catalog idx)

            n = self.bookCatalog.size()
          
            # loading graph
            if graph_ds == '1':
                self.similarityGraph = AdjacencyList.AdjacencyList(n) # FIXME: Initialize to an AdjacencyList
            elif graph_ds == '2':
                self.similarityGraph = AdjacencyMatrix.AdjacencyMatrix(n) # FIXME: Initialize to an AdjacencyList
            else:
                raise ValueError(f"'{graph_ds}' is not a valid graph data structure option.")

            m = 0 # This will be the number of edges in the graph
            for source_node in range(self.bookCatalog.size()):
                book = self.bookCatalog.get(source_node)
                similar = book.similar.split(" ") # Splitting the string of keys to similar books
                
                # cleaning the list
                similar = [x for x in similar[1:] if len(x) > 0]

                for j in range(len(similar)):
                    key = similar[j]
                    if '\n' in key:
                        key = key.replace('\n', '')  # removing unwanted characters in the key
                      
                    target_node = self.mapKeysToIdxs.get(key) # FIXME: Get the index corresponding to the key
                    if target_node is not None:
                        # FIXME: Add the edge (source_node, target_node) to the graph
                        self.similarityGraph.add_edge(source_node, target_node)
                        m += 1
            print("\nLoad Summary:\n"+msg + f"\n- Loaded and sorted {n} items.\n- Created graph with {n} nodes and {m} edges." + f"\nAction completed in {elapsed_time} seconds.")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)

    def get_book_at_index(self, i: int):
        """
        retrieves the Book at index i of the catalog
        :param i: int type; the index of the book to retrieve
        :return: Book type; the book at index i of the catalog
        """
        try:
            start_time = time.time()
            book = self.bookCatalog.get(i)
            elapsed_time = time.time() - start_time
            print(f"Accessed the following book from catalog:{book}")
            print(f"\nAction completed in {elapsed_time} seconds.")
        except IndexError:
            print(f"Index {i} is out of bounds for catalog of size {self.bookCatalog.size()}")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)

    def search_by_infix(self, infix: str, n: int, by_rank: bool):
        """
        search the catalog for the first n books whose titles contain the given substring
        if less than k books contain the substring, then the max number of books that is
        less than k are displayed
        :param infix: str type; the substring that titles should contain
        :param n: int type; the max number of books to display
        :param by_rank: bool type; if True, matching books are displayed in order
                        of highest rating; otherwise, matching books are displayed
                        in order of first match according usingby_rankp linear search
        """
        if not by_rank:
            try:
                printed = 0
                start_time = time.time()
                for i in range(self.bookCatalog.size()):
                    book = self.bookCatalog.get(i)
                    if infix.lower() in book.title.lower():
                        print("-" * 25 + f"\nMatch found at catalog index {i}:\n{book}\n")
                        printed += 1
                    if printed == n:
                        break
                elapsed_time = time.time() - start_time
                print(f"Found {printed} matches in {elapsed_time} seconds.")
            except Exception:
                print("The following unexpected error occurred:")
                traceback.print_exc(limit=2, file=sys.stdout)
        else:
            try:

                start_time = time.time()
                self.booksByRank = BinaryHeap.BinaryHeap()
                for i in range(self.bookCatalog.size()):
                    book = self.bookCatalog.get(i)
                    if infix.lower() in book.title.lower():
                        b = Book(book.key, book.title, book.group, -1 * book.rank, book.group)
                        self.booksByRank.add(b)
                printed = 0
                for i in range(self.booksByRank.size()):
                    top_book = self.booksByRank.remove()
                    top_book.rank = abs(top_book.rank)
                    print("-" * 25 + f"\nTop Match #{printed + 1}:\n{top_book}\n")
                    printed += 1
                    if printed == n:
                        break
                elapsed_time = time.time() - start_time
                print(f"Found {printed} matches in {elapsed_time} seconds.")
            except Exception:
                print("The following unexpected error occurred:")
                traceback.print_exc(limit=2, file=sys.stdout)

    def search_by_title(self, title: str, search_algo):
        """
        finds the index of the Book with the given title if it exists
        :param title: str type; gets the catalog index of the Book with
                      the given title if it exists; None otherwise
        """
        try:
            if search_algo == '1':
                start_time = time.time()
                idx = algorithms.linear_search(self.bookCatalog, title)
                elapsed_time = time.time() - start_time
            elif search_algo == '2':
                if self.catalogIsSorted:
                    start_time = time.time()
                    idx = algorithms.binary_search(self.bookCatalog, title)
                    elapsed_time = time.time() - start_time
                else:
                    raise InvalidStateException("Cannot perform Binary Search on unsorted catalog.")
            else:
                raise ValueError("Invalid searching algorithm was selected.  Please try again.")
            if idx is None:
                print(f"\nThe title \"{title}\" does not exist in the catalog.")
            else:
                print(
                    "-" * 40 + f"\nThe following book matching the given title was found at catalog index {idx}:{self.bookCatalog.get(idx)}")
            print(f"Action completed in {elapsed_time} seconds.")

        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)

    def search_by_key(self, key):
        """
        displays the book with the given key if it exists
        :param key: str type; the key of the book to search for
        """
        try:
            start_time = time.time()
            idx = self.mapKeysToIdxs.find(key)
            elapsed_time = time.time() - start_time
            if idx is None:
                print(f"\nThere is no book with key \"{key}\" in the catalog.")
            else:
                print(
                    f"\nThe following book matching the given key was found at catalog index {idx}:{self.bookCatalog.get(idx)}")
            print(f"\nAction completed in {elapsed_time} seconds.")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)
        return

    def search_by_prefix(self, prefix, n):
        """
        displays the first n books in alphabetical order whose titles
        begin with the given prefix (ignores case).
        :param prefix: str type;
        :param n: int type; the max number of results to display
        """
        lowercase_prefix = prefix.lower()
        try:
            start_time = time.time()
            r = self.mapTitlesToIdxs.bookstore_helper(lowercase_prefix)
            printed = 0
            if r is None:
                print(f"\nThere are no titles that begin with \"{prefix}\" in the catalog.")
            else:
                bt = BinaryTree.BinaryTree()
                bt.r = r
                nodes = ArrayList.ArrayList(bt.bf_order())
                algorithms.merge_sort(nodes)
                for i in range(len(nodes)):
                    idx = nodes[i].v
                    book = self.bookCatalog.get(idx)
                    if lowercase_prefix == book.title[0:len(prefix)].lower():
                        print('-' * 20 + f"\nMatch #{printed + 1} at index {idx}:\n{book}")
                        printed += 1
                    if n == printed:
                        break
            elapsed_time = time.time() - start_time
            print(f"\nFound {printed} matches in {elapsed_time} seconds.")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)
        return

    """ --------- METHODS RELATED TO THE SHOPPING CART --------- """

    def add_book_at_index(self, i: int):
        """
        adds the book at index i of the catalog into the shopping cart
        :param i: int type; the index in the catalog of the desired book
        """
        try:
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"\nAdded to shopping cart: {s}")
            self._display_similar(i)
            print(f"\nAction completed in {elapsed_time} seconds.")
        except IndexError:
            print(f"Index {i} is out of bounds for catalog of size {self.bookCatalog.size()}")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)

    def add_book_with_key(self, key):
        """
        adds the book with given key into the shopping cart if it exists
        :param key: str type; the key in the catalog of the desired book
        """
        try:
            start_time = time.time()
            i = self.mapKeysToIdxs.find(key)
            if i is not None:
                s = self.bookCatalog.get(i)
                self.shoppingCart.add(s)
                elapsed_time = time.time() - start_time
                print(f"\nAdded to shopping cart: {s}")
                self._display_similar(i)
                print(f"\nAction completed in {elapsed_time} seconds.")
            else:
                print(f"The key '{key}' does not exist in the catalog")
        except IndexError:
            print(f"Index {i} is out of bounds for catalog of size {self.bookCatalog.size()}")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)

    def remove_from_shopping_cart(self):
        """
        removes and displays one book from the shopping cart in FIFO order
        """
        try:
            start_time = time.time()
            if self.shoppingCart.size() > 0:
                u = self.shoppingCart.remove()
                elapsed_time = time.time() - start_time
                print(
                    f"Removed from shopping cart the following book:\n{u}\nAction completed in {elapsed_time} seconds.")
            else:
                elapsed_time = time.time() - start_time
                print(f"Nothing to remove.  Shopping cart is empty.\nAction completed in {elapsed_time} seconds.")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)

    def cart_best_seller(self):
        """
        displays the item with the highest number of sales that is in
        the shopping cart
        """
        try:

            if self.shoppingCart.size() > 0:
                start_time = time.time()
                bestseller = self.shoppingCart.max()
                elapsed_time = time.time() - start_time
                print("All books in shopping cart:")
                for book in self.shoppingCart:
                    print('-' * 10 + str(book))
                print('-' * 30 + f"\nThe highest ranking book:{bestseller}\nAction completed in {elapsed_time} seconds")
            else:
                print("Shopping cart is empty.")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)

    """ HELPER METHOD"""

    def _display_similar(self, idx: int):
        """
        helper method; displays the key, index, group, and title of the items
        that are similar to the item at the given index.
        :param idx: int type; the index of the item
        """
        try:
            similar = self.dtype()  # Initializing 'similar' to be an empty ArrayList/DLList
            
            # FIXME: Use the graph to help you place into the List 'similar' the indices of 
            #        the items that are at most two edges away from the given index.

          
            if similar.size() > 0:
                print(f"\nYou might also like:")
                print('-' * 100)
                print("%-15s | %-15s | %-15s | %-100s |" % ('Key', 'Index', 'Group', 'Title'))
                print('-' * 100)
                for i in range(similar.size()):
                    similar_book = self.bookCatalog.get(similar[i])
                    print("%-15s | %-15s | %-15s | %-100s |" % (
                        similar_book.key, similar[i], similar_book.group, similar_book.title))
        except IndexError:
            print(f"Index {idx} is out of bounds for catalog of size {self.bookCatalog.size()}")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)