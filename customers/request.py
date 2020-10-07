CUSTOMERS = [
    {
        "id": 1,
        "name": "Bo"
    },
    {
        "id": 2,
        "name": "Duke"
    },
    {
        "id": 3,
        "name": "Daisy"
    },
    {
        "id": 4,
        "name": "Uncle Jesse"
    },
    {
        "id": 5,
        "name": "Boss Hog"
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