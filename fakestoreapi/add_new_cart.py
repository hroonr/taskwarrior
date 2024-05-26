import requests
import json

# Base URL
base_url = "https://fakestoreapi.com/carts"

# Scenario: Retrieve All Carts
def test_get_all_carts():
    response = requests.get(base_url)
    assert response.status_code == 200, "Failed to retrieve all carts"
    assert isinstance(response.json(), list), "Response is not a list of carts"

# Scenario: Retrieve a Single Cart
def test_get_single_cart():
    cart_id = 1  # Example cart ID
    response = requests.get(f"{base_url}/{cart_id}")
    assert response.status_code == 200, f"Failed to retrieve cart with ID {cart_id}"
    assert response.json()['id'] == cart_id, f"Cart ID does not match {cart_id}"

# Scenario: Add a New Cart
def test_add_new_cart():
    new_cart = {
        "userId": 1,
        "date": "2023-05-24",
        "products": [
            {"productId": 1, "quantity": 2},
            {"productId": 2, "quantity": 3}
        ]
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(base_url, data=json.dumps(new_cart), headers=headers)
    assert response.status_code == 200 or response.status_code == 201, "Failed to add new cart"
    new_cart_id = response.json()['id']

    # Verify the new cart is added
    get_response = requests.get(f"{base_url}/{new_cart_id}")
    assert get_response.status_code == 200, "Failed to retrieve the newly added cart"
    assert get_response.json()['id'] == new_cart_id, "New cart ID does not match"

# Scenario: Update a Cart
def test_update_cart():
    cart_id = 1  # Example cart ID
    updated_cart = {
        "userId": 1,
        "date": "2023-05-24",
        "products": [
            {"productId": 1, "quantity": 5},  # Updated quantity
            {"productId": 2, "quantity": 1}
        ]
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f"{base_url}/{cart_id}", data=json.dumps(updated_cart), headers=headers)
    assert response.status_code == 200, f"Failed to update cart with ID {cart_id}"

    # Verify the cart is updated
    get_response = requests.get(f"{base_url}/{cart_id}")
    assert get_response.status_code == 200, "Failed to retrieve the updated cart"
    assert get_response.json()['products'][0]['quantity'] == 5, "Cart product quantity was not updated"

# Scenario: Delete a Cart
def test_delete_cart():
    cart_id = 1  # Example cart ID
    response = requests.delete(f"{base_url}/{cart_id}")
    assert response.status_code == 200, f"Failed to delete cart with ID {cart_id}"

    # Verify the cart is deleted
    get_response = requests.get(f"{base_url}/{cart_id}")
    assert get_response.status_code == 404, "Deleted cart is still retrievable"
