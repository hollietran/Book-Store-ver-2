import sys
import traceback

import BinarySearchTree
import BinaryTree
from Book import Book
import ArrayList
import MaxQueue
import time
import DLList
import ChainedHashTable


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
        self.mapTitlesToIdxs = BinarySearchTree.BinarySearchTree()

    """ --------- METHODS RELATED TO THE CATALOG --------- """

    def load_catalog(self, fileName: str, ds: str):
        """
        reads the text file at the given directory and creates a list with all books.
        Each book record contains a key, title, group, rank (number of copies sold) and
        a list of keys of similar books
        :param fileName: str type; the name of the text file containing the book catalog
        :param ds: str type; the option of list data structure to use 1 - ArrayList, 2 - DLList
        """
        try:
            if ds == '1':
                self.bookCatalog = ArrayList.ArrayList()
                self.mapKeysToIdxs = ChainedHashTable.ChainedHashTable(ArrayList.ArrayList)
            elif ds == '2':
                self.bookCatalog = DLList.DLList()
                self.mapKeysToIdxs = ChainedHashTable.ChainedHashTable()
            else:
                raise ValueError(f"Invalid option {ds} for data structure given")
            with open(fileName, encoding="utf8") as f:
                # The following line is the time that the computation starts
                start_time = time.time()
                for line in f:
                    (key, title, group, rank, similar) = line.split("^")
                    s = Book(key, title, group, rank, similar)
                    self.bookCatalog.append(s)
                    idx = self.bookCatalog.size() - 1
                    self.mapKeysToIdxs.add(key, idx)
                    self.mapTitlesToIdxs.add(title.lower(), idx)
                elapsed_time = time.time() - start_time
                print(f"Loaded {self.bookCatalog.size()} books in {elapsed_time} seconds.")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)

    def add_to_catalog(self, i, book: Book):
        """
        inserts a new book to the catalog at the given index
        :param i: int type; the index of insertion
        :param book: Book type; the new book
        :return: None
        """
        try:
            print(f"Current catalog size: {self.bookCatalog.size()}")
            start_time = time.time()
            self.bookCatalog.add(i, book)
            elapsed_time = time.time() - start_time
            print(f"Inserted the following book at index {i}:{book}\nAction completed in {elapsed_time} seconds.")
        except IndexError:
            print(f"Index {i} is out of bounds for catalog of size {self.bookCatalog.size()}.")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)

    def remove_from_catalog(self, i: int):
        """
        removes from the catalog the book at index i and displays its information
        :param i: int type; the index of the book to be removed
        """
        try:
            print(f"Current catalog size: {self.bookCatalog.size()}")
            start_time = time.time()
            removed_book = self.bookCatalog.remove(i)
            elapsed_time = time.time() - start_time
            print(f"Removed the following book from catalog:{removed_book}\nCatalog size after removal: "
                  f"{self.bookCatalog.size()}\nAction completed in {elapsed_time} seconds.")
        except IndexError:
            print(f"Index {i} is out of bounds for catalog of size {self.bookCatalog.size()}")
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
            print(f"Accessed the following book from catalog:{book}\nAction completed in {elapsed_time} seconds.")
        except IndexError:
            print(f"Index {i} is out of bounds for catalog of size {self.bookCatalog.size()}")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)

    def search_by_infix(self, infix: str, n: int):
        """
        search the catalog for the first k books whose titles contain the given substring
        if less than k books contain the substring, then the max number of books that is
        less than k are displayed
        :param infix: str type; the substring that titles should contain
        :param n: int type; the max number of books to display
        """
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
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)

    def search_by_title(self, title: str):
        """
        finds the index of the Book with the given title if it exists
        :param title: str type; gets the catalog index of the Book with
                      the given title if it exists; None otherwise
        """
        try:
            start_time = time.time()
            idx = self.bookCatalog.index_of(title)
            elapsed_time = time.time() - start_time
            if idx is None:
                print(f"\nThe title \"{title}\" does not exist in the catalog.")
            else:
                print(
                    f"\nThe following book matching the given title was found at catalog index {idx}:{self.bookCatalog.get(idx)}")
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
            print(f"Action completed in {elapsed_time} seconds.")
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
          
            # FIXME: r should be the first node in the tree mapping titles to indices whose key starts with prefix
            # HINT: look at the load_catalog() method to determine what r should be
            r = self.mapTitlesToIdxs.bookstore_helper(lowercase_prefix)
            if r == None:
                print(f"\nThere are no titles that begin with \"{prefix}\" in the catalog.")
            else:
                # creating a subtree rooted at the first node in the tree that contains the prefix
                bt = BinaryTree.BinaryTree()
                bt.r = r

                # FIXME: Fix the line below so that nodes is the list of nodes in the subtree
                #        as they are traversed in the order that will list the book titles
                #        in alphabetical order.
                nodes = bt._in_order(bt.r)
              
                printed = 0
                for i in range(len(nodes)):
                    idx = nodes[i].v
                    book = self.bookCatalog.get(idx)
                    title = book.title.lower()

                    # FIXME: Replace the condition in the if statement with the correct condition 
                    #        that checks if the title starts with the given prefix.  REMEMBER that 
                    #        the comparison should be case-insensitive.
                    if title.startswith(lowercase_prefix): 
                        print('-'*20 +f"\nMatch #{printed+1} at index {idx}:\n{book}")
                        printed +=1
                    if n == printed:
                        break
                elapsed_time = time.time() - start_time
                print(f"Found {printed} matches in {elapsed_time} seconds.")
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
            print(f"\nAdded to shopping cart: {s} \nAction completed in {elapsed_time} seconds.")
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
            start_time = time.time()
            bestseller = self.shoppingCart.max()
            elapsed_time = time.time() - start_time
            print("All books in shopping cart:")
            for book in self.shoppingCart:
                print('-' * 10 + str(book))
            print('-' * 30 + f"\nThe highest ranking book:{bestseller}\nAction completed in {elapsed_time} seconds")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)
