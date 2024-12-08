# SQL Fundamentals

"""
    What is SQL?
        SQL, or Structured Query Language, is the standard language used for interacting with relational databses. Relational 
        databases store and organize data in a structured format using tables, which consist of rows (records) and columns (fields).
        Each table in a relational databse holds data about a specific entity, such as users, orders, or products, and these tables
        can relate to each other, forming complex data structures.
        
        SQL allows us to perform tasks such as:
            -Creating tables and databases.
            -Inserting, updating, or deleting records.
            -Retrieving data for analysis or reporting.
            
            
    Key Concepts in SQL and Relational Databases
        -Tables: A table is a collection of data organized in rows and columns. Each row represents an individual record, and each column
        represents a specific attribute of that record.
            >Example: In a table, for users, each row could represent a user, and columns could include attributes like username,
            email, and create_at.
        -Rows(Records): A row is a single, complete entry in a table. It contains all the data for one record.
            >Example: A row in the users table might look like this:
            
            user_id             username                email                       created_at
            ----------------------------------------------------------------------------------------------
            1                   john_doe                john@example.com            2024-10-16 10:45:00
    
    
    Basic SQL Syntax
        SQL uses simple syntax with clear, descriptive keywords. Before diving into each category of SQL commands, let's review the 
        basic structure and components of an SQL query.
        
            -Keywords: Commands like CREATE, INSERT, SELECT, and UPDATE define actions.
            -Clauses: Such as WHERE, FROM, and ORDER BY, which refine your queries.
            -Semicolons (;): Used to terminate SQL commands.
            -Comments: SQL allows comments with -- for single-line comments or /*...*/ for multi-line.
            
            EXAMPLE:
            --Select all columns from the users table
            SELECT * FROM users;
            
            
    SQL Commands (DDL, DML, DQL for this lesson):
    
        DDL (Data Definition Language): Commands that define and modify database structures.
        DML (Data Manipulation Language): Commands to manage that data within tables.
        DQL (Data Query Language): Commands to query and retrieve data from the database.
"""

# Data Definition Language (DDL)

"""
    DDL commands define and modify the structure of a batabase. With DDL, you create and manipulate database objects like
    tables and indexes.
    
    The CREATE Command - is used to make new objects in the database, such as databses or tables. Let's look at the syntax for 
    creating a database and a table:
    
        -Creating a Databse:
        
            CREATE DATABASE mydatabase
        
        This command creats a new database named 'mydatabase'. After creating the database, youn eed to use it with:
        
            USE mydatabase
        
         
        -Creating a Table:
        
            CREATE TABLE users(
                user_id INT AUTO_INCREMENT,
                username VARCHAR(50)NOT NULL,
                email VARCHAR(100)NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (user_id)
            );
            
            Breakdown:
                > user_id INT AUTO_INCREMENT: This creates an integer field (INT) that autoincrements, meaning each new user
                gets a unique ID.
                > username VARCHAR(50): This defines a column for usernames, allowing a maximum of 50 character (VARCHAR).
                > NOT NULL: Ensures that the field cannot be empty.
                > PRIMARY KEY (user_id): The primary key uniquely identifies each record in the table.
                > TIMESTAMP DEFAULT CURRENT_TIMESTAMP: Automatically records the time the row was created.
    
    
    The ALTER Command - allows you to modify an existing table's structure by adding, modifying, or dropping columns.
    
        Adding a Column:
        
            ALTER TABLE users ADD last_login TIMESTAMP;
        
        This command adds a new column 'last_login' to the 'users' table. The new colun's data type is TIMESTAMP, which stores both
        date and time values. This column can now be used to track when users last logged into the system.
        
        Modifying a Column:
        
            ALTER TABLE users MODIFY COLUMN email VARCHAR(150) NOT NULL;
            
        This command modifies the existing 'email' column in the 'users' table. It increase the maximum length for the 'email' field
        to 150 characters and enforces the NOT NULL constraint, ensuring that every user must have an email address with no empty
        values allowed.
    
    The DROP Command - deletes entire tables or databases permanently. It is an irreversible operation, so it should be used with caution
    as all the data and the structure are removed.
    
        Dropping a Table:
        
            DROP TABLE users;
            
        This command completely removes the 'users' table from the database, including all of its structure. Once executed, the table 
        is deleted, and it cannot be recovered unless there is a backup in place.
"""

# Data Manipulation Language (DML)

