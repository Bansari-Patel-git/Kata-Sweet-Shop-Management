# Kata-Sweet-Shop-Management
# 🍭 Sweet Shop Management System

A simple, beginner-friendly **Sweet Shop Management System** built in **Python** following **Test-Driven Development (TDD)**. The system enables users to manage sweets via a Command-Line Interface (CLI), with operations like adding, deleting, viewing, searching, sorting, purchasing, and restocking sweets.

---

## 📌 Features

- ➕ Add sweets with ID, name, category, price, and quantity
- 🗑️ Delete sweets by ID
- 📋 View all available sweets
- 🔍 Search sweets by name, category, or price range
- 📊 Sort sweets by name, price, or quantity
- 💸 Purchase sweets and reduce stock
- 🔁 Restock sweets
- ✅ Fully tested using `pytest`

---

## 🛠 Technologies Used

- **Python 3.10+**
- **pytest** for unit testing
- **VS Code** (recommended IDE)

---
How to Run the Program 

### ▶ Open VS Code Terminal

Ensure you're in the folder where `main.py` exists.

Then run the following command in your terminal:
```bash
python main.py
```
You’ll see a CLI menu like this:
```bash
====== Sweet Shop Management System ======
1. Add Sweet
2. Delete Sweet
3. View Sweets
4. Search Sweets
5. Sort Sweets
6. Purchase Sweet
7. Restock Sweet
8. Exit
Enter your choice:
```
How to Run Unit Tests
Ensure you're in the project directory and run:
```bash
pytest

```
Expected output:
```bash
=================== test session starts ===================
collected 7 items

test_sweet_shop.py .......

=================== 7 passed in 0.03s ======================
