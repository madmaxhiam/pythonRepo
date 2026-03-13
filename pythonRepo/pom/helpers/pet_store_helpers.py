"""
Body для запросов для API Pet Store
"""

def json_create_or_update_a_pet(pet_id: int, breed: str, name: str) -> dict:
    return {
  "id": pet_id,
  "category": {
    "id": 0,
    "name": breed
  },
  "name": name,
  "photoUrls": [
    "string"
  ],
  "status": "available"
}
