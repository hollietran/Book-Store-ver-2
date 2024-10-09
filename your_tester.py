from ArrayList import ArrayList
from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack
import random


def test():
    """write your own tester in this function"""

    """
    Testing ArrayStack...
    """
    print("YOUR TESTS:")

    # Initialize an empty ArrayStack
    stack = ArrayStack()
    print("Created empty stack.")

    # Push random unique elements to the stack
    while stack.size() < 5:
        ele = random.randint(1, 10)
        if ele not in stack:
            stack.push(ele)
            print(f"Added: {ele}\nStack after addition: {stack}\n")

    # Pop elements from the stack until empty
    while stack.size() > 0:
        r = stack.pop()
        print(f"Popped: {r}\nStack after removal: {stack}\n")

    # Print the empty stack
    print(stack)

    # Push new random unique elements into the stack again
    while stack.size() < 4:
        ele = random.randint(1, 10)
        if ele not in stack:
            stack.push(ele)
            print(f"Added: {ele}\nStack after addition: {stack}\n")

    # Pop all elements to empty the stack
    while stack.size() > 0:
        r = stack.pop()
        print(f"Popped: {r}\nStack after removal: {stack}\n")
