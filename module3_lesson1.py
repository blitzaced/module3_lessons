# Database Fundamentals

"""
    What is a Database?
        -A database is an organized collection of data, stored and accessed electronically, that allows for 
        efficient management, retrieval, and manipulation of information. Databases are designed to handle large 
        volumes of data in a structured format, making it easy to store, retrieve, update, and delete information.
"""

# Key Concepts

"""
    Structured Data Storage - A database is structured in a way  that enables efficient storage and retrieval of data. The structure
    typically involves tables (in relational databases), where data is stored in rows and columns, similar to a spreadsheet.
    
        -Table: A collection of related data entries, structures in rows and columns (for example, a "Customers" table might store
            customer names, addresses, and contact details).
        -Row: Each row in a table represents a single entry or record (for example, a single customer).
        -Column: Each column in a table represents an attribute of the data (for example, a "Name" or "Email" field).
        
    Database Management System (DBMS) - software that enables users to interact with the database, allowing for data to be stored, 
    modified, and retrieved. Example of popular DBMS software include MySQL, PostgreSQL, MongoDB, and Oracle.
    
    Data Integrity and Security - Databases ensure data integrity by enforcing rules on the types of data that can be entered, 
    relationships between different data sets, and sontraints (like ensuring that certain fields are unique). Additionally, databases 
    provide various levels of data security, ensuring that unauthorized users cannot access or alter the data.
    
    Types of Databases:
        -Relational Databases: Stoare data in structured tables with rows and columns, where relationships between data are
        maintained using primary keys and foreign keys. Common examples include MySQL and PostgreSQL.
        -Non-Relational Databases (noSQL): Store data in a flexible, unstructured way, such as in documents, key-value pairs, or graphs.
        Common examples include MongoDB and Redis.
        
    Common Database Operations
        Databases enable a wide variety or operations for managing data:
            -Create: Add new records to a table (e.g., adding a new customer).
            -Read: Retrieve data from the database (e.g., viewing all orders placed by a customer).
            -Update: Modify exisiting data (e.g., updating a customer's email address).
            -Delete: Remove data (e.g., deleting an outdated record). 
    
    Real-World Examples of Databases:
        1. E-commerce Platforms:
            -Amazon: Uses a large database to store product information, user accounts, orders, and inventory.
        2. Banking Systems:
            -Banks use databases to manage customer accounts, transactions, loans, and financial data, ensuring security
                and integrity.
        3. Social Media:
            -Platforms like Facebook or Instagram use databases to store user profiles, posts, comments, and friend lists.
"""

# Relational Databases (SQL Databases)

"""
    A relational databses organizes data into structures tables (also called relations), where each table consists of rows
    and columns. These tables are connected to each other through relationships, typically defined by primary keys and foreign keys.
    
        -Data Model: Relational databases use a strict schema where the data is stored in tables, each defined with a fixed
        structure (columns and their data types).
        
        -Query Language: They use Structure Query Language (SQL) ti ubteract with the database. SQL allows for complex queries
        to retrieve, insert, update, and delete data.
        
        -ACID Compliance: Relational databases follow the ACID properties -- Atomicity, Consistency, Isolation, and Durability --
        which ensure reliable and consistent transactions.
        
        -Use Case: Suitable for applucations requiring structures data and complex queries (e.g., banking systems, e-commerce
        platforms, enterprise resource planning systems).
        
    Advantages:
        -Data Integrity: The use of constraints and relationships (foreign keys) ensures data integrity.
        -Structured Data: Well-suited for handling structured data where relationships between entities are important.
        -Complex Queries: SQL enables complex queries, including joins, aggregations, and filtering, making it easier
        to retrieve specific data across mutliple tables.
        
    Disadvantages:
        -Scalability: Relational databases are traditionally scaled vertically, meaning that improving performance often requires
        upgrading the hardward. This can be limiting for large-scale applications.
        -Schema Rigidity: Requires a predefined schema, which can make it less flexible when dealing with unstructure or rapidly
        changing data.
            
    Examples:
        -MySQL: Widely used in web applications for storing structured data, such as user information, orders, and products.
        -PostgreSQL: Known for its support of complex queries and advanced data types.
        -Oracle: Often used in large enterprise environments for mission-critical applications.   
"""


# Non-Relational Databases (NoSQL Databases)

