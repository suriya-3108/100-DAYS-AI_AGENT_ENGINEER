"""Practice Question 3 — Evaluate Postfix Expression
Problem:
A postfix expression (also called Reverse Polish Notation) is a mathematical expression where operators come after the operands.

Example:
Infix: 3 + 4 → Postfix: 3 4 +
Infix: (5 + 2) * 3 → Postfix: 5 2 + 3 *

Task:
Given a postfix expression as a string or list, evaluate its value using a stack."""

a = ["2", "3", "+", "4", "*"]

def fun(a):
    stack = []
    for c in a:
        if c.isdigit():
            stack.append(int(c))
        else:
            b = stack.pop()
            d = stack.pop()
            if c == '+':
                stack.append(d + b)
            elif c =='-':
                stack.append(d - b)
            elif c == '*':
                stack.append(d * b)
            elif c =='/':
                stack.append(d / b)
    return stack[0]

print(fun(a))