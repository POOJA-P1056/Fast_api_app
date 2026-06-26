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