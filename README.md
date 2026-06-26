# Fast_api_app

## creating fastapi application

# CRUD operations

# RestAPI 
Get 
POST 
PUT 
DELETE
# status code
- 200 OK 
- 201 Created or login 
- 204 No content 
- 400 Bad request 
- 401 Unauthorized access
- 403 Forbidden 
- 400 page not found 
- 405 method not allowed 
- 409 conflict
- 500 internal server error 

# Architecture of fastapi application 
- model (denoting the database) -- tables creation
- Routers -- routes requests to controllers
- Controller(what are the company providing logic) -- controller logic 
- Services -- business logic 
- Repository -- data access layer 
- middleware -- request processing pipeline
-            -- it is like a security should i allow the request to backend aor reject  

- Schema--pydantic models for validation


# database 
## 1.Relational database
- Stores data in tables (rows & columns).
- Uses SQL for queries.
- Data is related using Primary Key and Foreign Key.
- Ensures ACID properties (reliable transactions).
- Examples: MySQL, PostgreSQL, Oracle Database.
## 2.Non relational 
- Stores data as documents, key-value pairs, graphs, or columns.
- Flexible schema (no fixed table structure).
- Good for large-scale and unstructured data.
- High scalability and performance.
- Examples: MongoDB, Redis, Apache Cassandra.
- mongodb
- cassandra
- redis 
- dynamodb
# constraints in database 
PRIMARY KEY – Uniquely identifies each record; cannot be NULL. eg:- student id
FOREIGN KEY – Links two tables; maintains referential integrity. eg:- department_id in student table
NOT NULL – Prevents NULL values in a column.eg:-name
UNIQUE – Ensures all values in a column are different. eg:- email, phonenumber. eg:- email,phonenumber
CHECK – Allows only values that satisfy a specified condition. eg:- salary > 0
DEFAULT – Assigns a default value if no value is provided. eg:- timestamp:fun.now()
