# 📘 Week 1 — Day 3: File Handling — User Data Management

## 🗓️ **100 Days to AI Agent Engineer** — Phase 1: Foundations

---

## 📌 Overview

Today I focused on **practical file handling in Python**. I applied my learning to implement **user data management operations** — creating, reading, searching, and deleting user records in a file.

This strengthened my **problem-solving skills, file handling, string parsing, exception handling, and list manipulation**, laying a foundation for real-world Python projects that involve persistent data storage.

---

## ✅ What I Accomplished Today

|   | Task                                 | Status    |
| - | ------------------------------------ | --------- |
| ✓ | Task 1 — Basic File Writing          | Completed |
| ✓ | Task 2 — File Reading                | Completed |
| ✓ | Task 3 — Search in File              | Completed |
| ✓ | Task 4 — Delete a User (Challenging) | Completed |

---

## 📚 What I Learned

| Concept                | Application                                         |
| ---------------------- | --------------------------------------------------- |
| **File Modes**         | `'r'`, `'w'`, `'a'` for reading, writing, appending |
| **Exception Handling** | `try-except` to catch `FileNotFoundError`           |
| **String Parsing**     | Splitting file content into lines and records       |
| **List Manipulation**  | Storing records in lists for filtering or deletion  |
| **Conditional Checks** | Searching for specific data in file                 |
| **Rewriting Files**    | Updating files after modifying content              |
| **Data Formatting**    | Storing user info with proper separators            |

---

## 🛠️ Projects & Tasks

### Task 1 — Basic File Writing

| # | Feature           | Description                              |
| - | ----------------- | ---------------------------------------- |
| 1 | **User Input**    | Ask for Name, Age, City                  |
| 2 | **Write to File** | Append user data to `users.txt`          |
| 3 | **Formatting**    | Each record separated by lines or dashes |

---

### Task 2 — File Reading

| # | Feature             | Description                                     |
| - | ------------------- | ----------------------------------------------- |
| 1 | **Read File**       | Open `users.txt` in read mode                   |
| 2 | **Display Content** | Print user records                              |
| 3 | **Error Handling**  | Catch `FileNotFoundError` if file doesn't exist |

---

### Task 3 — Search in File

| # | Feature          | Description                                             |
| - | ---------------- | ------------------------------------------------------- |
| 1 | **Input Name**   | Ask user to enter the name to search                    |
| 2 | **Search Logic** | Check each record for the matching name                 |
| 3 | **Output**       | Print full record if found; else print "User not found" |

---

### Task 4 — Delete a User (Challenging)

| # | Feature           | Description                               |
| - | ----------------- | ----------------------------------------- |
| 1 | **Read All Data** | Store each record in a list               |
| 2 | **Filter Record** | Skip the record that matches the name     |
| 3 | **Rewrite File**  | Update `users.txt` with remaining records |
| 4 | **Output Result** | Confirm deletion or show "User not found" |

---

## 💡 Key Takeaways

| Takeaway                     | Why It Matters                                                                  |
| ---------------------------- | ------------------------------------------------------------------------------- |
| **File Handling Mastery**    | Essential for data persistence in Python applications                           |
| **Exception Handling**       | Prevents crashes when files are missing or inaccessible                         |
| **List & String Operations** | Crucial for filtering, searching, and updating file content                     |
| **Data Formatting**          | Ensures readability and proper record separation                                |
| **Step-by-Step Logic**       | Reading → Processing → Writing workflow is foundational for real-world projects |

---

## 🔍 Challenges & Solutions

| Challenge                                  | Solution                                                           |
| ------------------------------------------ | ------------------------------------------------------------------ |
| File not found                             | Used `try-except` block with `FileNotFoundError`                   |
| Searching specific user in a file          | Checked `f"name:{user_name}"` in each line                         |
| Deleting a record from file                | Stored records in a list, skipped the matched record, rewrote file |
| Maintaining formatting when rewriting file | Added newline `\n` after each line                                 |

---

## 🎯 Why This Matters for AI Agent Engineering

| Today's Learning              | Future Application                                |
| ----------------------------- | ------------------------------------------------- |
| Reading/Writing Files         | Storing and retrieving AI agent logs or user data |
| Searching & Filtering Records | Implementing search functions in agent interfaces |
| Conditional Logic & Loops     | Handling workflow decisions in Python scripts     |
| List Manipulation             | Updating and maintaining structured data          |
| Exception Handling            | Making robust applications resilient to errors    |

---

## 📊 Progress Tracker

| Phase | Week | Day   | Focus Area              | Status     |
| ----- | ---- | ----- | ----------------------- | ---------- |
| 1/5   | 1/15 | 3/100 | File Handling in Python | ✅ Complete |

---

## 💭 Reflection

Week 1, Day 3 is complete! I successfully built a **file-based user management system** using Python. This project reinforced my understanding of **reading, writing, searching, and deleting records**, while teaching me the importance of **data formatting and error handling**.

**Progress, not perfection.** 🚀

---

## 🔗 Journey Details

|                |                                            |
| -------------- | ------------------------------------------ |
| **Journey**    | 100 Days to AI Agent Engineer              |
| **Phase**      | 1/5 — Foundations                          |
| **Week**       | 1 — Python Basics & DSA Fundamentals       |
| **Day**        | 3/100                                      |
| **Next Topic** | Loops, Conditional Logic & File Operations |

---

*"The expert in anything was once a beginner. Every master was once a disaster. Keep going."*