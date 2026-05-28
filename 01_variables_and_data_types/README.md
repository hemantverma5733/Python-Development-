# 01. Variables and Data Types

This project covers the absolute building blocks of Python programming: **Variables** and **Data Types**.

---

## 💡 What is a Variable?
A variable is a named storage location in your computer's memory where you can store data that your program can manipulate.
* Think of it as a labeled box where you put values.
* Python variables are created the moment you assign a value to them using the `=` symbol.

---

## 📊 Core Data Types in Python

In Python, every value has a data type. Here are the primary ones you will work with:

### 1. Primitive Types
* **Integer (`int`):** Whole numbers without a decimal point. Example: `age = 22`
* **Float (`float`):** Decimal or floating-point numbers. Example: `price = 19.99`
* **String (`str`):** Text wrapped in single or double quotes. Example: `name = "Hemant"`
* **Boolean (`bool`):** True or False values. Example: `is_active = True`
* **NoneType (`None`):** Represents the absence of a value. Example: `result = None`

### 2. Collection Types
* **List (`list`):** Ordered, mutable (changeable), and allows duplicates. Used for lists of items. Example: `fruits = ["apple", "banana"]`
* **Tuple (`tuple`):** Ordered, immutable (cannot be changed after creation). Example: `coords = (12.34, 56.78)`
* **Dictionary (`dict`):** Key-value pairs. Highly efficient for looking up data. Example: `user = {"name": "Hemant", "age": 22}`
* **Set (`set`):** Unordered collection of unique items. Duplicates are auto-removed. Example: `unique_numbers = {1, 2, 3}`

---

## ⚡ How to Run the Script

Navigate to this project's directory and run the script using Python:

```bash
python3 variables_demo.py
```

---

## 🧠 Key Takeaways
1. **Dynamic Typing:** Python automatically detects the type of variable at runtime. You don't need to write `int age = 22`.
2. **Type Checking:** You can inspect any variable's type using the built-in `type()` function.
3. **Casting:** You can convert variables between types using conversion functions like `str()`, `int()`, `float()`, `list()`, etc.
