# Pizza Ordering System using FastAPI

This project is a simple Pizza Ordering System built using FastAPI, a modern web framework for building APIs with Python. The system allows users to create pizza orders, update their status, update the items in an order, cancel orders, and view pending orders. The pizza menu is predefined with various pizza options and their details.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies using pip:

```bash
pip install fastapi uvicorn pydantic
```

## How to Use

1. Run the application by executing the following command:

```bash
python app.py
```

2. The application will start running at http://localhost:8000.

## Endpoints

### Create an Order

- **Endpoint:** `/create_order`
- **Method:** POST
- **Input:** JSON payload with `item_ids` (list of integers) and `mobile` (integer).
- **Output:** JSON response with the created order details.

### Update Order Status

- **Endpoint:** `/update_order_status/{order_id}/{status}`
- **Method:** POST
- **Input:** `order_id` (integer) and `status` (string).
- **Output:** JSON response with the updated order ID.

### Update Order Items

- **Endpoint:** `/update_order_items/{order_id}`
- **Method:** POST
- **Input:** `order_id` (integer), `add_item` (list of integers), and `remove_item` (list of integers).
- **Output:** JSON response with the updated total cost of the order.

### Cancel Order

- **Endpoint:** `/cancel_order/{order_id}`
- **Method:** POST
- **Input:** `order_id` (integer).
- **Output:** JSON response confirming the deletion of the order.

### View Pending Orders

- **Endpoint:** `/pending_orders`
- **Method:** GET
- **Output:** JSON response containing all pending orders (orders with status other than "Delivered").

## Sample Usage

Below are some sample calls to the API:

```python
import requests

# Create an order
response = requests.post("http://localhost:8000/create_order", json={"item_ids": [2, 5], "mobile": 1234567890})
print(response.json())  # Returns the details of the created order

# Update order status
response = requests.post("http://localhost:8000/update_order_status/1/Delivered")
print(response.json())  # Returns the order ID with the updated status

# Update order items
response = requests.post("http://localhost:8000/update_order_items/1", json={"add_item": [1, 3], "remove_item": [5]})
print(response.json())  # Returns the updated total cost of the order

# Cancel an order
response = requests.post("http://localhost:8000/cancel_order/2")
print(response.json())  # Returns the deleted order ID

# View pending orders
response = requests.get("http://localhost:8000/pending_orders")
print(response.json())  # Returns a list of all pending orders
```

## Acknowledgments

This project was inspired by the desire to learn FastAPI and build a simple yet functional Pizza Ordering System.