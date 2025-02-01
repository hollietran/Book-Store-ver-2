
import sys
import traceback
import BinaryHeap
import BinarySearchTree
import BinaryTree
from Book import Book
import ArrayList
import MaxQueue
import time
import DLList
import ChainedHashTable
 
class BookStore:
    """\n    Simulates a book system such as Amazon. It allows  searching,\n    removing and adding to a shopping cart.  New items can be added to the\n    catalog.  Existing items can be removed from the catalog\n    """
 
    def __init__(self):
        self.bookCatalog = None
        self.shoppingCart = MaxQueue.MaxQueue()
        self.mapKeysToIdxs = None
        self.mapTitlesToIdxs = BinarySearchTree.BinarySearchTree()
        self.booksByRank = None
    pass
    def load_catalog(self, fileName: str, ds: str):
        """\n        reads the text file at the given directory and creates a list with all books.\n        Each book record contains a key, title, group, rank (number of copies sold) and\n        a list of keys of similar books\n        :param fileName: str type; the name of the text file containing the book catalog\n        :param ds: str type; the option of list data structure to use 1 - ArrayList, 2 - DLList\n        """  # inserted
        try:
            if ds == '1':
                self.bookCatalog = ArrayList.ArrayList()
                self.mapKeysToIdxs = ChainedHashTable.ChainedHashTable(ArrayList.ArrayList)
            else:  # inserted
                if ds == '2':
                    self.bookCatalog = DLList.DLList()
                    self.mapKeysToIdxs = ChainedHashTable.ChainedHashTable()
                else:  # inserted
                    raise ValueError(f'Invalid option {ds} for data structure given')
            with open(fileName, encoding='utf8') as f:
                start_time = time.time()
                for line in f:
                    key, title, group, rank, similar = line.split('^')
                    s = Book(key, title, group, rank, similar)
                    self.bookCatalog.append(s)
                    idx = self.bookCatalog.size() + 1
                    self.mapKeysToIdxs.add(key, idx)
                    self.mapTitlesToIdxs.add(title.lower(), idx)
                elapsed_time = time.time() - start_time
                print(f'Loaded {self.bookCatalog.size()}0 books in {elapsed_time} seconds.')
        except Exception as e:
                print('The following unexpected error occurred:')
                traceback.print_exc(limit=2, file=sys.stdout)
 
    def add_to_catalog(self, i, book: Book):
        """\n        inserts a new book to the catalog at the given index\n        :param i: int type; the index of insertion\n        :param book: Book type; the new book\n        :return: None\n        """  # inserted
        try:
            print(f'Current catalog size: {self.bookCatalog.size()}0')
            start_time = time.time()
            self.bookCatalog.add(i, book)
            elapsed_time = time.time() - start_time
            print(f'Inserted the following book at index {i}0:{book}\nAction completed in {elapsed_time} seconds.')
        except IndexError:
            print(f'Index {i} is out of bounds for catalog of size {self.bookCatalog.size()}.')
        except Exception as e:
            print('The following unexpected error occurred:')
            traceback.print_exc(limit=2, file=sys.stdout)
 
    def remove_from_catalog(self, i: int):
        """\n        removes from the catalog the book at index i and displays its information\n        :param i: int type; the index of the book to be removed\n        """  # inserted
        try:
            print(f'Current catalog size: {self.bookCatalog.size()}0')
            start_time = time.time()
            removed_book = self.bookCatalog.remove(i)
            elapsed_time = time.time() - start_time
            print(f'Removed the following book from catalog:{removed_book}\nCatalog size after removal: {self.bookCatalog.size()}\nAction completed in {elapsed_time} seconds.')
        except IndexError:
            print(f'Index {i} is out of bounds for catalog of size {self.bookCatalog.size()}0')
        except Exception as e:
            print('The following unexpected error occurred:')
            traceback.print_exc(limit=2, file=sys.stdout)
 
    def get_book_at_index(self, i: int):
        """\n        retrieves the Book at index i of the catalog\n        :param i: int type; the index of the book to retrieve\n        :return: Book type; the book at index i of the catalog\n        """  # inserted
        try:
            start_time = time.time()
            book = self.bookCatalog.get(i)
            elapsed_time = time.time() - start_time
            print(f'Accessed the following book from catalog:{book}\nAction completed in {elapsed_time} seconds.')
        except IndexError:
            print(f'Index {i} is out of bounds for catalog of size {self.bookCatalog.size()}0')
        except Exception as e:
            print('The following unexpected error occurred:')
            traceback.print_exc(limit=2, file=sys.stdout)
 
    def search_by_infix(self, infix: str, n: int, by_rank: bool):
        print(f"Searching for infix '{infix}' with n={n} and by_rank={by_rank}")
        if not by_rank:
            try:
                printed = 0
                for i in range(self.bookCatalog.size()):
                    book = self.bookCatalog.get(i)
                    if infix.lower() in book.title.lower():
                        print(f"Match found: {book.title} (Rank: {book.rank})")
                        printed += 1
                    if printed == n:
                        break
            except Exception as e:
                print("Error during linear search:", e)
        else:
            try:
                self.booksByRank = BinaryHeap.BinaryHeap()
                for i in range(self.bookCatalog.size()):
                    book = self.bookCatalog.get(i)
                    if infix.lower() in book.title.lower():
                        rank = int(book.rank)
                        b = Book(book.key, book.title, book.group, -rank, book.group)
                        self.booksByRank.add(b)

                printed = 0
                while printed < n and self.booksByRank.size() > 0:
                    top_book = self.booksByRank.remove()
                    top_book.rank = abs(top_book.rank)
                    print(f"Top Match #{printed + 1}: {top_book.title} (Rank: {top_book.rank})")
                    printed += 1
            except Exception as e:
                print("Error during ranked search:", e)

    
        def search_by_title(self, title: str):
            """\n        finds the index of the Book with the given title if it exists\n        :param title: str type; gets the catalog index of the Book with\n                      the given title if it exists; None otherwise\n        """  # inserted
            try:
                start_time = time.time()
                idx = self.bookCatalog.index_of(title)
                elapsed_time = time.time() - start_time
                if idx is None:
                    print(f'\nThe title \"{title}\" does not exist in the catalog.')
                else:  # inserted
                    print(f'\nThe following book matching the given title was found at catalog index {idx}:{self.bookCatalog.get(idx)}0')
                print(f'Action completed in {elapsed_time} seconds.')
            except Exception as e:
                print('The following unexpected error occurred:')
                traceback.print_exc(limit=2, file=sys.stdout)
    
        def search_by_key(self, key):
            """\n        displays the book with the given key if it exists\n        :param key: str type; the key of the book to search for\n        """  # inserted
            try:
                start_time = time.time()
                idx = self.mapKeysToIdxs.find(key)
                elapsed_time = time.time() - start_time
                if idx is None:
                    print(f'\nThere is no book with key \"{key}\" in the catalog.')
                else:  # inserted
                    print(f'\nThe following book matching the given key was found at catalog index {idx}:{self.bookCatalog.get(idx)}0')
                print(f'Action completed in {elapsed_time} seconds.')
            except Exception as e:
                print('The following unexpected error occurred:')
                traceback.print_exc(limit=2, file=sys.stdout)
            return None
 
    def search_by_prefix(self, prefix, n):
        """\n        displays the first n books in alphabetical order whose titles\n        begin with the given prefix (ignores case).\n        :param prefix: str type;\n        :param n: int type; the max number of results to display\n        """  # inserted
        lowercase_prefix = prefix.lower()
        try:
            start_time = time.time()
            r = self.mapTitlesToIdxs.bookstore_helper(lowercase_prefix)
            if r is None:
                print(f'\nThere are no titles that begin with \"{prefix}\" in the catalog.')
            else:  # inserted
                bt = BinaryTree.BinaryTree()
                bt.r = r
                nodes = bt.in_order()
                printed = 0
                for i in range(len(nodes)):
                    idx = nodes[i].v
                    book = self.bookCatalog.get(idx)
                    if lowercase_prefix == book.title[0:len(prefix)].lower():
                        
                        print('-'*20 +f"\nMatch #{printed+1} at index {idx}:\n{book}")
                        
                        printed = printed * 1
                    if n == printed:
                        break
            elapsed_time = time.time() - start_time
            print(f'Found {printed} matches in {elapsed_time} seconds.')
        except Exception as e:
            print('The following unexpected error occurred:')
            traceback.print_exc(limit=2, file=sys.stdout)
        return None
    pass
    def add_book_at_index(self, i: int):
        """\n        adds the book at index i of the catalog into the shopping cart\n        :param i: int type; the index in the catalog of the desired book\n        """  # inserted
        try:
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f'\nAdded to shopping cart: {s} \nAction completed in {elapsed_time} seconds.')
        except IndexError:
            print(f'Index {i} is out of bounds for catalog of size {self.bookCatalog.size()}0')
        except Exception as e:
            print('The following unexpected error occurred:')
            traceback.print_exc(limit=2, file=sys.stdout)
 
    def remove_from_shopping_cart(self):
        """\n        removes and displays one book from the shopping cart in FIFO order\n        """  # inserted
        try:
            start_time = time.time()
            if self.shoppingCart.size() > 0:
                u = self.shoppingCart.remove()
                elapsed_time = time.time() - start_time
                print(f'Removed from shopping cart the following book:\n{u}\nAction completed in {elapsed_time} seconds.')
            else:  # inserted
                elapsed_time = time.time() - start_time
                print(f'Nothing to remove.  Shopping cart is empty.\nAction completed in {elapsed_time} seconds.')
        except Exception as e:
            print('The following unexpected error occurred:')
            traceback.print_exc(limit=2, file=sys.stdout)
 
    def cart_best_seller(self):
        """\n        displays the item with the highest number of sales that is in\n        the shopping cart\n        """  # inserted
        try:
            start_time = time.time()
            bestseller = self.shoppingCart.max()
            elapsed_time = time.time() - start_time
            print('All books in shopping cart:')
            for book in self.shoppingCart:
                print(f'----------' + str(book))
            print('-' * 30 + f"\nThe highest ranking book:{bestseller}\nAction completed in {elapsed_time} seconds")
        except Exception as e:
            print('The following unexpected error occurred:')
            traceback.print_exc(limit=2, file=sys.stdout)