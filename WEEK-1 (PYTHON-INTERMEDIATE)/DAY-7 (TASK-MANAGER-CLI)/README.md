# 📘 Week 1 — Day 7: Functional Programming — Task Manager CLI

## 🗓️ **100 Days to AI Agent Engineer** — Phase 1: Foundations

---

## 📌 Overview

Today I focused on **functional programming in Python** by building a **Task Manager CLI application**.
I implemented core CRUD operations using **functions and lists of dictionaries**, including adding, viewing, updating, deleting, changing status, and searching tasks.

This day was critical for understanding **function-based program design, data handling with dictionaries, and CLI interaction**, which are essential foundations for Python backend development and real-world scripting.

---

## ✅ What I Accomplished Today

|   | Task                                      | Status    |
| - | ----------------------------------------- | --------- |
| ✓ | Designed a CLI menu for task operations   | Completed |
| ✓ | Implemented task addition using functions | Completed |
| ✓ | Implemented task viewing                  | Completed |
| ✓ | Implemented task updating by title        | Completed |
| ✓ | Implemented task deletion by title        | Completed |
| ✓ | Implemented changing task status          | Completed |
| ✓ | Implemented searching tasks by title      | Completed |

---

## 📚 What I Learned

| Concept              | Explanation                                                              |
| -------------------- | ------------------------------------------------------------------------ |
| **Functions**        | Modular units of code that perform specific tasks                        |
| **Dictionaries**     | Used to store task data with key-value pairs                             |
| **Lists**            | Maintained collection of tasks                                           |
| **CRUD Operations**  | Create, Read, Update, Delete — core application operations               |
| **CLI Interaction**  | Taking user input to select operations and input task details            |
| **For-Else Loops**   | Used in searching and updating tasks with proper task-not-found handling |
| **Input Validation** | Ensured basic validation for numeric inputs like task ID                 |

---

## 🛠️ Hands-On Tasks Performed

---

### Task 1 — CLI Menu Setup

| # | Step           | Description                                                           |
| - | -------------- | --------------------------------------------------------------------- |
| 1 | Menu Options   | Added options: Add, View, Update, Delete, Change Status, Search, Exit |
| 2 | Input Handling | Prompted user to enter a number to select operation                   |
| 3 | Loop Control   | Used `while True` to keep program running until Exit                  |

---

### Task 2 — Add Task

| # | Step                 | Description                              |
| - | -------------------- | ---------------------------------------- |
| 1 | Input Task Details   | ID, Title, Description, Status, Priority |
| 2 | Store Task           | Saved as dictionary in global list `obj` |
| 3 | Confirmation Message | Printed task added successfully          |

---

### Task 3 — View Tasks

| # | Step                | Description                         |
| - | ------------------- | ----------------------------------- |
| 1 | Loop Through Tasks  | Iterated over `obj` list            |
| 2 | Display Information | Printed ID, Title, Status, Priority |
| 3 | Empty List Handling | Added message if no tasks exist     |

---

### Task 4 — Update Task

| # | Step                    | Description                                       |
| - | ----------------------- | ------------------------------------------------- |
| 1 | Search Task by Title    | Compared input with `task['title']`               |
| 2 | Update Details          | Replaced ID, Title, Description, Status, Priority |
| 3 | Task Not Found Handling | Printed message if title not in list              |

---

### Task 5 — Delete Task

| # | Step                    | Description                          |
| - | ----------------------- | ------------------------------------ |
| 1 | Search Task by Title    | Compared input with `task['title']`  |
| 2 | Remove Task             | Used `obj.remove(task)`              |
| 3 | Task Not Found Handling | Printed message if title not in list |

---

### Task 6 — Change Task Status

| # | Step                    | Description                          |
| - | ----------------------- | ------------------------------------ |
| 1 | Search Task by Title    | Compared input with `task['title']`  |
| 2 | Update Status           | Set `task['status'] = "Completed"`   |
| 3 | Task Not Found Handling | Printed message if title not in list |

---

### Task 7 — Search Task by Title

| # | Step                    | Description                            |
| - | ----------------------- | -------------------------------------- |
| 1 | Input Task Title        | Asked user for task title to search    |
| 2 | Display Task            | Printed task details if found          |
| 3 | Task Not Found Handling | Printed message if task does not exist |

---

## 💡 Key Takeaways

| Takeaway                      | Why It Matters                                          |
| ----------------------------- | ------------------------------------------------------- |
| **Functional Programming**    | Modular, reusable functions simplify code management    |
| **Dictionary & List Usage**   | Efficient way to store and access task data             |
| **CRUD Fundamentals**         | Core skill for backend applications and data management |
| **CLI Interaction**           | Builds interactive scripts without GUI                  |
| **For-Else & Input Handling** | Ensures robust logic and user-friendly error messages   |

---

## 🔍 Challenges & Solutions

| Challenge                                              | Solution                                                    |
| ------------------------------------------------------ | ----------------------------------------------------------- |
| Updating/deleting tasks without removing actual object | Used `obj.remove(task)` instead of `del task`               |
| Searching for task by title correctly                  | Compared `task['title']` instead of `title in task`         |
| Handling non-existent tasks                            | Added proper for-else structure with messages               |
| Avoiding duplicate task updates                        | Updated dictionary directly instead of deleting + appending |

---

## 🎯 Why This Matters for AI Agent Engineering

| Today's Learning              | Future Application                                           |
| ----------------------------- | ------------------------------------------------------------ |
| Functional Programming        | Foundation for building modular, maintainable Python scripts |
| CRUD Operations               | Essential for backend systems and data handling              |
| Data Structures (List & Dict) | Core for storing and manipulating structured data            |
| CLI Interaction               | Enables development of small automation and utility scripts  |

---

## 📊 Progress Tracker

| Phase | Week | Day   | Focus Area                 | Status     |
| ----- | ---- | ----- | -------------------------- | ---------- |
| 1/5   | 1/15 | 7/100 | Functional Programming CLI | ✅ Complete |

---

## 💭 Reflection

Week 1, Day 7 is complete!

Today I successfully implemented a **fully functional Task Manager** using **Python functions and data structures**.
I strengthened my understanding of **functions, dictionaries, lists, loops, and CLI interaction**, and learned practical **CRUD operations** applicable in real-world backend and scripting projects.

**Functional programming provides clarity and modularity, even before moving to OOP.** 🚀
