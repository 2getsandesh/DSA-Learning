'''You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i == '+':
                two = stack.pop()
                one = stack.pop()
                stack.append(one+two)
            elif i == '-':
                two = stack.pop()
                one = stack.pop()
                stack.append(one-two)
            elif i == '*':
                two = stack.pop()
                one = stack.pop()
                stack.append(one*two)
            elif i == '/':
                two = stack.pop()
                one = stack.pop()
                stack.append(int(one/two)) #truncates to zero division
            else: stack.append(int(i))
        return stack[0]