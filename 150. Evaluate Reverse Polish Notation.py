"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                stack.append(int(tokens[i]))
            else:
                if tokens[i] == "+":
                    stack[-2] += stack[-1]
                elif tokens[i] == "-":
                    stack[-2] -= stack[-1]
                elif tokens[i] == "*":
                    stack[-2] *= stack[-1]
                else:
                    stack[-2] = int(float(stack[-2]) / stack[-1])
                stack.pop()
        return stack[0]
