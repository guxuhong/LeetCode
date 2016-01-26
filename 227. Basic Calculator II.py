"""
Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
The integer division should truncate toward zero.
You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '')
        length, numbers, operators, i = len(s), [], [], 0
        if length == 0:
            return 0
        def myeval(num1, num2, op):
            if op == '+':
                return num1 + num2
            if op == '-':
                return num1 - num2
            if op == '*':
                return num1 * num2
            if op == '/':
                return num1 / num2
        while i < length:
            if s[i] in ['+', '-']:
                while operators != []:
                    numbers[-2] = myeval(numbers[-2], numbers[-1], operators[-1])
                    numbers.pop()
                    operators.pop()
                operators.append(s[i])
                i += 1
            elif s[i] in ['*', '/']:
                while operators != []:
                    if operators[-1] in ['*', '/']:
                        numbers[-2] = myeval(numbers[-2], numbers[-1], operators[-1])
                        numbers.pop()
                        operators.pop()
                    else:
                        break
                operators.append(s[i])
                i += 1
            else:
                temp, i = int(s[i]), i + 1
                while i < length:
                    if s[i] not in ['+', '-', '*', '/']:
                        temp = temp * 10 + int(s[i])
                        i += 1
                    else:
                        break
                numbers.append(temp)
        while operators != []:
            numbers[-2] = myeval(numbers[-2], numbers[-1], operators[-1])
            numbers.pop()
            operators.pop()
        return numbers[0]
