# Project Name: REST API Integration & CRUD Test Suite
# Framework: Python Requests
# Author: Indrani Vucha

import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def test_api_crud_operations():
    print("--- Starting API Integration Tests ---")
    
    # 1. READ (GET Request)
    response_get = requests.get(f"{BASE_URL}/1")
    assert response_get.status_code == 200, "GET request failed!"
    print("✓ GET Request Passed: Status 200 OK")
    
    # 2. CREATE (POST Request)
    payload = {
        "title": "Automated API Test",
        "body": "Validating POST request payload verification.",
        "userId": 1
    }
    response_post = requests.post(BASE_URL, json=payload)
    assert response_post.status_code == 201, "POST request failed!"
    print("✓ POST Request Passed: Resource Created (Status 201)")
    
    # 3. UPDATE (PUT Request)
    updated_payload = {
        "id": 1,
        "title": "Updated API Title",
        "body": "Updated payload text.",
        "userId": 1
    }
    response_put = requests.put(f"{BASE_URL}/1", json=updated_payload)
    assert response_put.status_code == 200, "PUT request failed!"
    print("✓ PUT Request Passed: Resource Updated (Status 200)")
    
    # 4. DELETE (DELETE Request)
    response_delete = requests.delete(f"{BASE_URL}/1")
    assert response_delete.status_code == 200, "DELETE request failed!"
    print("✓ DELETE Request Passed: Resource Deleted (Status 200)")

if __name__ == "__main__":
    test_api_crud_operations()
