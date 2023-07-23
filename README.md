## Getting started

Install all required dependencies using the following command:
```
pip install -r requirements.txt
```

Run the application using the following command:
```
python -m uvicorn main:app --reload
```

## Accounts

This API is RESTful and arranged around accounts. As this application has no data behind it, there are no accounts to start with.

An account object is:

| Field | Type | Description |
| ----- | ---- | ----------- |
| name | string | The name of of the account |
| description | string | The description of the account |
| balance | float | The balance of the account |
| active | bool | Indicates the state of the account | 

## Endpoints

### `/healthz`

Get the health status of the application.
```
GET http://http://127.0.0.1:8000/healthz
```

Example response:
```
200 OK
{
    "status":true
}
```

### `accounts/{account_id}`

#### GET

Returns an account.

```
GET http://http://127.0.0.1:8000/accounts/{account_id}
```
Where `account_id` is the account id.

Example response:
```
200 OK
{
  "name": "Account 1",
  "description": "This is account 1",
  "balance": 1000.0,
  "active": true
}
```

Possible errors:

| Error code | Description |
| ---------- | ----------- |
| 422 Unprocessable Entity | The type of the input is invalid. |
| 404 Not Found | An account with the specified id doesn't exist. |

#### POST

Adds an account.
```
PUT http://http://127.0.0.1:8000/accounts/{account_id}
```
Where `account_id` is the account id.

Example request:
```
POST /account/1
{
  "name": "Account 1",
  "description": "This is account 1",
  "balance": 1000,
  "active": true
}
```

Example response:
```
201 Created
{
  "name": "Account 1",
  "description": "This is account 1",
  "balance": 1000.0,
  "active": true
}
```

Possible errors:

| Error code | Description |
| ---------- | ----------- |
| 422 Unprocessable Entity | The type of the input is invalid. |
| 409 Conflict | An account with this `account_id` already exists. |

#### DELETE

Deletes an account
```
DELETE http://http://127.0.0.1:8000/accounts/{account_id}
```

Example response:
```
200 OK
{
  "msg": "Successful"
}
```

| Error code | Description |
| ---------- | ----------- |
| 422 Unprocessable Entity | The type of the input is invalid. |
| 404 Not Found | An account with this `account_id` doesn't exist. |


## Running the application on a container (using Docker)

To create an image, run the following command:
```
docker build -t accounts-api .
```

To create a local container to run the image locally on your machine, tun the following command:
```
docker run -d --name myaccountscontainer -p 8000:80 accounts-api
```