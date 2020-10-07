LOCATIONS = [
    {
        "id": 1,
        "name": "Seattle"
    },
    {
        "id": 2,
        "name": "Los Angeles"
    },
    {
        "id": 3,
        "name": "San Diego"
    },
    {
        "id": 3,
        "name": "Nashville"
    }
]

def get_all_locations():
  return LOCATIONS

def get_single_location(id):
  requested_location = None

  for location in LOCATIONS:
    if location["id"] == id:
      requested_location = location

  return requested_location
