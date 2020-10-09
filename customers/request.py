import customers


CUSTOMERS = [
    {
        "id": 1,
        "name": "Bo",
        "address": "123 Main St"
    },
    {
        "id": 2,
        "name": "Duke",
        "address": "123 Main St"
    },
    {
        "id": 3,
        "name": "Daisy",
        "address": "123 Main St"
    },
    {
        "id": 4,
        "name": "Uncle Jesse",
        "address": "123 Main St"
    },
    {
        "id": 5,
        "name": "Boss Hog",
        "address": "123 Main St"
    }
]

def get_all_customers():
  return CUSTOMERS

def get_single_customer(id):
  requested_customer = None

  for customer in CUSTOMERS:
    if customer["id"] == id:
      requested_customer = customer

  return requested_customer

def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break

def delete_customer(id):
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)