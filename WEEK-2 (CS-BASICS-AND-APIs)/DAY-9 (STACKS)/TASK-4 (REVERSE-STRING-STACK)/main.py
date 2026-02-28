"""Question 4 — Reverse a String Using Stack
Problem:
Given a string, reverse it using a stack (do not use slicing like [::-1] — we want to practice stacks).
Example:

Input: "hello"
Output: "olleh"

Input: "AIStack"
Output: "kcatSIA" """

s = 'hello'

def calc(s):
    stack = []
    for char in s:
        stack.append(char)
    
    c = ''
    while stack:
        c += stack.pop()
    return c

print(calc(s))

