import Book
import Calculator
import BookStore
import your_tester

def menu_calculator():
    calculator = Calculator.Calculator()
    option = ""
    while option.upper() != 'Q':
        menu = "-" * 40 + "\nCALCULATOR MENU\n1. Check mathematical expression\nQ. Return to main menu\n\nEnter your selection: "
        option = input(menu)
        if option == '1':
            expression = input("-" * 40 + "\nIntroduce the mathematical expression: ")
            if calculator.balanced_parens(expression):
                print(f"Parentheses are BALANCED.\n")
            else:
                print(f"Parentheses are NOT BALANCED.\n")
        elif option.upper() != 'Q':
            print("Invalid selection.  Please try again.\n")


def menu_bookstore_system():
    bookStore = BookStore.BookStore()
    option = ''
    while option.upper() != 'Q':
        print("-" * 40 + """
        BOOKSTORE MENU
        1. Load book catalog
        2. Edit the book catalog
        3. Access book at index
        4. Search book by infix
        5. Add a book by index to shopping cart
        6. Remove from the shopping cart
        Q. Return to main menu
        """)
        option = input("Enter your selection: ")
        if option == "1":
            file_name = input("-" * 40 + "\nIntroduce the name of the file: ")
            bookStore.loadCatalog(file_name)
        elif option == "2":
            option2 = ''
            while option2.upper() != 'Q':
                print("-" * 40 + """
                EDIT CATALOG MENU
                1. Insert a book to the catalog
                2. Delete an existing book
                Q. Return to bookstore menu
                """)
                option2 = input("Enter your selection: ")
                if option2 == '1':
                    key = input("-" * 40 + "\nEnter the book key: ")
                    title = input("Enter the book title: ")
                    group = input("Enter the book group: ")
                    rank = input("Enter the book rank: ")
                    similar = input("Input keys of similar books separated by a space: ")
                    book = Book.Book(key, title, group, rank, similar)
                    idx = int(input("Enter the index of insertion: "))
                    bookStore.addToCatalog(idx, book)
                elif option2 == '2':
                    i = int(input("-" * 40 + "\nIntroduce the index to remove from catalog: "))
                    bookStore.removeFromCatalog(i)
        elif option == "3":
            idx = int(input("-" * 40 + "\nIntroduce the index: "))
            bookStore.getBookAtIndex(idx)

        elif option == "4":
            infix = input("-" * 40 + "\nIntroduce the query to search: ")
            cnt = int(input("Enter max number of results: "))
            bookStore.searchBookByInfix(infix, cnt)

        elif option == "5":
            i = int(input("-" * 40 + "\nIntroduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)

        elif option == "6":
            print("-" * 40)
            bookStore.removeFromShoppingCart()

        elif option.upper() != 'Q':
            print("Invalid selection.  Please try again.\n")


def main():
    option = ""
    while option.upper() != 'Q':
        print("-" * 40 + """
        MAIN MENU
        1. Calculator
        2. Bookstore System
        3. Run your own tester
        Q. Quit
        """)
        option = input("Enter your selection: ")

        if option == "1":
            menu_calculator()
        elif option == "2":
            menu_bookstore_system()
        elif option == "3":
            print("\n" + "-" * 40)
            your_tester.test()
        elif option.upper() != 'Q':
            print("Invalid selection.  Please try again.\n")


if __name__ == "__main__":
    main()
