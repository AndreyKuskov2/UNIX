import requests

delete_pet_headers = {
    "auth_key": "197394683a7069e85ca2fb34c04d4009f7d4ce0697c14820b4441c2b",
    "pet_id": "195ff726-8900-42d2-902e-059b4f66de85"
}

delete_pet_params = delete_pet_headers
DELETE_pet_link = "https://petfriends1.herokuapp.com/api/pets/" + delete_pet_headers['pet_id']


def delete_pet(link, del_params, del_headers):
    response = requests.delete(link,
                               params=del_params,
                               headers=del_headers
                               )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(delete_pet(DELETE_pet_link, delete_pet_params, delete_pet_headers))
