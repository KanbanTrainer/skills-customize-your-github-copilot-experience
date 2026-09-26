# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build a REST API using the FastAPI framework, including defining endpoints, handling parameters, and validating request data with Pydantic models.

## 📝 Tasks

### 🛠️ Setting Up a Basic Endpoint

#### Description
Create a FastAPI app with a root endpoint that returns a welcome message, and a `GET /items` endpoint that returns a list of items.

#### Requirements
Completed program should:

- Create a FastAPI app instance called `app`.
- Define a `GET /` endpoint that returns `{"message": "Welcome to the Items API"}`.
- Define a `GET /items` endpoint that returns the full list of items from the `items` list.
- Example response for `GET /items`:
  ```json
  [
    {"id": 1, "name": "Widget", "price": 9.99},
    {"id": 2, "name": "Gadget", "price": 19.99}
  ]
  ```

### 🛠️ Path and Query Parameters

#### Description
Add an endpoint that retrieves a single item by its ID, with an optional query parameter to control the response.

#### Requirements
Completed program should:

- Define a `GET /items/{item_id}` endpoint that returns the matching item using a path parameter.
- Return a `404` error with a clear message if no item matches the given `item_id`.
- Add an optional `include_price` query parameter (default `True`) that, when set to `False`, omits the `price` field from the response.
- Example usage:
  `GET /items/1?include_price=false` returns `{"id": 1, "name": "Widget"}`

### 🛠️ Handling POST Requests with Pydantic

#### Description
Add an endpoint that lets clients create a new item, validating the request body using a Pydantic model.

#### Requirements
Completed program should:

- Define a Pydantic model called `Item` with fields `name` (str) and `price` (float).
- Define a `POST /items` endpoint that accepts an `Item` in the request body.
- Assign the new item a unique `id` and add it to the `items` list.
- Return the newly created item, including its assigned `id`.
- Example request body:
  ```json
  {"name": "Doohickey", "price": 4.99}
  ```
