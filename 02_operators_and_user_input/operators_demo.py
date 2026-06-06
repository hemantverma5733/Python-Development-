# 🐍 Python Operators & User Input Demo
# Topic 02: Foundational Python (Day 2)

def print_separator(title):
    """
    Helper function to print a neat separator for different sections.
    Makes terminal output clean and readable.
    """
    print("\n" + "=" * 50)
    print(f"🔹 {title} 🔹")
    print("=" * 50)

def main():
    print("🚀 Welcome to Day 2: Operators & User Input Exploration! 🚀")

    # ==========================================
    # 1. ARITHMETIC OPERATORS
    # ==========================================
    print_separator("1. Arithmetic Operators")
    
    # Defining two base variables for arithmetic operations
    a = 15
    b = 4
    print(f"Base numbers: a = {a}, b = {b}\n")
    
    # Addition (+)
    sum_result = a + b
    print(f"Addition (a + b)         : {a} + {b} = {sum_result}")
    
    # Subtraction (-)
    diff_result = a - b
    print(f"Subtraction (a - b)      : {a} - {b} = {diff_result}")
    
    # Multiplication (*)
    prod_result = a * b
    print(f"Multiplication (a * b)   : {a} * {b} = {prod_result}")
    
    # Division (/) - Always returns a float in Python 3
    div_result = a / b
    print(f"Division (a / b)         : {a} / {b} = {div_result}  (Result is float)")
    
    # Floor Division (//) - Divides and rounds down to the nearest whole integer
    floor_div_result = a // b
    print(f"Floor Division (a // b)  : {a} // {b} = {floor_div_result}  (Discards decimal part)")
    
    # Modulus (%) - Returns the remainder of the division
    mod_result = a % b
    print(f"Modulus/Remainder (a % b): {a} % {b} = {mod_result}  (What is left over after dividing)")
    
    # Exponentiation (**) - Power operation (a raised to the power b)
    power_result = a ** b
    print(f"Exponentiation (a ** b)  : {a} ** {b} = {power_result}  ({a} raised to the power of {b})")


    # ==========================================
    # 2. COMPARISON (RELATIONAL) OPERATORS
    # ==========================================
    print_separator("2. Comparison Operators")
    
    # Comparison operators always return a boolean (True or False)
    x = 10
    y = 20
    print(f"Comparing: x = {x}, y = {y}\n")
    
    # Equal to (==)
    print(f"Is x equal to y? (x == y)          : {x == y}")
    
    # Not equal to (!=)
    print(f"Is x not equal to y? (x != y)      : {x != y}")
    
    # Greater than (>)
    print(f"Is x greater than y? (x > y)       : {x > y}")
    
    # Less than (<)
    print(f"Is x less than y? (x < y)          : {x < y}")
    
    # Greater than or equal to (>=)
    print(f"Is x greater/equal to y? (x >= y)  : {x >= y}")
    
    # Less than or equal to (<=)
    print(f"Is x less/equal to y? (x <= y)     : {x <= y}")


    # ==========================================
    # 3. LOGICAL OPERATORS
    # ==========================================
    print_separator("3. Logical Operators")
    
    # Logical operators are used to combine conditional statements
    has_high_score = True
    has_good_conduct = False
    
    print(f"Conditions: High Score = {has_high_score}, Good Conduct = {has_good_conduct}\n")
    
    # Logical AND (returns True if BOTH conditions are True)
    # Both must be True for the overall expression to be True
    and_result = has_high_score and has_good_conduct
    print(f"AND Operator (High Score and Good Conduct): {and_result}")
    
    # Logical OR (returns True if AT LEAST ONE condition is True)
    or_result = has_high_score or has_good_conduct
    print(f"OR Operator (High Score or Good Conduct)  : {or_result}")
    
    # Logical NOT (reverses/negates the boolean result)
    not_result = not has_high_score
    print(f"NOT Operator (not High Score)             : {not_result} (reverses True to False)")


    # ==========================================
    # 4. ASSIGNMENT OPERATORS
    # ==========================================
    print_separator("4. Assignment Operators")
    
    # Used to assign values to variables, often combined with arithmetic operators
    num = 10
    print(f"Initial Value of num: {num}")
    
    # Simple assignment (=)
    # Add and assign (+=)
    num += 5  # Equivalent to: num = num + 5
    print(f"After num += 5      : {num}")
    
    # Subtract and assign (-=)
    num -= 3  # Equivalent to: num = num - 3
    print(f"After num -= 3      : {num}")
    
    # Multiply and assign (*=)
    num *= 2  # Equivalent to: num = num * 2
    print(f"After num *= 2      : {num}")
    
    # Divide and assign (/=)
    num /= 4  # Equivalent to: num = num / 4
    print(f"After num /= 4      : {num}  (Converted to float due to division)")


    # ==========================================
    # 5. DYNAMIC USER INPUT & CASTING
    # ==========================================
    print_separator("5. User Input & Casting (Interactive)")
    
    print("Now let's build a simple custom calculator using your input!")
    
    # The input() function always reads data as a String (str)
    num1_str = input("Enter the first number: ")
    num2_str = input("Enter the second number: ")
    
    # Let's see what happens if we don't convert them (string concatenation)
    string_concat = num1_str + num2_str
    print(f"\n⚠️ Without Casting (String Concatenation): '{num1_str}' + '{num2_str}' = '{string_concat}'")
    
    # To perform arithmetic, we must CAST (convert) the strings into float or integer
    try:
        # float() converts string to decimal number
        number1 = float(num1_str)
        number2 = float(num2_str)
        
        print(f"\n✅ Successfully casted inputs to float! Performing calculations:")
        print(f"Addition       : {number1} + {number2} = {number1 + number2}")
        print(f"Subtraction    : {number1} - {number2} = {number1 - number2}")
        print(f"Multiplication : {number1} * {number2} = {number1 * number2}")
        
        # Division requires caution to avoid DivisionByZero error
        if number2 != 0:
            print(f"Division       : {number1} / {number2} = {number1 / number2}")
        else:
            print("Division       : Cannot divide by zero!")
            
    except ValueError:
        print("\n❌ Error: Please enter valid numbers! Casting failed.")

    print("\n🎉 Excellent! Day 2 of Python concepts (Operators & Input) is complete! 🎉\n")

if __name__ == "__main__":
    main()
