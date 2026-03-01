# 📘 **DAY 10: Queues — Understanding FIFO Data Structures**

## 🗓️ **100 Days to AI Agent Engineer** — Phase 1: Foundations

---

## 📌 Overview

Today I learned about **Queues**, a fundamental **First-In-First-Out (FIFO) data structure**. Queues are essential for managing **ordered tasks, job scheduling, and real-world scenarios like printer queues**.

I practiced:

* Basic queue operations (enqueue, dequeue, peek, check empty)
* Reversing the first `k` elements of a queue
* Simulating a **printer/task manager application** using a queue

This day helped me understand how **FIFO logic** is applied in practical problems and algorithm design.

---

## ✅ What I Accomplished Today

|   | Task                                     | Status    |
| - | ---------------------------------------- | --------- |
| ✓ | Implemented basic queue operations       | Completed |
| ✓ | Reversed first k elements in a queue     | Completed |
| ✓ | Built a printer/task manager application | Completed |

---

## 📚 What I Learned

| Concept                      | Explanation                                                                                  |
| ---------------------------- | -------------------------------------------------------------------------------------------- |
| **Queue**                    | A data structure that follows **First-In-First-Out (FIFO)**                                  |
| **Enqueue**                  | Add an element to the rear of the queue                                                      |
| **Dequeue**                  | Remove the element from the front of the queue                                               |
| **Peek / Front**             | View the front element without removing it                                                   |
| **isEmpty**                  | Check if the queue has no elements                                                           |
| **Reverse First K Elements** | Reverse the first `k` elements in a queue while keeping the rest in order                    |
| **Printer/Task Manager App** | Simulate real-world task handling using queues (add tasks, update process, remove completed) |

---

## 💡 Key Takeaways

| Takeaway                          | Why It Matters                                                  |
| --------------------------------- | --------------------------------------------------------------- |
| **Queues are FIFO**               | Useful in scheduling, task management, and ordered processing   |
| **Front and rear operations**     | Core queue logic depends on adding/removing elements properly   |
| **Reversing queue segments**      | Shows how to manipulate queue elements while maintaining order  |
| **Real-world queue applications** | Practice in printer jobs, task management, and process tracking |

---

## 🔍 Challenges & Solutions

| Challenge                                | Solution                                                             |
| ---------------------------------------- | -------------------------------------------------------------------- |
| Reversing only part of the queue         | Slice the first `k` elements, reverse, and concatenate with the rest |
| Removing items during iteration          | Iterate over a copy or use a while-loop to avoid `RuntimeError`      |
| Tracking completed tasks in a queue      | Use a field like `PROCESS` and safely remove completed items         |
| Ensuring queue updates display correctly | Always display queue after each operation to verify correctness      |

---

## 🎯 Why This Matters for AI Agent Engineering

| Today's Learning                            | Future Application                                       |
| ------------------------------------------- | -------------------------------------------------------- |
| Using queues to manage ordered tasks        | Task scheduling, job processing, and event handling      |
| Reversing parts of a queue                  | Data manipulation, algorithm design, and problem-solving |
| Real-world queue simulation                 | Printer queue, task manager apps, and priority handling  |
| Safe modification of queue during iteration | Prevent runtime errors, maintain data integrity          |

---

## 📊 Progress Tracker

| Phase | Week | Day    | Focus Area    | Status     |
| ----- | ---- | ------ | ------------- | ---------- |
| 1/5   | 2/15 | 10/100 | Queues (FIFO) | ✅ Complete |

---

## 💭 Reflection

Today I learned **Queues** and applied FIFO logic in **practical scenarios**. I practiced **basic operations**, **reversing segments**, and built a **task manager/printer queue simulation**.

The key insight is that queues are **simple but extremely useful** for **ordered processing and task management**, forming the backbone of scheduling algorithms and real-world applications.

**Today I realized that proper management of front/rear elements and careful iteration makes queues reliable and versatile!** 🚀

---

## 🔗 Journey Details

|                |                               |
| -------------- | ----------------------------- |
| **Journey**    | 100 Days to AI Agent Engineer |
| **Phase**      | 1/5 — Foundations             |
| **Week**       | 2 — CS Basics & APIs          |
| **Day**        | 10/100                        |
| **Next Topic** | Queue Variants & Deques       |

---

*"First in, first out — mastering order is the key."* 💡