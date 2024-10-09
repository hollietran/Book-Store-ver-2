class Calculator:
    def __init__(self):
        pass

    def balanced_parens(self, expression: str) -> bool:
        """
        Checks if the parentheses in the given expression are balanced.
        :param expression: str type; the expression to check
        :return: bool type; True if parentheses are balanced, False otherwise
        """
        stack = []
        for char in expression:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False
        return not stack  # True if the stack is empty after processing

    def evaluate(self, expression: str) -> float:
        """
        Evaluates a mathematical expression with parentheses, addition,
        subtraction, multiplication, and division.
        :param expression: str type; the expression to evaluate
        :return: float type; the result of the evaluation
        """
        # Remove spaces from the expression
        expression = expression.replace(" ", "")

        # Handle cases with no parentheses
        if "(" not in expression:
            return self._evaluate_no_parens(expression)

        # Find the innermost parentheses
        start = 0
        count = 0
        for i in range(len(expression)):
            if expression[i] == '(':
                count += 1
            elif expression[i] == ')':
                count -= 1
            if count == 0:
                end = i + 1
                break

        # Recursively evaluate the inner part
        inner_result = self.evaluate(expression[start + 1:end - 1])

        # Replace the innermost parentheses with the result
        expression = expression[:start] + str(inner_result) + expression[end:]

        # Recursively evaluate the remaining expression
        return self.evaluate(expression)

    def _evaluate_no_parens(self, expression: str) -> float:
        """
        Evaluates an expression without parentheses.
        :param expression: str type; the expression to evaluate
        :return: float type; the result of the evaluation
        """
        numbers = []
        operators = []
        current_number = ""
        for i in range(len(expression)):
            if expression[i].isdigit() or expression[i] == '.':
                current_number += expression[i]
            elif expression[i] in ('+', '-', '*', '/'):
                numbers.append(float(current_number))
                current_number = ""
                operators.append(expression[i])
        numbers.append(float(current_number))

        while operators:
            op = operators.pop(0)
            if op == '+':
                numbers[-2] = numbers[-2] + numbers[-1]
                numbers.pop()
            elif op == '-':
                numbers[-2] = numbers[-2] - numbers[-1]
                numbers.pop()
            elif op == '*':
                numbers[-2] = numbers[-2] * numbers[-1]
                numbers.pop()
            elif op == '/':
                if numbers[-1] == 0:
                    raise ZeroDivisionError("Division by zero")
                numbers[-2] = numbers[-2] / numbers[-1]
                numbers.pop()

        return numbers[0]