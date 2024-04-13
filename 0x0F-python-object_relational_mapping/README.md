## Object-Relational Mapping with Python
This project aims to demonstrate the fundamentals of Object-Relational Mapping (ORM) using Python. By leveraging ORM libraries like MySQLdb and SQLAlchemy, the project establishes connections to a MySQL database and performs various operations like querying, inserting, updating, and deleting data using Python scripts.

## Table of Contents
#Description
#Installation
#Usage
#Files
#Dependencies

## Description
Object-Relational Mapping (ORM) is a programming technique that allows developers to work with relational databases using an object-oriented approach. In this project, we explore how to use ORM libraries in Python to interact with a MySQL database seamlessly. The project covers the following key concepts:

- Connecting to a MySQL database from a Python script
- Performing CRUD (Create, Read, Update, Delete) operations using MySQLdb and SQLAlchemy
- Writing secure code to prevent SQL injection vulnerabilities
- Defining and mapping Python classes to database tables using SQLAlchemy
- Querying data from database tables using SQLAlchemy


## Installation
To run the scripts in this project, follow these steps:
Ensure you have Python 3.8 installed on your system.

# Install the MySQLdb library version 2.0.x:
''' 
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
'''

# Install the SQLAlchemy library version 1.4.x:
''''
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclieny code
$ sudo pip3 install SQLAlchemy

# Clone this repository to your local machine:

''''
$ git clone <repository-url>


## Usage
Navigate to the directory containing the Python scripts and execute them with the required arguments. For example:

''''
$ ./0-select_states.py <mysql-username> <mysql-password> <database-name>
Ensure you replace <mysql-username>, <mysql-password>, and <database-name> with your MySQL credentials and database name.

## Files
0-select_states.py: Script to list all states from the database.
1-filter_states.py: Script to list states starting with 'N'.
2-my_filter_states.py: Script to list states based on user input.
3-my_safe_filter_states.py: Script to list states safely without SQL injection vulnerability.
4-cities_by_state.py: Script to list all cities from the database.
5-filter_cities.py: Script to list cities of a specific state.
6-model_state.py: Script to define the State class and create the database table.
7-model_state_fetch_all.py: Script to fetch all State objects from the database.
8-model_state_fetch_first.py: Script to fetch the first State object from the database.
9-model_state_filter_a.py: Script to list states containing the letter 'a'.
10-model_state_my_get.py: Script to retrieve a State object by name.
11-model_state_insert.py: Script to insert a new State object into the database.
12-model_state_update_id_2.py: Script to update the name of a State object.
13-model_state_delete_a.py: Script to delete State objects containing the letter 'a'.

model_state.py: Module containing the State class definition.
model_city.py: Module containing the City class definition.
README.md: Project documentation.

## Dependencies
- Python 3.8
- MySQLdb 2.0.x
- SQLAlchemy 1.4.x
