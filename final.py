import mysql.connector
import random

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="harsh",
    database="quiz_db"
)
cursor = db.cursor()

def setup_database():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(50) NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        question TEXT NOT NULL,
        option1 VARCHAR(255),
        option2 VARCHAR(255),
        option3 VARCHAR(255),
        option4 VARCHAR(255),
        answer VARCHAR(255),
        topic VARCHAR(255) NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        score INT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

def insert_questions():
    questions = [
        # RDMS Questions
        ("What does SQL stand for?", "Structured Query Language", "Simple Query Language", "Standard Question Language", "None of the above", "Structured Query Language", "RDMS"),
        ("Which SQL clause is used to sort the result-set?", "ORDER BY", "SORT BY", "GROUP BY", "ARRANGE BY", "ORDER BY", "RDMS"),
        ("Which command is used to delete a table in SQL?", "DELETE TABLE", "REMOVE TABLE", "DROP TABLE", "CLEAR TABLE", "DROP TABLE", "RDMS"),
        ("What is a primary key?", "A unique identifier", "A duplicate identifier", "A foreign key", "None of the above", "A unique identifier", "RDMS"),
        ("Which SQL function is used to count the number of rows?", "SUM()", "COUNT()", "TOTAL()", "NUMBER()", "COUNT()", "RDMS"),
        ("What does ACID stand for in databases?", "Add, Create, Implement, Delete", "Atomicity, Consistency, Isolation, Durability", "Aggregate, Consistency, Isolation, Data", "None of the above", "Atomicity, Consistency, Isolation, Durability", "RDMS"),
        ("What is normalization?", "Removing redundancy", "Adding redundancy", "Deleting tables", "Creating indexes", "Removing redundancy", "RDMS"),
        ("What is a foreign key?", "A field linking to a primary key in another table", "A field with unique values", "A key that locks tables", "None of the above", "A field linking to a primary key in another table", "RDMS"),
        ("What is a composite key?", "A key that is a combination of two or more columns", "A key with unique values", "A primary key", "None of the above", "A key that is a combination of two or more columns", "RDMS"),
        ("What is the purpose of the GROUP BY clause?", "To group identical values", "To delete duplicates", "To count rows", "To limit rows", "To group identical values", "RDMS"),
        ("What is a view in SQL?", "A virtual table", "A copy of a table", "A stored procedure", "A backup of a table", "A virtual table", "RDMS"),
        ("What is the default sorting order in SQL?", "Ascending", "Descending", "Alphabetical", "Random", "Ascending", "RDMS"),
        ("What is a unique constraint?", "Ensures all values are distinct", "Ensures all values are duplicate", "Restricts length of values", "None of the above", "Ensures all values are distinct", "RDMS"),
        ("Which SQL statement is used to update existing data?", "UPDATE", "MODIFY", "CHANGE", "ALTER", "UPDATE", "RDMS"),
        ("What does the HAVING clause do?", "Filters groups based on conditions", "Filters individual rows", "Limits columns", "None of the above", "Filters groups based on conditions", "RDMS"),
        ("Which SQL statement is used to remove rows from a table?", "DELETE", "DROP", "REMOVE", "CLEAR", "DELETE", "RDMS"),
        ("What is an index in SQL?", "Improves query performance", "Deletes duplicate rows", "Defines a primary key", "None of the above", "Improves query performance", "RDMS"),
        ("What is a trigger in SQL?", "A procedure that runs automatically in response to an event", "A primary key", "A stored procedure", "A query optimizer", "A procedure that runs automatically in response to an event", "RDMS"),
        ("What is a candidate key?", "A field that can act as a primary key", "A foreign key", "A unique constraint", "None of the above", "A field that can act as a primary key", "RDMS"),
        ("Which SQL keyword is used to retrieve unique values?", "DISTINCT", "UNIQUE", "SPECIFIC", "ONLY", "DISTINCT", "RDMS"),

        # Python 
        ("What is Python?", "A snake", "A programming language", "A type of database", "None of the above", "A programming language", "Python"),
        ("Which keyword is used to define a function in Python?", "function", "def", "define", "func", "def", "Python"),
        ("Which data structure is immutable in Python?", "List", "Tuple", "Dictionary", "Set", "Tuple", "Python"),
        ("What is the output of 2**3 in Python?", "8", "6", "9", "None of the above", "8", "Python"),
        ("Which method is used to add an element to a list?", "add()", "append()", "insert()", "push()", "append()", "Python"),
        ("What is the keyword used for inheritance in Python?", "inherit", "extends", "super", "None of the above", "super", "Python"),
        ("What does the len() function do?", "Finds the length of an object", "Counts the elements", "Sorts a list", "None of the above", "Finds the length of an object", "Python"),
        ("What is a lambda function?", "A function defined with lambda", "A recursive function", "A built-in function", "None of the above", "A function defined with lambda", "Python"),
        ("What is a dictionary in Python?", "A collection of key-value pairs", "A mutable list", "A type of tuple", "None of the above", "A collection of key-value pairs", "Python"),
        ("Which library is used for data visualization in Python?", "numpy", "matplotlib", "scipy", "pandas", "matplotlib", "Python"),
        ("What is used to handle exceptions in Python?", "try-except", "catch-finally", "if-else", "None of the above", "try-except", "Python"),
        ("Which symbol is used for comments in Python?", "#", "//", "/* */", "<!-- -->", "#", "Python"),
        ("What is the output of print(10//3)?", "3", "3.33", "10", "None of the above", "3", "Python"),
        ("Which Python keyword is used to create a class?", "define", "class", "create", "new", "class", "Python"),
        ("What is PIP in Python?", "A package manager", "A loop", "A function", "None of the above", "A package manager", "Python"),
        ("Which of these is not a Python data type?", "String", "Integer", "Float", "Character", "Character", "Python"),
        ("What is the use of the 'pass' keyword in Python?", "To skip execution", "To break a loop", "To define a class", "None of the above", "To skip execution", "Python"),
        ("Which function is used to read a file in Python?", "open()", "read()", "file()", "get()", "open()", "Python"),
        ("What is the output of bool([])?", "True", "False", "None", "Error", "False", "Python"),
        ("What is a module in Python?", "A file containing Python code", "A data type", "A function", "None of the above", "A file containing Python code", "Python"),

        # JavaScript 
        ("Which symbol is used for single-line comments in JavaScript?", "//", "#", "/* */", "<!-- -->", "//", "JavaScript"),
        ("Which data type is used to store true or false values in JavaScript?", "Boolean", "String", "Number", "Object", "Boolean", "JavaScript"),
        ("What does 'typeof' return in JavaScript?", "Data type of a variable", "Value of a variable", "Reference of a variable", "None of the above", "Data type of a variable", "JavaScript"),
        ("Which method is used to find the length of a string in JavaScript?", "length()", "size()", "count()", "None of the above", "length()", "JavaScript"),
        ("What is the output of '2' + 2 in JavaScript?", "'22'", "4", "'4'", "Error", "'22'", "JavaScript"),
        ("What is used to declare variables in JavaScript?", "var, let, const", "int, float, double", "dim, set", "None of the above", "var, let, const", "JavaScript"),
        ("Which function is used to parse a string into a number in JavaScript?", "parseInt()", "convert()", "toNumber()", "None of the above", "parseInt()", "JavaScript"),
        ("What is NaN in JavaScript?", "Not a Number", "A string", "A type of object", "None of the above", "Not a Number", "JavaScript"),
        ("Which JavaScript method is used to add an element to the end of an array?", "push()", "append()", "add()", "insert()", "push()", "JavaScript"),
        ("What is the output of 5 === '5' in JavaScript?", "false", "true", "error", "undefined", "false", "JavaScript"),
        ("Which keyword is used to create a function in JavaScript?", "function", "func", "def", "method", "function", "JavaScript"),
        ("What is the purpose of the 'this' keyword in JavaScript?", "Refers to the current object", "Declares a variable", "Calls a method", "None of the above", "Refers to the current object", "JavaScript"),
        ("What is the DOM in JavaScript?", "Document Object Model", "Data Object Manager", "Dynamic Object Model", "None of the above", "Document Object Model", "JavaScript"),
        ("What is the default value of an uninitialized variable in JavaScript?", "undefined", "null", "0", "None of the above", "undefined", "JavaScript"),
        ("Which JavaScript event occurs when a user clicks on an HTML element?", "onclick", "onhover", "onchange", "onselect", "onclick", "JavaScript"),
        ("How do you declare a constant in JavaScript?", "const", "let", "var", "constant", "const", "JavaScript"),
        ("What is JSON?", "JavaScript Object Notation", "JavaScript Online", "Java Structure Object", "None of the above", "JavaScript Object Notation", "JavaScript"),
        ("What is the output of null == undefined in JavaScript?", "true", "false", "error", "undefined", "true", "JavaScript"),
        ("Which method is used to convert an object to a string in JavaScript?", "JSON.stringify()", "toString()", "convert()", "None of the above", "JSON.stringify()", "JavaScript"),
        ("What is the purpose of the 'alert()' function in JavaScript?", "To display a message box", "To log messages", "To raise errors", "None of the above", "To display a message box", "JavaScript")
    ]

    insert_query = """
    INSERT INTO questions (question, option1, option2, option3, option4, answer, topic)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.executemany(insert_query, questions)
    db.commit()
    print("Questions have been inserted successfully.")

def get_random_questions(topic):
    cursor.execute("SELECT * FROM questions WHERE topic = %s ORDER BY RAND() LIMIT 5", (topic,))
    return cursor.fetchall()

def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    db.commit()
    print("Registration successful! Please log in to continue.")
    
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    cursor.execute("SELECT id FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    if user:
        print("Login successful!")
        return user[0]
    else:
        print("Invalid username or password.")
        return None    

def take_quiz(user_id):
    print("\nSelect a topic:")
    print("1. RDMS")
    print("2. Python")
    print("3. JavaScript")
    topic_choice = input("Enter the number of your choice: ")
    topics = { "1": "RDMS", "2": "Python", "3": "JavaScript" }
    topic = topics.get(topic_choice)
    if not topic:
        print("Invalid choice.")
        return
    
    questions = get_random_questions(topic)
    score = 0
    for q in questions:
        print("\n" + q[1])
        print(f"A. {q[2]}")
        print(f"B. {q[3]}")
        print(f"C. {q[4]}")
        print(f"D. {q[5]}")
        answer = input("Your answer (A/B/C/D): ").lower()
        if answer == 'a' and q[2] == q[6]:
            score += 1
        elif answer == 'b' and q[3] == q[6]:
            score += 1
        elif answer == 'c' and q[4] == q[6]:
            score += 1
        elif answer == 'd' and q[5] == q[6]:
            score += 1
    cursor.execute("INSERT INTO scores (user_id, score) VALUES (%s, %s)", (user_id, score))
    db.commit()
    print(f"\nQuiz completed! Your score is {score}/5.")

def main():
    setup_database()
    insert_questions()
    while True:
        print("\n1. Register\n2. Login\n3. Quit")
        choice = input("Select an option: ")
        if choice == "1":
            register()
        elif choice == "2":
            user_id = login()
            if user_id:
                take_quiz(user_id)
        elif choice == "3":
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please try again.")

main()
cursor.close()
db.close()

      
     