# 📘 Week 1 — Day 4: Exception Handling — Robust & Secure Programs

## 🗓️ **100 Days to AI Agent Engineer** — Phase 1: Foundations

---

## 📌 Overview

Today I focused on **exception handling in Python**. I practiced handling runtime errors, preventing program crashes, creating custom exceptions, and implementing retry logic similar to real authentication systems.

This strengthened my understanding of **error handling, validation logic, program flow control, and defensive programming**, which are essential for building secure and production-ready applications.

---

## ✅ What I Accomplished Today

|   | Task                                       | Status    |
| - | ------------------------------------------ | --------- |
| ✓ | Task 1 — Safe Division with Error Handling | Completed |
| ✓ | Task 2 — Handling Index & Input Errors     | Completed |
| ✓ | Task 3 — File Handling with Exceptions     | Completed |
| ✓ | Task 4 — Custom Age Validation Exceptions  | Completed |
| ✓ | Task 5 — Password Retry Logic (3 Attempts) | Completed |

---

## 📚 What I Learned

| Concept                 | Application                                          |
| ----------------------- | ---------------------------------------------------- |
| **try / except**        | Catching runtime errors without crashing the program |
| **Multiple Exceptions** | Handling different error types separately            |
| **finally Block**       | Executing cleanup code regardless of error           |
| **else Block**          | Running code only when no exception occurs           |
| **raise Keyword**       | Manually triggering exceptions                       |
| **Custom Exceptions**   | Creating domain-specific error classes               |
| **Retry Logic**         | Limiting user attempts in authentication systems     |
| **Input Validation**    | Preventing invalid data from entering the system     |

---

## 🛠️ Projects & Tasks

### Task 1 — Safe Division Program

| # | Feature                   | Description                                  |
| - | ------------------------- | -------------------------------------------- |
| 1 | **User Input**            | Accept two numbers                           |
| 2 | **ZeroDivision Handling** | Catch division by zero                       |
| 3 | **ValueError Handling**   | Catch non-numeric input                      |
| 4 | **finally Block**         | Print completion message regardless of error |

---

### Task 2 — Index Access with Error Handling

| # | Feature                 | Description                              |
| - | ----------------------- | ---------------------------------------- |
| 1 | **List Access**         | Retrieve value using user-provided index |
| 2 | **IndexError Handling** | Prevent crash for invalid index          |
| 3 | **ValueError Handling** | Handle invalid numeric input             |

---

### Task 3 — File Reader with Exception Handling

| # | Feature               | Description                               |
| - | --------------------- | ----------------------------------------- |
| 1 | **File Input**        | Ask user for filename                     |
| 2 | **FileNotFoundError** | Handle missing file                       |
| 3 | **PermissionError**   | Handle restricted file access             |
| 4 | **Generic Exception** | Catch unexpected errors                   |
| 5 | **else Usage**        | Print content only if no exception occurs |

---

### Task 4 — Custom Age Validation (Custom Exceptions)

| # | Feature                    | Description                           |
| - | -------------------------- | ------------------------------------- |
| 1 | **Custom Exception Class** | Created age-related exception classes |
| 2 | **raise Usage**            | Trigger error for invalid age         |
| 3 | **Validation Rules**       | Age > 0 and Age < 120                 |
| 4 | **ValueError Handling**    | Prevent crash for non-numeric input   |

---

### Task 5 — Password Retry Logic (Authentication Simulation)

| # | Feature              | Description                            |
| - | -------------------- | -------------------------------------- |
| 1 | **3 Attempt Limit**  | Restrict login attempts                |
| 2 | **Loop Control**     | Decrease attempts after wrong password |
| 3 | **Break on Success** | Stop loop when password is correct     |
| 4 | **Raise Exception**  | Lock account after 3 failed attempts   |

---

## 💡 Key Takeaways

| Takeaway                      | Why It Matters                                          |
| ----------------------------- | ------------------------------------------------------- |
| **Defensive Programming**     | Makes applications secure and stable                    |
| **Custom Exceptions**         | Helps create meaningful, domain-specific error handling |
| **Input Validation**          | Prevents invalid data from corrupting system logic      |
| **Retry Mechanisms**          | Used in real-world authentication systems               |
| **Structured Error Handling** | Essential for APIs, backend services, and AI workflows  |

---

## 🔍 Challenges & Solutions

| Challenge                                 | Solution                                  |
| ----------------------------------------- | ----------------------------------------- |
| Handling input errors before try block    | Moved input conversion inside `try` block |
| Index errors not triggering               | Accessed list directly using user index   |
| File variable mistake (`'file_name'`)     | Used variable instead of string literal   |
| Preventing program crash after 3 attempts | Used loop + manual `raise Exception()`    |
| Designing custom validation errors        | Created custom exception classes          |

---

## 🎯 Why This Matters for AI Agent Engineering

| Today's Learning    | Future Application                               |
| ------------------- | ------------------------------------------------ |
| Exception Handling  | Preventing AI systems from crashing on bad input |
| Custom Exceptions   | Handling domain-specific validation logic        |
| Retry Logic         | Authentication & access control in AI tools      |
| File Error Handling | Managing logs, datasets, and configuration files |
| Input Validation    | Secure API and chatbot input filtering           |

---

## 📊 Progress Tracker

| Phase | Week | Day   | Focus Area         | Status     |
| ----- | ---- | ----- | ------------------ | ---------- |
| 1/5   | 1/15 | 4/100 | Exception Handling | ✅ Complete |

---

## 💭 Reflection

Week 1, Day 4 is complete!

Today I learned how to make programs **resilient, secure, and production-ready** by handling errors properly. I practiced built-in exceptions, custom exceptions, validation logic, and authentication-style retry systems.

I am now building programs that don't just work — they **fail safely and intelligently**.

**Strong foundations create powerful engineers.** 🚀

---

## 🔗 Journey Details

|                |                                        |
| -------------- | -------------------------------------- |
| **Journey**    | 100 Days to AI Agent Engineer          |
| **Phase**      | 1/5 — Foundations                      |
| **Week**       | 1 — Python Basics & Core Concepts      |
| **Day**        | 4/100                                  |
| **Next Topic** | Loops, Functions & Structured Programs |

---

*"Errors are not failures — they are feedback for better systems."*