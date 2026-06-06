# 02. Operators and User Input in Python

Welcome to Day 2 of Python Development! This guide covers **Operators** (Arithmetic, Comparison, Logical, Assignment) and **User Input & Casting**. It explains the concepts, key definitions, and provides a line-by-line breakdown of [operators_demo.py](file:///Users/hemantverma/Desktop/All%20projects/python%20Development/02_operators_and_user_input/operators_demo.py).

---

## 📚 Important Definitions

Before we dive into the code, let's understand the core terms:

1. **Operator (ऑपरेटर):** A symbol that performs an operation on one or more values. For example, `+` is an addition operator.
2. **Operand (ऑपरेंड):** The data or variables on which the operator acts. In `15 + 4`, the numbers `15` and `4` are operands, and `+` is the operator.
3. **Arithmetic Operators:** Operators used to perform mathematical calculations (like addition, subtraction, division, modulus, and powers).
4. **Comparison (Relational) Operators:** Operators used to compare two values. They return a Boolean value (`True` or `False`).
5. **Logical Operators:** Used to combine conditional statements (`and`, `or`, `not`).
6. **Assignment Operators:** Used to assign values to variables (e.g., `=` assigns, `+=` adds and assigns, etc.).
7. **User Input (`input()`):** A built-in Python function that pauses program execution and waits for the user to type text in the terminal and press Enter.
8. **Type Casting (टाइप कास्टिंग):** The process of converting a value from one data type to another (e.g., converting a string `"22"` to an integer `22`).

---

## 🔍 Line-by-Line Code Explanation of `operators_demo.py`

Let's break down [operators_demo.py](file:///Users/hemantverma/Desktop/All%20projects/python%20Development/02_operators_and_user_input/operators_demo.py) line-by-line:

### 1. General Setup & Helper Function

* **Lines 1-2:**
  ```python
  # 🐍 Python Operators & User Input Demo
  # Topic 02: Foundational Python (Day 2)
  ```
  * *Explanation:* Single-line comments starting with `#`. Python ignores these lines; they are only for human documentation.

* **Lines 4-10:**
  ```python
  def print_separator(title):
      """
      Helper function to print a neat separator for different sections.
      Makes terminal output clean and readable.
      """
      print("\n" + "=" * 50)
      print(f"🔹 {title} 🔹")
      print("=" * 50)
  ```
  * *Explanation:* 
    * `def print_separator(title):` declares a custom function named `print_separator` that accepts one argument: `title`.
    * The text inside triple quotes `"""..."""` is a **docstring** (documentation string) explaining what the function does.
    * `print("\n" + "=" * 50)` prints a newline (`\n`) followed by the `=` character repeated 50 times (string multiplication).
    * `print(f"🔹 {title} 🔹")` uses an **f-string** (formatted string literal) to print the title parameter between two emojis.
    * `print("=" * 50)` prints another separating line of 50 equals signs.

---

### 2. The `main` Function & Arithmetic Operators

* **Lines 12-19:**
  ```python
  def main():
      print("🚀 Welcome to Day 2: Operators & User Input Exploration! 🚀")

      # ==========================================
      # 1. ARITHMETIC OPERATORS
      # ==========================================
      print_separator("1. Arithmetic Operators")
      
      # Defining two base variables for arithmetic operations
      a = 15
      b = 4
  ```
  * *Explanation:*
    * `def main():` defines our main program controller function.
    * `a = 15` creates a variable `a` and assigns it the integer value `15`.
    * `b = 4` creates a variable `b` and assigns it the integer value `4`.

* **Lines 22-41: Calculations & Output:**
  * `sum_result = a + b`: The `+` operator adds `a` and `b`. `sum_result` becomes `19`.
  * `diff_result = a - b`: The `-` operator subtracts `b` from `a`. `diff_result` becomes `11`.
  * `prod_result = a * b`: The `*` operator multiplies `a` and `b`. `prod_result` becomes `60`.
  * `div_result = a / b`: The `/` operator performs division. In Python 3, `/` always returns a `float` (decimal). `div_result` becomes `3.75`.
  * `floor_div_result = a // b`: The `//` operator performs **floor division** (rounds down the result to the nearest integer). `15 // 4` is `3` (discarding the `.75`).
  * `mod_result = a % b`: The `%` operator performs **modulus** (calculates the remainder). `15 / 4` is `3` with a remainder of `3`. So `mod_result` is `3`.
  * `power_result = a ** b`: The `**` operator raises `a` to the power of `b` ($15^4$). `power_result` is `50625`.

---

### 3. Comparison Operators

* **Lines 44-70:**
  ```python
  x = 10
  y = 20
  ```
  * *Explanation:*
    * `x == y`: Returns `True` if `x` is equal to `y`. Since `10 == 20` is false, it returns `False`.
    * `x != y`: Returns `True` if `x` is **not** equal to `y`. Since `10` is indeed not equal to `20`, it returns `True`.
    * `x > y`: Checks if `x` is greater than `y`. Returns `False`.
    * `x < y`: Checks if `x` is less than `y`. Returns `True`.
    * `x >= y`: Checks if `x` is greater than or equal to `y`. Returns `False`.
    * `x <= y`: Checks if `x` is less than or equal to `y`. Returns `True`.

---

### 4. Logical Operators

* **Lines 73-95:**
  ```python
  has_high_score = True
  has_good_conduct = False
  ```
  * *Explanation:*
    * `and_result = has_high_score and has_good_conduct`: The `and` operator returns `True` **only if both** operands are `True`. Since one is `False`, the result is `False`.
    * `or_result = has_high_score or has_good_conduct`: The `or` operator returns `True` if **at least one** operand is `True`. Since `has_high_score` is `True`, the result is `True`.
    * `not_result = not has_high_score`: The `not` operator negates/reverses the Boolean. `not True` becomes `False`.

---

### 5. Assignment Operators

* **Lines 98-121:**
  ```python
  num = 10
  ```
  * *Explanation:*
    * `num += 5` is a shorthand for `num = num + 5`. `num` changes from `10` to `15`.
    * `num -= 3` is a shorthand for `num = num - 3`. `num` changes from `15` to `12`.
    * `num *= 2` is a shorthand for `num = num * 2`. `num` changes from `12` to `24`.
    * `num /= 4` is a shorthand for `num = num / 4`. `num` changes from `24` to `6.0` (as division changes the type to a floating-point number).

---

### 6. User Input & Type Casting

* **Lines 124-154:**
  ```python
  num1_str = input("Enter the first number: ")
  num2_str = input("Enter the second number: ")
  ```
  * *Explanation:*
    * `input(...)` prints the prompt text in the console and waits for the user to type something. Whatever the user types is captured as a **string** (`str`), even if they typed numbers!
    * `string_concat = num1_str + num2_str`: If we use `+` on two strings, Python performs **concatenation** (joins them together). For example, if you enter `5` and `3`, it joins them to make `"53"`.
    * To do real addition, we must **cast** them:
      ```python
      try:
          number1 = float(num1_str)
          number2 = float(num2_str)
      ```
      * `try:` initiates an exception handling block.
      * `float(num1_str)` converts the string representation of the number (e.g. `"5.5"`) to a floating-point number (`5.5`).
      * If the user enters a non-numeric string (e.g. `"hello"`), Python throws a `ValueError`. The program jumps to the `except ValueError:` block to prevent a crash:
        ```python
        except ValueError:
            print("\n❌ Error: Please enter valid numbers! Casting failed.")
        ```
    * `if number2 != 0:`: Before performing division (`number1 / number2`), we check if the second number is not zero. If it is zero, division is impossible, so we output an error message instead of letting the program crash.

---

### 7. Running the Script

* **Lines 156-157:**
  ```python
  if __name__ == "__main__":
      main()
  ```
  * *Explanation:* This is a standard Python boilerplate code. It checks if the script is being run directly by Python (instead of being imported as a module by another script). If run directly, it executes the `main()` function.

---

## ⚡ Running the Script

Navigate to this directory in your terminal and run:

```bash
python3 operators_demo.py
```
This will run the interactive demo, prompting you for numbers and calculating results dynamically!