"""
    DML commands allow you to manipulate the data inside your tables. This is where you add, update, or delete records.
    
    The INSERT INTO Command - used to add new rows of data to a table.
    
        EXAMPLE:
            INSERT INTO users (username, email)
            VALUES ('john_doe', 'john@example.com');
            
        Breakdown:
            - INSERT INTO users (username, email): This specifies the table (users) where the new data will be added and the specific
            columns (username, email) that will receive the values.
            - VALUES ('john_doe', 'john@example.com'): These are the values being inserted into the specified columns. In this case, the value
            'john_doe' is inseted into the 'username' column, and 'john@example.com' is inserted into the 'email' column.
            
        What it does:
            The command inserts a new record into the 'users' table. A new user with the username 'john_doe' and the email 
            'john@example.com' is added as a row in the table.
            
    The UPDATE Command - used to modify existing records in a table.
    
        EXAMPLE:
            UPDATE users SET email = 'new_email@example.com' WHERE user_id = 1;
            
        Breakdown:
            - SET email = 'new_email@example.com': This specifies the colum (email) that you want to update and assigns it a new value
            ('new_email@example.com').
            - WHERE user_id = 1: This condition ensures that only the row where 'user_id' is '1' will be updated. The WHERE claus is
            crucial becuase it restricts the update to a specific row or set of rows.
            
        Important Note:
            Id you omit the WHERE clause, every record in the 'users' table would have its 'email' column updated to 
            'new_email@example.com'. This is why it's important to use WHERE carefully, as it determines which rows are affected by 
            the update.
            
    The DELETE Command -  used to remove records from the table.
    
        EXAMPLE:
            DELETE FROM users WHERE user_id = 1;
            
        Breakdown:
            - DELETE FROM users: Specifies the table (users) from which you want to delete records.
            - WHERE user_id = 1: Ensures that only the row where 'user_id' is '1' will be deleted. This condition targets a 
            specific record, preventing accidental deletion of other data.
            
        Important Note:
            Like with UPDATE, if you omit the WHERE clause, all records in the 'users' table will be delete. Always use the
            WHERE clause to precisely control which records are affected by the DELETE command.
"""

# Data Query Language (DQL)

"""
    DQL is all about querying the database to retrieve data in a meaningful way. The most common DQL command is SELECT.
    
    The SELECT Command - used to retrieve data from a table. You can specify which columns you want to retrieve, or you can 
    retrieve all columns from the table.
    
        EXAMPLE Select All Columns:
            SELECT * FROM users
            
        What it does: The * symbol is a wildcard that tells SQL to return every column from the 'users' table. This will
        retrieve all rows and all columns for each user in the table.
        
        Example Result: You'll get back a result with every available field, such as 'user_id', 'username', 'email', etc.,
        for all users in the 'users' table.
        
        EXAMPLE Select Specific Columns:
            SELECT username, email FROM users;
            
        What it does: Instead of retrieving all columns, you specify only the columns you're interested in --'username' and 'email'.
        This limits the data returned to just these two columns for each row.
        
        Example Result: The query will return a table with only two columns: 'usernam' and 'email', showing only these attributes
        for all users in the 'users' table.
        

    The WHERE Clause - used to filter results by specifying a condition. Only rows that match the condition will be included in the
    query results.
    
        EXAMPLE:
            SELECT * FROM users WHERE username = 'john_doe'
            
        What it does: This query retrieves all columns (*) from the 'users' table but only for the rows where the 'username'
        column equals 'john_doe'.
        
        Purpose: The WHERE clause narrows down the results, ensuring that only the user with the username 'john_doe' is returned.
        
        Without WHERE, the query would return every row in the 'users' table. The WHERE clause makes it possible to target
        specific records based on a condition.
        
    
    The ORDER BY Clause - used to sort the results of a query based on one or more columns. You can specify whether the results
    should be ordered in ascending (ASC) or descending (DESC) order.
    
        EXAMPLE:
            SELECT * FROM users ORDER BY  created_at DESC;
            
        What it does: This query retrieves all columns (*) from the 'users' table and orders the results by the 'create_at' column
        in descending order (DESC), meaning the most recent entries appear first.
        
        Pupose: By using ORDER BY, you can control the order of the returned rows, which is especially useful when you're dealing
        with dates, numbers, or any data you want to rank or prioritize.
        
        If you wanted the oldest entries first, you would use ASC (ascending) instead of DESC:
        
            SELECT * FROM users ORDER BY created_at ASC;
            
    
    The LIKE Operator - is used for pattern matching in queries, allowing you to search for values that match a specific pattern.
    It is commonly used with wildcard character:
    
        1. % : Represents zero or more characters.
        2. _ : Represents a single character.
        
        EXAMPLE:
            SELECT * FROM users WHERE email LIKE '%example.com';
            
        What it does: This query retrieves all columns (*) from the 'users' table where the 'email' column ends with 
        'example.com'.
        
        Purpose: The '%' wildcard before 'example.com' allows for any characters before the domain, meaning this query will
        match emails like 'john@example.com', 'jane@example.com', and so on.
        
        You can also use LIKE to search for patterns at the beginning or middle of a string:
        
            - Starts with a pattern:
                SELECT * FROM users WHERE username LIKE 'john%';
                
                This finds all users whose username starts with 'john' (e.g., john_doe, johnsmith).
                
            - Contains a pattern anywhere:
                SELECT * FROM users WHERE email LIKE '%@gmail.com%';
                
                This retrieves all users with a 'gmail.com' email address. 
"""