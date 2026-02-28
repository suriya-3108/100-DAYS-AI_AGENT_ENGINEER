"""Practice Question 1 — Basic Stack Operations

Create an empty stack.
Push the numbers: 5, 10, 15, 20, 25 into the stack (in that order).
Pop two elements from the stack.

Print:
The current top element of the stack
Whether the stack is empty or not"""

# Stack by using deque

from collections import deque

stack = deque()

stack.append(5)
stack.append(10)
stack.append(15)
stack.append(20)
stack.append(25)

stack.pop()
stack.pop()

top = -1

print(stack[top])

if len(stack) > 0:
    print("not empty")
else:
    print("empty")

