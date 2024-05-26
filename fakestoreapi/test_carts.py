import requests

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

    