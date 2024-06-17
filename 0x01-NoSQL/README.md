# 0x01. NoSQL Project

## Overview

This project focuses on learning and implementing NoSQL databases, specifically MongoDB, using Python. The tasks involve querying, inserting, updating, and deleting data in MongoDB, both through the MongoDB shell and via Python scripts using the PyMongo library.

## Learning Objectives

By the end of this project, you should be able to:

- Understand the concept of NoSQL and its types.
- Differentiate between SQL and NoSQL databases.
- Explain ACID properties.
- Describe document storage.
- List the benefits of NoSQL databases.
- Perform CRUD operations in a NoSQL database.
- Use MongoDB effectively.

## Resources

- [NoSQL Databases Explained](https://example.com)
- [What is NoSQL?](https://example.com)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://example.com)
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](https://example.com)
- [Aggregation](https://example.com)
- [Introduction to MongoDB and Python](https://example.com)
- [mongo Shell Methods](https://example.com)
- [Mongosh](https://example.com)

## Requirements

### MongoDB Command File
- Files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2).
- Each file should end with a new line and start with a comment.
- A `README.md` file at the root of the project folder is mandatory.
- File lengths will be tested using `wc`.

### Python Scripts
- Files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7 and PyMongo 3.10.
- Each file should end with a new line and start with a shebang (`#!/usr/bin/env python3`).
- Follow the `pycodestyle` style guide (version 2.5.*).
- Each module and function should have documentation.
- Prevent execution of code when imported using `if __name__ == "__main__":`.

## Setup Instructions

### Installing MongoDB 4.2 on Ubuntu 18.04

```bash
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
$ echo "deb [arch=amd64,arm64] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
$ sudo service mongod start
$ mongo --version
```

### Installing PyMongo

```bash
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'
```

### Potential Issues and Fixes

- If encountering `Data directory /data/db not found.`, create the directory:
  ```bash
  $ sudo mkdir -p /data/db
  ```

- If `/etc/init.d/mongod` is missing, refer to the official MongoDB installation guide.

## Running MongoDB

To start MongoDB:

```bash
$ service mongod start
```

## Project Tasks

### Task 0: List all databases

Create a script to list all databases in MongoDB.

### Task 1: Create a database

Create or use the database `my_db`.

### Task 2: Insert document

Insert a document in the collection `school` with the attribute `name: "Holberton school"`.

### Task 3: All documents

List all documents in the collection `school`.

### Task 4: All matches

List all documents with `name="Holberton school"` in the collection `school`.

### Task 5: Count

Display the number of documents in the collection `school`.

### Task 6: Update

Add a new attribute `address: "972 Mission street"` to documents with `name="Holberton school"`.

### Task 7: Delete by match

Delete all documents with `name="Holberton school"` in the collection `school`.

### Task 8: List all documents in Python

Create a Python function to list all documents in a collection.

### Task 9: Insert a document in Python

Create a Python function to insert a new document in a collection based on kwargs.

### Task 10: Change school topics

Create a Python function to change all topics of a school document based on the name.

### Task 11: Where can I learn Python?

Create a Python function to return the list of schools having a specific topic.

### Task 12: Log stats

Create a Python script to provide some stats about Nginx logs stored in MongoDB.

## Repository Structure

- `0x01-NoSQL`
  - `0-list_databases`
  - `1-use_or_create_database`
  - `2-insert`
  - `3-all`
  - `4-match`
  - `5-count`
  - `6-update`
  - `7-delete`
  - `8-all.py`
  - `9-insert_school.py`
  - `10-update_topics.py`
  - `11-schools_by_topic.py`
  - `12-log_stats.py`
  - `README.md`

## Conclusion

This project aims to provide hands-on experience with MongoDB and NoSQL databases, highlighting their unique features and use cases. Happy coding!
