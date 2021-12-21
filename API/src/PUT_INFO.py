import requests

put_info_headers = {
    "auth_key": "197394683a7069e85ca2fb34c04d4009f7d4ce0697c14820b4441c2b",
    "pet_id": "ecf952d2-a774-482f-89e1-ba112e162419"
}

put_info_params = put_info_headers
put_info_link = "https://petfriends1.herokuapp.com/api/pets/" + put_info_headers['pet_id']


def put_pet_info(link, p_params, p_headers):
    response = requests.put(link,
                            params=p_params,
                            headers=p_headers
                            )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(put_pet_info(put_info_link, put_info_params, put_info_headers))
