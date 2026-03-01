"""Task 2 — Reverse First K Elements
Given a queue of integers and a number k, reverse the first k elements of the queue.

Example:
Queue: 1 2 3 4 5 6 7
k = 3
Output: 3 2 1 4 5 6 7

Goal: Practice manipulating queue elements."""

from collections import deque

queue = deque()

queue = [1,2,3,4,5,6,7]

k = 3

rev_queue = queue[:k]

rev_queue.reverse()

result = rev_queue + queue[k:]

print(result)