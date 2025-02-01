import Calculator
import BookStoreCP as BookStore
import tester

import time
def menu_calculator():
    calculator = Calculator.Calculator()
    option = ""
    while option.upper() != 'Q':
        menu = "-"*40 +"\nCALCULATOR MENU\n1. Store variable values.\n2. Display stored variables.\n3. Evaluate expression with stored values.\nQ. Return to main menu\n\nEnter your selection: "
        option = input(menu)
        if option == '1':
            r = ''
            while r.upper() != 'N':
                var = input("-"*40 + "\nEnter the variable: ")
                value = float(input(f"Enter its value: {var} = "))
                added = calculator.store_var(var, value)
                if not added:
                    s = input("Replace value? Y/N: ")
                    if s.upper() == 'Y':
                        calculator.store_var(var, value, True)
                r = input("\nEnter another variable? Y/N: ")
        elif option == '2':
            print("-"*40 + f"\nDisplaying stored variables:")
            calculator.print_stored_vars()

        elif option == '3':
            expression = input("-" * 40 + "\nIntroduce the mathematical expression: ")
            if calculator.balanced_parens(expression):
                expr_with_values, vars_without_vals = calculator.expr_with_values(expression)
                print("Expression with values:", expr_with_values)
                if len(vars_without_vals) > 0:
                    print("Can NOT evaluate expression because the following variables have not been assigned values:")
                    for v in vars_without_vals:
                        print(f"\t* {v}")
                else:
                    start_time = time.time()
                    value = calculator.evaluate(expression)
                    elapsed_time = time.time() - start_time
                    print("Result:", value)
                    print(f"Action completed in {elapsed_time} seconds.")

            else:
                print(f"Parentheses are NOT BALANCED. Replacing values is not supported for invalid expressions.\n")

        elif option.upper() != 'Q':
            print("Invalid selection.  Please try again.\n")


def menu_bookstore_system():
    bookStore = BookStore.BookStore()
    option = ''
    while option.upper() != 'Q':
        print("-"*40 + """
        BOOKSTORE MENU
        1. Load book catalog
        2. Access book at index
        3. Search Menu
        4. Shopping Cart Menu
        Q. Return to main menu
        """)
        option = input("Enter your selection: ")
        if option == "1":
            file_name = input("-"*40 +"\nIntroduce the name of the file: ")
            ds = input("\nEnter the desired catalog data structure:\n\t1. ArrayList\n\t2. DLList\n\nYour selection: ")
            graph = input("\nEnter the desired graph data structure:\n\t1. AdjacencyList\n\t2. AdjacencyMatrix\n\nYour selection: ")
            sort_by = input("\nChoose sorting algorithm:\n\t1. Quick-Sort (random pivot)\n\t2. Quick-Sort (first-element pivot)\n\nYour selection: ")
            bookStore.load_catalog(file_name, ds, graph, sort_by)

        elif option == "2":
            idx = int(input("-"*40 + "\nIntroduce the index: "))
            bookStore.get_book_at_index(idx)

        elif option == "3":
            s = ''
            while s.upper() != 'Q':
                print("-" * 40 + """
                    SEARCH MENU
                    1. Search for matching infix
                    2. Search for matching title
                    3. Search for matching key
                    4. Search for matching prefix
                    Q. Return to bookstore menu
                            """)
                s = input("Enter your selection: ")
                if s == '1':
                    infix = input("-"*40 + "\nIntroduce the query to search for: ")
                    cnt = int(input("Enter max number of results: "))
                    srch_choice = input("Display by...\n\t1. first matching\n\t2. top-ranking\nEnter your selection: ")
                    if srch_choice == '1':
                        bookStore.search_by_infix(infix, cnt, False)
                    elif srch_choice == '2':
                        bookStore.search_by_infix(infix, cnt, True)
                    else:
                        print("Invalid selection.  Please try again.")
                elif s == '2':
                    title = input("-" * 40 + "\nIntroduce the title to search for: ")
                    algo = input("Select the searching algorithm:\n\t1. Linear Search\n\t2. Binary Search\n\nEnter your selection: ")
                    bookStore.search_by_title(title, algo)
                elif s == '3':
                    key = input("-" * 40 + "\nIntroduce the book key to search for: ")
                    bookStore.search_by_key(key)
                elif s == '4':
                    prefix = input("-" * 40 + "\nIntroduce the title prefix to search for: ")
                    cnt = int(input("Enter max number of results: "))
                    bookStore.search_by_prefix(prefix, cnt)
                elif s.upper() != 'Q':
                    print("Invalid selection.  Please try again.")

        elif option == "4":
            s = ''
            while s.upper() != 'Q':
                print("-" * 40 + """
                SHOPPING CART MENU
                1. Add a book by index to shopping cart
                2. Add a book by key to shopping cart
                3. Remove from the shopping cart
                4. Get the cart bestseller
                Q. Return to bookstore menu
                """)
                s = input("Enter your selection: ")
                if s == '1':
                    i = int(input("-" * 40 + "\nIntroduce the index: "))
                    bookStore.add_book_at_index(i)
                elif s == '2':
                    key = input("-" * 40 + "\nIntroduce the item key: ")
                    bookStore.add_book_with_key(key)
                elif s == '3':
                    print("-" * 40)
                    bookStore.remove_from_shopping_cart()
                elif s == '4':
                    print("-" * 40)
                    bookStore.cart_best_seller()
                elif s != 'q':
                    print("Invalid selection.  Please try again.")



        elif option.upper() != 'Q':
            print("Invalid selection.  Please try again.\n")




# main: Create the main menu
def main():
    option = ""
    while option.upper() != 'Q':
        print("-"*40 + """
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
            tester.test()
        elif option.upper() != 'Q':
            print("Invalid selection.  Please try again.\n")


if __name__ == "__main__":
    main()
