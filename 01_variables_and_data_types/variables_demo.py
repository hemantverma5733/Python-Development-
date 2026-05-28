# 🐍 Python variables & Data Types Demo
# Topic 01: Foundational Python

def print_separator(title):
    print("\n" + "=" * 50)
    print(f"🔹 {title} 🔹")
    print("=" * 50)

def main():
    print("🚀 Starting the Variables and Data Types Exploration! 🚀")

    # ==========================================
    # 1. VARIABLE DECLARATION & NAMING CONVENTIONS
    # ==========================================
    print_separator("1. Variables Declaration")
    
    # Python is dynamically typed (no need to declare variable types explicitly)
    user_name = "Hemant Verma"  # Snake case is standard for variable names in Python
    age = 22
    is_learning = True
    
    print(f"User Name (str) : {user_name}")
    print(f"Age (int)       : {age}")
    # f-strings (formatted strings) make combining variables and strings very easy
    print(f"Is Learning?    : {is_learning}")

    # ==========================================
    # 2. PRIMITIVE DATA TYPES
    # ==========================================
    print_separator("2. Primitive Data Types")

    # Integer (Whole numbers)
    score = 98
    # Float (Decimal numbers)
    pi_value = 3.14159
    # String (Text sequences)
    greeting = "Hello, Python World!"
    # Boolean (True or False)
    has_completed_milestone = False
    # NoneType (Represents the absence of a value)
    empty_value = None

    print(f"Score      : {score} | Type: {type(score)}")
    print(f"Pi Value   : {pi_value} | Type: {type(pi_value)}")
    print(f"Greeting   : {greeting} | Type: {type(greeting)}")
    print(f"Milestone  : {has_completed_milestone} | Type: {type(has_completed_milestone)}")
    print(f"Empty Val  : {empty_value} | Type: {type(empty_value)}")

    # ==========================================
    # 3. COLLECTION / CONTAINER DATA TYPES
    # ==========================================
    print_separator("3. Collection Data Types")

    # List: Ordered, mutable (changeable), and allows duplicate elements
    languages = ["Python", "JavaScript", "HTML", "CSS"]
    print(f"List (languages)       : {languages} | Type: {type(languages)}")
    
    # Tuple: Ordered, immutable (unchangeable), and allows duplicate elements
    coordinates = (40.7128, -74.0060)  # Latitude, Longitude of New York
    print(f"Tuple (coordinates)    : {coordinates} | Type: {type(coordinates)}")

    # Dictionary (dict): Unordered (ordered since 3.7), mutable key-value pairs
    project_info = {
        "title": "Variables and Data Types",
        "difficulty": "Beginner",
        "lines_of_code": 75
    }
    print(f"Dictionary (project)   : {project_info} | Type: {type(project_info)}")
    print(f"Access Dictionary key  : The difficulty is '{project_info['difficulty']}'")

    # Set: Unordered, unindexed, unique elements (no duplicates)
    unique_ids = {101, 102, 103, 101, 102}  # Duplicates will be removed automatically
    print(f"Set (unique IDs)       : {unique_ids} | Type: {type(unique_ids)}")

    # ==========================================
    # 4. TYPE CASTING (CONVERSION)
    # ==========================================
    print_separator("4. Type Casting (Conversion)")

    # Converting float to integer
    original_float = 9.99
    converted_int = int(original_float)
    print(f"Float to Int : {original_float} -> {converted_int} (decimals are discarded)")

    # Converting integer/float to string
    number_of_projects = 5
    project_message = "I have built " + str(number_of_projects) + " mini-projects."
    print(f"Int to String: {project_message}")

    # Converting string to integer/float
    string_price = "49.99"
    float_price = float(string_price)
    print(f"String to Float: '{string_price}' (str) -> {float_price} (float) | Result * 2 = {float_price * 2}")

    print("\n🎉 Awesome! You have completed your first variables and data types exploration. 🎉\n")

if __name__ == "__main__":
    main()
