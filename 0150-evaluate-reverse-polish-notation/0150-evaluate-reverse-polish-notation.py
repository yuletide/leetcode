class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # input: array of strings - tokens representing a valid arithmetic expression in RPN
        # output: 32 bit integer result of arithmetic
        # operators: +, -, *, /
        # rules:
        # - Operand can be 32 bit integer or expression
        # - Integer division truncates to zero
        # - How many operands per operator??
        # - assume that each operator takes 2 operands for now

        # Steps:
        # For each item in input list, push to calculator stack until we hit an operator
        # Once we hit operator, pop off 2 items from stack, and perform operation, store result as current solution value, and push to stack

        # operand1 = stack.pop()
        # operand2 = stack.pop()
        operators = set(['+', '-', '*', '/'])
        stack = deque([])

        # if len(tokens) == 1:
        #     return int(tokens[0])
        for token in tokens:
            if token in operators:
                # print("operating", token)
                operand1 = int(stack.pop())
                operand2 = int(stack.pop())
                string = f"{operand2}{token}{operand1}"
                if token == '+':
                    result = operand2 + operand1
                elif token == '-':
                    result = operand2 - operand1
                elif token == '*':
                    result = operand2 * operand1
                elif token == '/':
                    result = operand2 / operand1
                # print(string)
                # this is hella slow cause we doing all the python
                # result = int(eval(string))
                stack.append(int(result))
                # print(result)
            else:
                stack.append(token)
        return int(stack.pop())
            

            




        