"""
    A non-relational database (commonly referred to as NoSQL) stores data in a non-tabular format, often designed for handling large
    volumes of unstructure or semi-structured data. These databases use a variety of data models, such as document_based, key-value
    pairs, colum-based, and graph structures.
    
        -Data Model: Non-relational databases do not require a fixed schema. Daat is often stored in a more flexible format like
        JSON documents, key-value pairs, or graphs.
        
        -Query Language: The query language vaires depending on the NoSQL database. For example, document-based databases like
        MongoDB allow for queries using JSON, while key-value stores may use specific API-based queries.
        
        -BASE Model: NoSQL databases often follow the BASE model -- Basically Available, Soft state, Eventual consistency --
        which emphasizes availability and scalability over strict consistency.
        
        -Use Case: Ideal for applications dealing with large volumes of unstructured or semi-strictyred data, real-time applications,
        and big data (e.g., social media, IoT applications, real-time analytics).
        
    Types od Non-Relational Databases:
        -Document-Based Databses: Store data in documents, typically in JSON or BSON format (e.g., MongoBD).
        -Key-Value Stores: Store data as key-value pairs, where each key is unique, and values can be anything (e.g., Redis).
        -Column-Family Stores: Store data in columns instead of rows, optimized for reading and writing large datasets (e.g., Cassandra).
        -Graph Databases: Store data as nodes and relationships, ideal for applications where relationships between entities
        are important (e.g., Neo4j).
        
    Advantages:
        -Scalability: Non-relational databases are typically horizontally scalable, meaning they can handle large amounts of data
        by distributing it across multiple servers.
        -Flexibility: The schema-less nature allows for storing different kinds of data in a flexible and dynamic way.
        -High Availability: Many NoSQL databases are designed to ensure high availability and are fault-tolerant, making them
        suitable for applications requiring real-time data processing.
        
    DisadvantagesL
        -Lack of ACID Compliance: No SQL databases may sacrifice consistency in favor of availability and partition tolerance, which
        can lead to eventual consistency rather than immediate consistency.
        -Less Support for Complex Queries: While many NoSQL databases offer powerful querying capabilities, they may not support the
        complex joins and transactions found in SQL databases.
        
    Examples:
        -MongoDB: A popular document-based NoSQL database that stores data in a flexible, JSON-like format.
        -Cassandra: A column-family store designed for handling large volumes of data across disctributed systems.
        -Redis: A fast, in-memory key-value store, often used for caching, sessions management, and real-time analytics.
        
"""

# Comparison Table: Relational vs. Non-Relational Databases

"""
    Features                    Relational Database (SQL)                   Non-Relational Databases (NoSQL)
    -----------------------------------------------------------------------------------------------------------------------------
    Data Model                  Tables with rows and columns                Varies: documents, key-value, column-family, or graphs
                                (relational)                                (non-relational)
    
    Schema                      Fixed schema, predefined table              Flexible schema, dynamic data structures
                                and columns
    
    Query Language              Structured Query Language (SQL)             Caries by type (e.g., JSON for document stores, API for
                                                                            key-value)
    
    ACID Complaince             Full ACID compliance (strict consistency)   BASE model (eventual consistency, high availability)
    
    Scalability                 Vertical scalability (scaling up by         Horizontal scalability (scaling out by adding more 
                                increasing server resources)                servers)
    
    Use Cases                   Structured data, complex queries,           Unstructured or semi-structured data, real-time
                                transactional systems                       applications, large-scale data handling
    
    Examples                    MySQL, PostgreSQL, Oracle                   MongoDB, Cassandra, Redi, Neo4j
    ------------------------------------------------------------------------------------------------------------------------------
    
    When to Use Relational Databases:
        -Structured Data: When your data is highly structured and requires well-defined relationships, such as in financial systems,
        inventory management, and HR systems.
        -Complex Queries: When your application requires complex queries, including joins, aggregations, and filtering across
        multiple tables.
        -Transactions: When strict ACID compliance is important, such as in banking applucationwhere consistency is critical.
        
    When to Use Non-Relational Databases:
        -Big Data & Scalability: When dealing with large-scale datasets that need to be distributed across multiple servers, such as
        in social media, IoT, and real-time analytics.
        -Flexibility: When the data model is evolving or unstructured, and flexbility is more important than predefined schema
        (e.g., for storing user-generated content).
        -Real-Time Processing: For real-time applications where low-latency data access os crucial, such as chat applications, live
        streaming, or gaming.
""" 

# Entity Relationship Diagrams (ERDs) for Relational Databases

"""
    An Entity Relationship Diagram (ERD) is a crucial tool for designing and visualizing the structure of a relational database.
    ERDs help in mapping out the relationships between tables (entities) and understanding how data flows and connects within a
    database.
    
"""


# What is an ERD?

"""
    An Entity Relationship Diagram (ERD) is a graphical representation that shows the relationships between entities in a relational
    database. Entities (typically tables) are represented as boxes, and relationships between these entities are depicted with lines, 
    showing how they interact with one another.
    
    ERDs are fundamental during the databse design phase, as they help to ensure data is organized properly, relationships between 
    tables are clear, and database integrity is maintained.
    
"""

