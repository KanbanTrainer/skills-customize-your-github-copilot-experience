# Starter Code for Building REST APIs with FastAPI Assignment
#
# Run this API locally with:
#   pip install fastapi uvicorn
#   uvicorn starter-code:app --reload

from fastapi import FastAPI

app = FastAPI()

# Sample in-memory data
items = [
    {"id": 1, "name": "Widget", "price": 9.99},
    {"id": 2, "name": "Gadget", "price": 19.99},
]

# TODO (Task 1): Define a GET "/" endpoint that returns a welcome message
# TODO (Task 1): Define a GET "/items" endpoint that returns the `items` list

# TODO (Task 2): Define a GET "/items/{item_id}" endpoint that:
#   - Returns the matching item from `items`
#   - Returns a 404 error if no item matches
#   - Supports an optional `include_price` query parameter (default True)

# TODO (Task 3): Define a Pydantic `Item` model with `name` (str) and `price` (float)
# TODO (Task 3): Define a POST "/items" endpoint that:
#   - Accepts an `Item` in the request body
#   - Assigns a new unique id and appends it to `items`
#   - Returns the newly created item
