"""Task 1 — Basic Queue Operations

Create a queue (using deque).
Enqueue 5 integers entered by the user.
Dequeue 2 elements.
Print the front element and the size of the queue.
Print the final queue.

Goal: Practice enqueue, dequeue, peek, and size."""

from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

queue.popleft()
queue.popleft()

print(f"the first element is : {queue[0]} The size of the queue is : {len(queue)}")

print(list(queue))