# Components of an ERD

"""
    1. Entities - An entity represents a database table. Each entity contains attrubutes *columns) that store information about the data
    in that table.
        -Example: In an e-commerce system, you might have entities like:
            >Customer: Stores customer information such as name, email, and address.
            >Order: Stores information about a customer's order, such as order date and total amount.
    
    2. Attributes - The properties or details of an entity. They represent the columns in a database table, each describing a specific
    characteristic of the entity. Attributes are usually listed within the entity box in an ERD as rows.
        -Example: For the  'Customer' entity, typical attributes might include:
            >CustomerID (Prmiary Key)
            >Name
            >Email
            >Phone Number
            
        Each attirbute has a data type, which specifies the kind of data that can be stored in that column. Data types are crucial
        because they define what kind of values are allowed in a column, and they optimize how data is stored and retrieved. Here
        are some common data types:
            >Integer (INT): Stores whole numbers. For example, 'CustomerID' or 'OrderID'.
            >VARCHAR(n): Variable-length string of up to n characters. Used for storing text, like 'Name' or 'Email'.
            >CHAR(n): Fixed-length string of n characters. Ideal for values like 'PhoneNumber' or 'PostalCode'.
            >FLOAT or DECIMAL: Stores decimal numbers. Used for attributes like 'TotalAmount' in an order.
            >DATE or DATETIME: Stores date and time information. Used for attributes like 'OrderDate' of 'Birthdate'.        

    3. Relationships - Depict how two entities are related to each other. These relationships are key to understanding how data is 
    linked across tables. Relationships are represented by lines between entities, and they include 'Cardinality' and 'Ordinality'
    (which describes the nature of the relationships, such as one-to-one or one-to-many).
    

    Keys in ERDs - Keys are essential for defining relationships and ensuring data integrity in relational databses.
    
        1. Primary Key (PK) - Unique identifier for each record in a table. It ensures that each row in a table is unique and can
        be referenced easily.
            -Example: In a 'Customer' table, 'CustomerID' would typicaly be the primary key, uniquely identifying each customer.
        
        2. Foregin Key (FK) - A field in one table that references the primary key (PK) of another table. This is how relationships
        are established between tables.
            -Example: In an 'Order' tbale, 'CustomerID' would be a foreign key (FK) that links each order to a specific customer
            in the 'Customer' table.
            
        Foreign keys (FK) ensure referential integrity, meaning that relationships between data are maintained properly.
        
    
    Cardinality vs. Ordinality
    
        When designing a database using an Entity Relationship Diagram (ERD), both the cardinality and ordinality play key roles in 
        defining how entities (tables) relate to one another. While they seem similar, they serve different purposes in modeling 
        relationships. Here's a clear comparison:
        
        Cardinality: Maximum Number of Relationships
            Cardinality refers to the maximum number of times an instance in one entity can be associated with instances in another
            entity. It answers the question, "What is the largest number of relationships that can exist between these two entities?"
            
            -Example: A 'Customer' can place many 'Orders', but each 'Order' can be associated with only one 'Customer'. This describes 
            a One-to-Many cardinality (1).
            -Real-World Example: In an e-commerce system, one customer can place multiple orders, but each order belongs to just one
            customer.......
            
            Cardinality Types:
                -One-to-One (1:1): One entity relates to exactly one instance of another entity.
                -One-to-Many (1): One entity relates to many instances of another entity.
                -Many-to-Many (M): Entities on both sides can relate to many instances of the other.
                
        
        Ordinality: Minimum Number of Relationships
            Ordinality refers to the minimum number of times an instance in one entity must be associated with instances in another
            entity. It tells us if the relationship is mandatory or optional.
            
            -Example: A 'Customer; may place an 'Order', but not every customer is required to do so. This describes an 'Optional' 
            ordinality because a customer can exist without ever placing an order.
            -Real-World Example: In a memebership system, a member might sign up for a service but never make a purchase. The 
            relationship between the memeber and purchases is optional.
            
            Ordniality Types:
                -Mandatory: A relationship must exist (minimum one relationship is required). For example, every 'Order' must be tied
                to a 'Customer'.
                -Optional: The relationship is not required (minimum of zero relationships). For example, a 'Customer' can exist
                without placing any 'Orders'.
                
        
        Key Points:
            -Cardinality defines the maximum numbver of times an entity can be associated with another entity. It tells us the
            "upper limit" of how entities relate.
            -Ordniality defines the minimum number of times an entity must be associated with another entity. It tells us whether a
            relationship is required *mandatory) or optional.
            
            By combining both cardinality and ordinality in an ERD, we can model not just how entities are related, but also whether
            those relationships are required or can be optional, creating a more accurate and flexible database structure.            
"""

