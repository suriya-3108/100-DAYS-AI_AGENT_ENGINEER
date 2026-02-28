"""Practice Question 2 — Balanced Parentheses
Problem:
Given a string containing only these characters: (, ), {, }, [, ]
Check if the parentheses are balanced.

Balanced means:
Every opening bracket has a corresponding closing bracket.
Brackets are closed in the correct order.

Examples:
"()"        → Balanced
"({[]})"    → Balanced
"([)]"      → Not Balanced
"((("       → Not Balanced"""

def check_bracket(s):
    stack = []
    brackets = {')':'(', '}':'{', ']':'['}
    
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return "not balanced"
            if stack.pop() != brackets[char]:
                return "not balanced"
    
    return "not balanced" if stack else "balanced"

s = '({[]})'
res = check_bracket(s)
print(res)