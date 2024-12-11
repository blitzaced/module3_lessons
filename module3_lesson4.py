# Web Fundamentals

"""
    This lesson introduces key web concepts including how the client-server model works, APIs, 
    JSON data, endpoints, and how to create virtual environments for managing project dependencies.
    By the end, you'll understand how web browsers interact with servers, hot to retrieve data from
    APIs, and how to set up isolated environments for your projects.
"""

# Client vs Server Model

"""
    How the Client-Server Interaction Works
        Client (Browser): The user interacts with the web by typing a URL into the browser or clicking a link. 
        The broswer then sends an HTTP request to the server.
        
        Server: The server receives the request, processes it, and sends back an HTTP response containing the data
        needed to display the web page, such as HTML, CSS, or JavaScript.
        
        HTTP Request-Response Cycle:
            -Client: The browser sends an HTTP request to the server.
            -Server: The server receives the request, processes it, and responds with the requested data.
        
        Common HTTP Methods:
            -GET: Used by the client to request data from the server (e.g., loading a webpage).
            -POST: Used by the client to send data to the server (e.g., submitting a form).
        
        Example of Client-Server Interaction:
            -URL Request: You enter https://example.com in your web browser.
            -Client (Browser): Sends an HTTP GET request to the server hosting example.com.
            -Server: Receives the request and responds with the HTML page for example.com.
            -Client (Browser): Renders the HTML and displays the page to the user.
            
        Visual Example
            Client (Browser)    -> GET/index.html           -> Server
            Server              -> Response (HTML file)     -> Client (Browser)
            
        Real-World Example
            Every time you visit a website, your browser (the client) and the web server are engaging in this 
            request-response cycle. The server delivers the resources necessary for your browser to display the site, 
            such as HTML files, imagies, and scripts.
"""

# Wat is an API?

"""
    An API (Application Programming Interface) is a set of rules that allows one piece of software to interact
    with another. It enables communication between different systems, lie a browser and a web server. APIs are
    like intermediaries that take your request to a system (like a server) and bring back the data or functionality
    you need.
    
    Types of APIs:
        -Web APIs: Allow web clients (browsers) to communicate with servers using HTTP requests.
        -RESTful APIs: Follow the REST (Representational State Transfer) architectural style, which uses standard HTTP
        methods like GET, POST, PUT, DELETE.
        
    Why APIs Are Important: They allow developers to build front end applications that can access external data or services, 
    like databases, without having to fully understand or build the backend systems.
"""

# PokeAPI Endpoint Example

"""
    Endpoint URL: https://pokeapi.co/api/v2/pokemon/pikachu
        -This URL returns information about Pikachu in JSON format.
"""


import requests

# Make a GET request to the PokeAPI for Pikachu
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

# Check if the request was successful
if response.status_code == 200:
    data = response.json()          # Parse JSON data
    print(data)                     # Output the JSON response
else:
    print('Error: {response.status.code}')
    
# YOU DON"T JUST WANT TO INSTALL IT. GENERALLY YOU WANT TO PUT IT INTO A VIRTUAL ENVIRONMENT.

"""
    Understanding the Code:
        1. Making the Request:
            -The 'requests.get()' function sends an HTTP GET request to the PokeAPI to retrieve
            data about Pikachu.
        2. Checking the Status Code:
            -We check if the response was successful (status code 200). If so, we parse the JSON data using ',json()'.
        3. Output:
            -The response is a JSON object containing details about Pikachu, such as its name, abilities, height, and weight.
""" 

# Learning JSON

"""
    JSON (JavaScript Object Notation) is a lightweight, text-based format for representing structured data. It is widely used
    for transmitting data between a server and a web client (such as a browser) becuase it is easy for both humans and machines
    to read and write.
    
    Why JSON is Important:
        - Human-Readable: JSON is easy for humans to read and understand due to its clean syntax based on key-value pairs.
        - Machine-Friendly: JSON can easily be parsed by machines, making it an ideal format forexchanging data between systems.
        - Cross-Language Compatibility: Although it originates from JabaScript, JSON is language-agnostic and is supported by virtually
        all modern programmin languages, including Python, Java, C#, and Ruby.
        
    JSON has become the standard for data interchange in RESTful APIs and web services becuase of its simplicity and efficiency in
    transmitting structured data.
    
"""

# Working with JSON in Python

"""
    In Python, JSON data is tyically handled using the 'json' module, which allows you to parse (convert) JSON data into Python 
    dictionaries (or lists) and vice versa. This enable you to easily interact with APIs, process responses, and extract the data you need.
    
Parsing JSON Data:
    When you receive JSON data from an API or a file, it comes as a string. To work with it in Python, you first need to parse it into a 
    dictionary using 'json.loads()' (for strings) or 'json.load()' (for files).

EXAMPLE - Parsing
import json

#example JSON string
person ='''
{
    "name": "John",
    "age": 30,
    "skills": ["Python", "Data Analysis"]
}
'''    

#parse JSON string into a Python dictionary
data = json.loads(person)

#access specific fields
name = data['name']
skills = data['skills']

print(f'Name: {name}, Skills: {skills}')

#Output
Name: John, Skils: ['Python', 'Datalysis']   


Serializing (Converting) Python Data to JSON
    When you need to send data as JSON, such as when making an API request, you can convert (serialize)
    Python dictionaries into JSON using 'json.dumps()'.
    
Example - Serializing
import json

#python dictionary
person_data = {
    "name": "John",
    "age": 30,
    "is_student": False
}

#convert python dictionary to JSON string
person_json = json.dumps(person_data)

print(person_json)

#output
{"name": "John", "age": 30, "is_student": false}


Example from PokeAPI - making an API call to retrieve information about a Pokemon, the response is in JSON format:

{
    "name": "pikachu",
    "heaight": 4,
    "weight": 60,
    :abilities": [
        {
            "ability": {
                "name": "static",
                "url": "https://pokeapi.co/api/v2/ability/9/"
            }
        },
        {
         "ability": {
             "name": "lightning-rod",
             "url": "https://pokeapi.co/api/v2/ability/31/"
         }
        }
    ]
}

Key Fields:
    -"name": "pikachu": The name of the Pokemon is Pikachu.
    -"height": 4: Pikachu's height in decimeters.
    -"abilities": A list of Pikachu's abilities, each with its own name and URL for more information.
    
Accessing Data from JSON Response:

#accesssing Pikachu's name and abilities
name = data['name']
abilities = [ability['ability']['name'] for ability in data ['abilities']]

print(f'Pokemon: {name}, Abilities: {abilities}')

#output
Pokemon: pikachu, Abilities: ['statis', 'lightning-rod']


JSON Recap
    - JSON is a flexible, human-readable data format widely used by APIs and web services.
    - In Python, you can use the 'json' module to parse JSON data into Python dictionaries and serialize
    Python data back into JSON format.
    - Key Structure: JSON data consists of key-value pairs, and it can represent objects, arrays, string, numbers, and booleans.
    - In Practice: JSON allows easy data interchange between clients (browsers) and servers, making it a fundamental part of
    working with APIs.
"""  


# Endpoints and Routes
