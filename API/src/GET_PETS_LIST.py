import requests

# "key": "197394683a7069e85ca2fb34c04d4009f7d4ce0697c14820b4441c2b"

get_headers_my_pets = {
    "auth_key ": "197394683a7069e85ca2fb34c04d4009f7d4ce0697c14820b4441c2b",
    "filter": "my_pets"
}

get_params_my_pets = get_headers_my_pets

my_pets_link = "https://petfriends1.herokuapp.com/api/pets?filter=my_pets"


def get_pets_list(link, params, headers):
    response = requests.get(link,
                            params=params,
                            headers=headers
                            )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(get_pets_list(my_pets_link, get_params_my_pets, get_headers_my_pets))
