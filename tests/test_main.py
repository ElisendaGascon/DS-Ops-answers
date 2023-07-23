from fastapi import FastAPI
# from fastapi.testclient import TestClient
import requests

## I couldn't get this to work to start a session automatically... 
# from main import app
# client = TestClient(app)

url = "http://127.0.0.1:8000"

def test_can_call_endpoint():
  endpoint = url + "/healthz"
  response = requests.get(endpoint)
  assert response.status_code == 200

def test_get_existing_account_returns_200():
  endpoint = url + "/accounts/1"
  payload = {
    "name": "Account 1",
    "description": "This is account 1",
    "balance": 1000,
    "active": True
  }
  requests.post(endpoint, json=payload)

  response = requests.get(endpoint)
  assert response.status_code == 200

def test_get_non_existing_account_returns_404():
  endpoint = url + "/accounts/2"
  response = requests.get(endpoint)
  assert response.status_code == 404

def test_get_account_invalid_input_returns_422():
  endpoint = url + "/accounts/foo"
  response = requests.get(endpoint)
  assert response.status_code == 422

def test_add_new_account_returns_201():
  endpoint = url + "/accounts/2"
  payload = {
  "name": "Account 2",
  "description": "This is account 2",
  "balance": 2000,
  "active": True
}
  response = requests.post(endpoint, json=payload)
  assert response.status_code == 201

def test_add_existing_account_returns_409():
  endpoint = url + "/accounts/3"
  payload = {
  "name": "Account 3",
  "description": "This is account 3",
  "balance": 3000,
  "active": True
}
  requests.post(endpoint, json=payload)
  response = requests.post(endpoint, json=payload)
  assert response.status_code == 409

def test_delete_existing_account_returns_200():
  endpoint = url + "/accounts/4"
  payload = {
    "name": "Account 4",
    "description": "This is account 4",
    "balance": 4000,
    "active": True
}
  requests.post(endpoint, json=payload)

  response = requests.delete(endpoint)
  assert response.status_code == 200

  response = requests.get(endpoint)
  assert response.status_code == 404
  
def test_delete_non_existing_account_returns_404():
  endpoint = url + "/accounts/5"
  response = requests.delete(endpoint)
  assert response.status_code == 404